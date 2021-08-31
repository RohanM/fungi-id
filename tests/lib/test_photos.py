from app.lib.photos import Photos

def test_get_photos():
    photos = Photos()
    my_photos = photos.get_photos('amanita muscaria', 3)
    assert len(my_photos) == 3
