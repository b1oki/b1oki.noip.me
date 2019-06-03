#!python3

from flask import Flask
from flask import render_template
from flask_cors import cross_origin

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def root():
    return render_template('root.html')


@app.route('/health.php', methods=['GET'])
@cross_origin(origins=['https://alexandersobyanin.ru'], methods=['GET'])
def health():
    return '{"health":1}'


@app.route('/ads.txt', methods=['GET'])
def ads():
    return 'google.com, pub-8901069185828760, DIRECT, f08c47fec0942fa0'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
