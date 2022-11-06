import requests, json, imghdr

# Tests if the stocks API returns a list
def test_stocklist():
    res = requests.get("http://api:8000/stocks")

    x=json.loads(res.text) 

    assert type(x) is list

# Tests if the correlation API returns a picture
def test_correlation():
    res = requests.get("http://api:8000/correlation?stock1=stock1&stock2=stock2")

    assert res.headers['Content-Type'] == 'image/png'