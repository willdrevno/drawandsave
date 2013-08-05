import os
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

@app.route('/')
def hello():
    return render_template('index.html')