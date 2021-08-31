from flask import Blueprint
from flask import request
from flask import render_template

from app.lib.model import predict
from app.lib.photos import Photos


bp = Blueprint('identification', __name__)


@bp.route("/identification", methods=['POST'])
def create():
    photo = request.files['photo']
    all_photos = Photos()

    predictions = predict(photo.stream)
    predictions = add_photos(predictions, all_photos)

    return render_template('identification.html', predictions=predictions)


def add_photos(predictions, all_photos):
    return [
        {
            **prediction,
            **{ 'photos': all_photos.get_photos(prediction['scientific_name'].lower())}
        } for prediction in predictions
    ]
