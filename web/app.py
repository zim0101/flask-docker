from flask import Flask, jsonify
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


@app.route('/')
def getData():
	data = {
		'a': 1,
		'b': 2
	}
	return jsonify(data)


if __name__ == '__main__':
	app.run(host='0.0.0.0')