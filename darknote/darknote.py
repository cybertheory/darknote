from flask import Flask, render_template
import os

class DarkNote():

    app = Flask(__name__)

    def write():
        pass

    @app.route('/')
    def hello():
        return render_template('templates/template.html')
