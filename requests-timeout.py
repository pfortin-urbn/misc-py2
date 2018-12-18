import requests
import json

headers = {
            "Content-Type": "application/json"
}
payload = {
    "test": 1,
    "active": True,
}

text = requests.post('http://requestbin.fullcontact.com/186d34m1', data=json.dumps(payload), headers=headers, timeout=(2, 10))
print(text)