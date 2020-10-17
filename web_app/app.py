from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory
from flask_cors import CORS
import json
import socket
import atexit

app = Flask(__name__)
CORS(app)

def exit_handler():
    print('Closing app')

def get_app():
    return app

@app.route('/', methods=['GET'])
def root():
    return 'Hello world!'

@app.errorhandler(404)
def handler404():
    return '<h1>404 Error</h1>'

if __name__ == '__main__':
    atexit.register(exit_handler)
    app.run(host='0.0.0.0', port=8000)