import pytest
from flask import url_for
from bs4 import BeautifulSoup

@pytest.fixture
def page(client):
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


def test_species(page):
    assert page.select('li p')[0].text == 'Amanita muscaria (100%)'
    assert page.select('li p')[1].text == 'Hypholoma australianum (0%)'
    assert page.select('li p')[2].text == 'Amanita flavella (0%)'
    assert page.select('li p')[3].text == 'Hypholoma brunneum (0%)'
    assert page.select('li p')[4].text == 'Chlorophyllum brunneum (0%)'

def test_photos(page):
    for i in range(5):
        photos = page.select('li')[i].select('img')
        assert len(photos) == 2
        check_photo(photos[0])
        check_photo(photos[1])


def check_photo(photo):
    assert photo['src'][:8] == 'https://'
    assert photo.parent()[1].text.strip()[:8] == 'Photo by'
