import pytest
from auth import Auth
from api_helper import APIHelper
import requests

def test_invalid_auth():
    with pytest.raises(Exception):
        auth = Auth("https://sandbox-sdwan-2.cisco.com", "baduser", "badpass")
        auth.get_token()

def test_invalid_endpoint():
    auth = Auth("https://sandbox-sdwan-2.cisco.com", "admin", "C1sco12345")
    token = auth.get_token()
    api = APIHelper("https://sandbox-sdwan-2.cisco.com", token)
    with pytest.raises(requests.exceptions.HTTPError):
        api.get("/invalid-endpoint")
