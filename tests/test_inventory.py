from auth import Auth
from api_helper import APIHelper

def test_inventory_fetch():
    auth = Auth("https://sandbox-sdwan-2.cisco.com", "admin", "C1sco12345")
    token = auth.get_token()
    api = APIHelper("https://sandbox-sdwan-2.cisco.com", token)
    data = api.get("/device")

    assert "data" in data and isinstance(data["data"], list)

    print("\nSD-WAN Devices:")
    for d in data["data"]:
        print(f"{d['host-name']} - {d['device-type']} - {d['reachability']}")
