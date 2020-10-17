from werkzeug.utils import secure_filename
from app import app
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

@app.route('/javascript/<path:jsfile>', methods=['GET'])
def jshandler(jsfile):
    jsfile = secure_filename(jsfile)
    return send_from_directory('./javascript', jsfile)
