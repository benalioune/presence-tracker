import requests


token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ0OWU0N2ZiZGQ0ZWUyNDE0Nzk2ZDhlMDhjZWY2YjU1ZDA3MDRlNGQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2Vzc2lvbnRyYWNrZXItNmZlMWUiLCJhdWQiOiJzZXNzaW9udHJhY2tlci02ZmUxZSIsImF1dGhfdGltZSI6MTY5OTE0NTYxMCwidXNlcl9pZCI6InFEM1Zad3RwN05lMTR1ckxpdlN3bHQ5a0hOQTIiLCJzdWIiOiJxRDNWWnd0cDdOZTE0dXJMaXZTd2x0OWtITkEyIiwiaWF0IjoxNjk5MTQ1NjEwLCJleHAiOjE2OTkxNDkyMTAsImVtYWlsIjoiYmVuYWxpb3VuZTZAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImJlbmFsaW91bmU2QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.AJHUJvx0o6U6ijd9E3XK2_rReQnx9nEjZiTY0W7-7AwZNX5d0-oXOZq1eNK0arVBsE1mx-lSxo_AVqNLQEfPz_Ju3chsOgmNhQDYH9CMpZijERkmQVZ2THot-2puA_VTlZt_5QabSVnB78IHUo5AI93qZdrLDgH9Q-TQzUiZnKJVjqG1nNL6Wler-O0BWr3yW6m3XFToJvcRYw9sUoE33XxronF3VJ-Qla1KEOJDzmTNr57nMTp3Vr4YD0GtOrXJt_fynK0auW1BSZ-TJD24nd-36wn3pbX6W3O_LFljtrFLfSn7RVlf1WzW0CA2QGE7Vgix3c3wbMocaKPQHt3Dtg"

def test_validate_endpoint():
    headers = {
        'authorization' : token
    }
    
    
    response = requests.post(
        "http://127.0.0.1:8000/ping",
        headers=headers
    )
    
    return response.text

print(test_validate_endpoint())