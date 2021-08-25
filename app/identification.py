from flask import Blueprint
from flask import request
from flask import render_template

from fastai.vision.all import *

bp = Blueprint('identification', __name__)

@bp.route("/identification", methods=['POST'])
def create():
    photo = request.files['photo']
    scientific_name = predict(photo.stream)
    return render_template('identification.html', scientific_name=scientific_name)


def predict(photo):
    learner = load_learner('models/model.pkl')
    image = PILImage.create(photo)
    result = learner.predict(image)
    return format_scientific_name(result[0])

def format_scientific_name(scientific_name):
    return scientific_name.replace('_', ' ').capitalize()
