from flask import Flask
from FlaskApi import app

@app.route('/')
@app.route('/home')
def home():
    return "Hello Flask!"
