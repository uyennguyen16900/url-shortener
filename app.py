from flask import Flask, render_template, redirect, request, url_for
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

@app.route('/new')
def url_new():
    return render_template('url_new.html', urls={})

@app.route('/shorten', methods=['POST'])
def return_shortened():
    url_shortener = URL_shortener()
    original_url = request.form['original_url']
    short_url = url_shortener.shorten_url(original_url)
    url = {
        'original_url': original_url,
        'shortened_url': short_url
    }
    short_id = urls.insert_one(url).inserted_id
    return render_template('result.html', short_url=short_url, original_url=original_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    # link_target = urls.find_one({'shortened_url': short_url}, {'original_url': 1, 'shortened_url': 0})
    link_target = urls.find_one({'shortened_url': short_url})
    if link_target is None:
        raise NotFound()
    # return redirect(link_target.get(original_url))
    return render_template('test.html', link_target=link_target)

if __name__ == "__main__":
    app.run(debug=True)
