from auth import Auth

def test_token_retrieval():
    auth = Auth("https://sandbox-sdwan-2.cisco.com", "admin", "C1sco12345")
    token = auth.get_token()
    assert isinstance(token, dict)
    assert "JSESSIONID" in token
