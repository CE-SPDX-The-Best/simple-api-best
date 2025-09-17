from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def welcome():
	return jsonify({'message': 'Hello, World!'})

@app.route('/plus/<int:n1>/<int:n2>', methods=['GET'])
def plus(n1, n2):
    return jsonify({'message': n1 + n2})

if __name__ == '__main__':
	app.run(debug=True, port=5000)