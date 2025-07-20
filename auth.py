import os
import requests

class Auth:
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.token = None

    def get_token(self):
        login_url = f"{self.base_url}/j_security_check"
        payload = {
            "j_username": self.username,
            "j_password": self.password
        }
        session = requests.Session()
        response = session.post(login_url, data=payload, verify=False)
        if "html" in response.text.lower():
            raise Exception("Login failed")
        self.token = session.cookies.get_dict()
        return self.token
