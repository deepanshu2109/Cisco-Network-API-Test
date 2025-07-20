import requests
import urllib3
urllib3.disable_warnings()

class APIHelper:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def get(self, endpoint):
        url = f"{self.base_url}/dataservice{endpoint}"
        response = requests.get(url, cookies=self.token, verify=False)
        response.raise_for_status()
        return response.json()
    
    
