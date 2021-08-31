from app.lib.photos import Photos

def test_num_photos():
    photos = Photos()
    my_photos = photos.get_photos('amanita muscaria', 3)
    assert len(my_photos) == 3

def test_image_url():
    photos = Photos()
    my_photos = photos.get_photos('amanita muscaria', 3)
    assert 'https://' in my_photos[0]['image_url']

def test_attribution():
    photos = Photos()
    my_photos = photos.get_photos('amanita muscaria', 3)
    assert len(my_photos[0]['user_login']) > 0
