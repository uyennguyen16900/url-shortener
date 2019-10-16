from flask import Flask, render_template, redirect, request
import sys
from shortener import URL_shortener
from pymongo import MongoClient
from bson.objectid import ObjectId
import redis
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
urls = db.urls

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('new')
def url_new():
    return render_template('url_new.html', urls={})

@app.route('/shorten', methods=['POST'])
def return_shortened():
    url_shortener = URL_shortener()
    url = request.form['url']
    short_url = url_shortener.shorten_url(url)
    return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_short_url(short_url):
    link_target = urls.find_one({'_id': ObjectId(short_url)})
    if link_target is None:
        raise NotFound()
    # redis.incr('click-count:' + short_url)
    return redirect(link_target)

if __name__ == "__main__":
    app.run(debug=True)
