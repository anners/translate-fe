from flask import Flask, request, render_template, send_file
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
    return render_template('hello.html', helloworld=hello.text)

@app.route('/health')
def health():
    return 'healthly'

@app.route("/image/<filename>")
def get_image(filename):
    return send_file(filename, mimetype='image/jpg')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
