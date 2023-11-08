from fastapi import APIRouter, Depends
import stripe
from fastapi import APIRouter, Header, Request
from routers.router_auth import get_current_user
from firebase_admin import auth
from database.firebase import db

from dotenv import dotenv_values

import json
stripe_config = json.loads(dotenv_values(dotenv_path='.exemple.env')['STRIPE_CONFIG'])
stripe.api_key = stripe_config['private_key']

YOUR_DOMAIN = 'http://localhost'

router = APIRouter(
    tags=["Stripe"],
    prefix='/stripe'
)

@router.post('/checkout')
async def stripe_checkout():
    try:
        checkout_session = stripe_checkout.Session.create(
            line_items = [
                {
                    #price id du produit qu'on veut vendre
                    'price': stripe_config['price_id'],
                    'quantity':1,
                },
                
            ],
            mode = 'payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return checkout_session
    except Exception as e:
        return str(e)
    
    

    
    # create webhook endpoint
@router.post('/webhook')
async def webhook_received(request:Request, stripe_signature: str = Header(None)):
    # use request to get a body and stripe  signature from the header to validate the payload 
    webhook_secret = stripe_config['webhook_secret']
    # stock the data from the request
    data = await request.body
    
    #construct a webhook event using the stripe library
    
    try:
        # call  the construct event function  on the stripe library passing the event data
        event = stripe.Webhook.construct_event(
            #use the webhook secret and the stripe signature  from the header to validate the event 
            payload=data,
            sig_header=stripe_signature,
            secret=webhook_secret
        )
        # pull out the event data 
        event_data = event['data']
        # return error and raise 
    except Exception as e:
        return {'error':str(e)}
    
    # handle the event that we received 
    event_type = event ['type']
    if event_type == 'checkout.session.completed': print('Checkout session completed')
    elif event_type == 'invoice.paid':
        print('Invoice paid')
        customer_email = event_data['object']['customer_email']
        firebase_user = auth.get_user_by_email(customer_email)
        customer_id = event_data['object']['customer']
        item_id = event_data['object']['lines']['data'][0]['subscription_item']
        db.child('user').child(firebase_user.uid).child('stripe').set(
            data={
                'item_id':item_id,
                'customer_id':customer_id
            }
        )
    elif event_type == 'invoice.payment_failed': print('Invoice payment failed')
    else : print(f'Unhandled event: {event_type}')



@router.get('/usage')
async def stripe_usage(userData: int = Depends(get_current_user)):
    fireBase_user= auth.get_user(userData['uid'])
    stripe_data= db.child("users").child(fireBase_user.uid).child("stripe").get().val()
    cust_id = stripe_data["cust_id"]
    return stripe.Invoice.upcoming(customer=cust_id)


def increment_stripe(userId:str):
    firebase_user= auth.get_user(userId) #identifiant firebase correspondant (uid)]
    stripe_data = db.child("user").child(firebase_user.uid).child("stripe").get().val()
    print(stripe_data.values())
    item_id= stripe_data['item_id']
    stripe.SubscriptionItem.create_usage_record(item_id, quantity=1)
    return
