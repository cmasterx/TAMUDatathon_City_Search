from flask.helpers import send_file, send_from_directory
from app import app

@app.route('/fav')
def fav():
    return send_from_directory('./assets', 'city.ico')