# Client code (client_app.py)
import requests

response = requests.get("http://api_service:5000/data")
print(response.json())