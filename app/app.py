from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
	return "<h1>This just exists to simple serve a js script.</h1>"

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug=False, ssl_context='adhoc')