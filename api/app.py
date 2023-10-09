
from flask import Flask, jsonify

from api.api_impl import search, match_data
from api.api_routes import api_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')
app.config['JSON_AS_ASCII'] = False


@app.route('/hello/',methods=["GET"])
def search1():
    return jsonify({"hello": "world"})


@app.route('/', methods=["GET"])
def search2():
    return jsonify({"hello": "world"})


@app.route('/search', methods=['POST'])
def search_route():
    return search()


@app.route('/match_data', methods=['POST'])
def match_data_route():
    return match_data()
