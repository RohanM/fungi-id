from flask import Blueprint
from flask import request
from flask import render_template

from fastai.vision.all import *

bp = Blueprint('identification', __name__)

@bp.route("/identification", methods=['POST'])
def create():
    photo = request.files['photo']
    predictions = predict(photo.stream)
    return render_template('identification.html', predictions=predictions)


def predict(photo):
    learner = load_learner('models/model.pkl')
    image = PILImage.create(photo)

    _, _, outputs = learner.predict(image)
    predictions = get_top_predictions(5, outputs, learner.dls.vocab)

    return predictions

def get_top_predictions(num_predictions, outputs, vocab):
    top_classes = outputs.topk(num_predictions)

    return [
        {
            'scientific_name': format_scientific_name(
                vocab[top_classes.indices[i]],
            ),
            'confidence': round(top_classes.values[i].item()*100)
        } for i in range(num_predictions)
    ]


def format_scientific_name(scientific_name):
    return scientific_name.replace('_', ' ').capitalize()
