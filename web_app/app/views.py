from flask.helpers import send_from_directory
from app import app
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        print(request.form)
        return request.form
    
    print(request.form)
    
    return 'Howdy!'

@app.route('/', methods=['GET'])
def root():
    return render_template('./html/index.html')

@app.errorhandler(404)
def handler404(e):
    return '<h1>404 Error</h1>', 404
