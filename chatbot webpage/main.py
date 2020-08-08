from flask import Flask, request
import json

PORT = 80
DEBUG = True

app = Flask(__name__, static_folder="web", static_url_path='')

@app.route('/')
def root():
	return app.send_static_file("index.html")

if __name__ == "__main__":
	app.run(port=PORT, debug=DEBUG)