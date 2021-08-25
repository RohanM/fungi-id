import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def index(client):
    rv = client.get('/')
    return BeautifulSoup(rv.data, 'html.parser')


def test_title(index):
    assert index.select('h1')[0].string == 'Australian Fungi ID'

def test_upload_present(index):
    assert len(index.select('form')) == 1
