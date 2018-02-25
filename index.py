from flask import Flask, request, render_template
from google.cloud import translate
import requests
app = Flask(__name__)

@app.route('/')
def home():
    client = translate.Client()
    languages = client.get_languages()
    return render_template('lang-dropdown.html', languages=languages)

@app.route('/submit')
def submit():
    lang = request.args.get('lang')
    hello = requests.get('http://translate-service/hello/' + lang)
    return hello.text

@app.route('/health')
def health():
    return 'healthly'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
