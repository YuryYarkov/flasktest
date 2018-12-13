from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__, static_url_path = "")

import views


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
