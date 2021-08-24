def test_index(client):
    rv = client.get('/')
    assert b'Hello, world!' in rv.data
