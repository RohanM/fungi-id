from flask import Blueprint
from flask import request
from flask import render_template

bp = Blueprint('identification', __name__)

@bp.route("/identification", methods=['POST'])
def create():
    photo = request.files['photo']
    return render_template('identification.html')
