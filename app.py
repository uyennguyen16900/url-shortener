from flask import Flask, render_template, redirect, request, url_for
from shortener import URL_shortener
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/urlshortener')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
urls = db.urls

app = Flask(__name__)

URL = "http://127.0.0.1:5000/"

@app.route('/')
def index():
    """Show the home page"""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def return_shortened():
    """Shorten the original url and print it"""
    url_shortener = URL_shortener()
    original_url = request.form['original_url']
    short_url = url_shortener.shorten_url(original_url)
    url = {
        'original_url': original_url,
        'shortened_url': short_url
    }
    on_heroku = False
    if 'YOUR_ENV_VAR' in os.environ:
        on_heroku = True
        URL = "https://url-shortener-un.herokuapp.com/"
    short_id = urls.insert_one(url).inserted_id
    return render_template('result.html', url=url, URL=URL)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Expand the shortened url and redirect back to original url"""
    link_target = urls.find_one({'shortened_url': short_url})
    if link_target:
        return redirect(link_target["original_url"])
    return 'Not working'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
