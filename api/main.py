import os

from flask import Flask
from api.api_routes import api_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
