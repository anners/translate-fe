from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('lang.html')

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
