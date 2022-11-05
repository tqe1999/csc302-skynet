import requests, json

# Tests if the stocks API returns a list
def test_stocklist():
    res = requests.get("http://api:8000/stocks")

    x=json.loads(res.text) 

    assert type(x) is list