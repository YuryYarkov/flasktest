from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__, static_url_path = "")

import views



if __name__ == '__main__':
    app.run(host='0.0.0.0')
