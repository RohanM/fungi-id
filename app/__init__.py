import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import index
    app.register_blueprint(index.bp)

    from . import identification
    app.register_blueprint(identification.bp)

    return app
