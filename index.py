# pylint: skip-file
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
if response.status_code == 200:
    print(response.content)
