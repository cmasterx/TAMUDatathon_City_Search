from app import app
import json
import socket
import atexit

def exit_handler():
    print('Closing app')

if __name__ == '__main__':
    atexit.register(exit_handler)
    app.run(host='0.0.0.0', port=8000)