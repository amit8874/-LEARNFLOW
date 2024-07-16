from flask import Flask, request, redirect, render_template_string
import string
import random

app = Flask(__name__)

# In-memory storage for URLs
url_mapping = {}

# Generate a short URL
def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url

# Home page with form to submit URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        url_mapping[short_url] = long_url
        return render_template_string("""
            <h1>URL Shortener</h1>
            <p>Short URL: <a href="/{{short_url}}">{{request.host}}/{{short_url}}</a></p>
            <a href="/">Shorten another URL</a>
        """, short_url=short_url)
    return '''
        <h1>URL Shortener</h1>
        <form method="post">
            Long URL: <input type="text" name="long_url">
            <input type="submit" value="Shorten">
        </form>
    '''

# Redirect to the original long URL
@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    return '<h1>URL not found</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)
