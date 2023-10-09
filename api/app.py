
from flask import Flask
from api.api_routes import api_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')
app.config['JSON_AS_ASCII'] = False

