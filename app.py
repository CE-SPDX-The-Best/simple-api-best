from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def welcome():
	return jsonify({'message': 'Hello, CEDT32'})

@app.route('/plus/<string:n1>/<string:n2>', methods=['GET'])
def plus(n1, n2):
	n1, n2 = int(n1), int(n2)
	return jsonify({'message': n1 + n2})

if __name__ == '__main__':
	app.run(debug=True, port=5000)