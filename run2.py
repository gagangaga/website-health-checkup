from flask import Flask, render_template, send_from_directory
from flask import request

app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory("static", path)

@app.route('/')
def hello_world():
    return render_template('web2.html')

@app.route('/render', methods=['GET'])
def products():







if __name__ == '__main__':
    app.run(debug=True, port=5000)