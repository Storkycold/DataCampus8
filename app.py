import os
import sys
import cv2
import numpy as np
from flask import Flask, render_template, jsonify, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# HTML을 주는 부분


@app.route('/', methods=['POST', 'GET'])
def mainpage():
    return render_template('mainpage.html')


@app.route('/imagetoimage', methods=['POST', 'GET'])
def imagetoimage():
    return render_template('imagetoimage.html')


@app.route('/texttoimage', methods=['POST', 'GET'])
def texttoimage():
    return render_template('texttoimage.html')


# @app.route('/lightbox', methods=['POST', 'GET'])
# def lightbox():
#    return render_template('lightbox.html')

@app.route('/lightbox', methods=['POST', 'GET'])
def lightbox():
    return render_template('lightbox.html')


# 서버 연결
if __name__ == '__main__':
    app.run()
