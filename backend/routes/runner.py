from flask_cors import CORS
from flask import Flask

from .admin import admin_bp
from .chatbot import chatbot_bp
from .server import server_bp
from .user import user_bp
from .db import db_bp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(admin_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(server_bp)
app.register_blueprint(user_bp)
app.register_blueprint(db_bp)


@app.errorhandler(Exception)
def handle_exception(e):
    return {'error': str(e)}, 500
