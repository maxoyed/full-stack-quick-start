# -*- coding:utf-8 _*-
"""
@author: maxoyed
@file: app.py
@time: 2019/03/21
@contact: maxoyed@gmail.com
@site: https://maxoyed.com

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from flask import Flask, jsonify, Blueprint, request, render_template
from flask_cors import *

app = Flask(__name__, static_folder="../dist", template_folder="../dist", static_url_path='')
CORS(app, supports_credentials=True)

api = Blueprint('api', __name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/hello-world', methods=['GET'])
def hello_world():
    return jsonify({
        "code": 20000,
        "message": "success",
        "data": "Hello World"
    })


app.register_blueprint(api, url_prefix="/api")
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
