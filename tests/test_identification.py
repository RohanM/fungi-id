import pytest
from flask import url_for
from bs4 import BeautifulSoup

@pytest.fixture
def id(client):
    photo = open('tests/data/aminita_muscaria_6119419.jpg', 'rb')
    data = {
        'photo': (photo, 'photo.jpg')
    }
    response = client.post(
        url_for('identification.create'),
        data=data,
        follow_redirects=True,
        content_type='multipart/form-data'
    )
    return BeautifulSoup(response.data, 'html.parser')


def test_top_five(id):
    assert id.select('.prediction')[0].string == 'Amanita muscaria (100%)'
    assert id.select('.prediction')[1].string == 'Hypholoma australianum (0%)'
    assert id.select('.prediction')[2].string == 'Amanita flavella (0%)'
    assert id.select('.prediction')[3].string == 'Hypholoma brunneum (0%)'
    assert id.select('.prediction')[4].string == 'Chlorophyllum brunneum (0%)'
