import requests, json, imghdr

# Tests if the stocks API is online
def test_positive_stocklist_online():
    res = requests.get("http://api:8000/stocks")
    assert res.status_code == 200

# Tests if the stocks API returns a list
def test_positive_stocklist():
    res = requests.get("http://api:8000/stocks")
    x=json.loads(res.text) 
    assert type(x) is list

# Tests if the correlation API is online
def test_positive_correlation_online():
    res = requests.get("http://api:8000/correlation?stock1=A&stock2=AAPL")
    assert res.status_code == 200

# Tests if the correlation API returns a picture
def test_positive_correlation_return_type():
    res = requests.get("http://api:8000/correlation?stock1=A&stock2=AAPL")
    assert res.headers['Content-Type'] == 'image/png'

# Tests if the correlation API errors out if parameters aren't provided
def test_negative_correlation_online():
    res = requests.get("http://api:8000/correlation")
    assert res.status_code != 200
