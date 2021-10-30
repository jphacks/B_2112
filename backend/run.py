from os import name
from flask import Flask, render_template, jsonify, request
from werkzeug.wrappers import response
from flask_cors import CORS
from random import *
from visualwordsTwitter import word_cloudt
from visualwords import word_cloud
from PIL import Image
import numpy as np
import base64
from getTweet import mkTweetFile
import db

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/u_word', methods={'POST'})
def u_word_cloud():
    number = request.form['number']
    text = request.form['text']
    word_cloud(number, text)
    response = {
        'res': '1'
    }
    return jsonify(response)

@app.route('/api/word', methods=['POST'])
def wordcloud():
    number = request.form['number']
    text = mkTweetFile()
    print(number)
    word_cloudt(number,text)
    response = {
        'res': '1'
    }
    return jsonify(response)

@app.route('/api/createdb', methods={'POST'})
def createDB():
    name = request.form['name']
    db.Initiate_DB(name)
    return '1'

@app.route('/api/bookinfo', methods=['POST'])
def getbookinfo():
    name = request.form['name']
    bookinfo = db.getallbooks(name)
    
    return bookinfo

@app.route('/api/add', methods={'POST'})
def add():
    isbn = request.form['isbn']
    date = request.form['date']
    name = request.form['name']
    bookinfo = db.Edit_DB(name, isbn, date)

    return bookinfo
        

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
