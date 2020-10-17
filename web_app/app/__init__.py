from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

__all__ = ['views', 'js', 'common']
from app import *