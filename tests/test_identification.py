import pytest
from flask import url_for


def test_identification(app, client):
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
    assert b'Amanita muscaria' in response.data
