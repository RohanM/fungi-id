from bs4 import BeautifulSoup

def test_index(client):
    rv = client.get('/')
    soup = BeautifulSoup(rv.data, 'html.parser')
    assert soup.select('h1')[0].string == 'Hello, world!'
