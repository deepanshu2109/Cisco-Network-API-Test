from auth import Auth
from api_helper import APIHelper
import os

# Load from env or hardcode here
BASE_URL = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "admin"
PASSWORD = "C1sco12345"

auth = Auth(BASE_URL, USERNAME, PASSWORD)
token = auth.get_token()

api = APIHelper(BASE_URL, token)
devices = api.get("/device")

for d in devices["data"]:
    print(f"{d['host-name']} - {d['device-type']} - {d['reachability']}")
