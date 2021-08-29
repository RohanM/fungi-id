from flask import Blueprint
from flask import request
from flask import render_template

from app.lib.model import predict

bp = Blueprint('identification', __name__)

@bp.route("/identification", methods=['POST'])
def create():
    photo = request.files['photo']
    predictions = predict(photo.stream)
    return render_template('identification.html', predictions=predictions)
