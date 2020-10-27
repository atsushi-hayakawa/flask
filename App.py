from flask import *
from controller import SampleController

app = Flask(__name__)
app.register_blueprint(SampleController.app, url_prefix='/')

if __name__ == '__main__':
    app.run(port=8080)
