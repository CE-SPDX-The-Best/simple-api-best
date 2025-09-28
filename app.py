from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/is_prime/<int:x>', methods=['GET'])
def is_prime(x):
	if x == 2 or x == 3:
		return jsonify({'message': True})
	for i in range(2, i):
		if x % i == 0:
			return jsonify({'message': False})
	return jsonify({'message': True})

# @app.route('/plus/<string:n1>/<string:n2>', methods=['GET'])
# def plus(n1, n2):
# 	n1, n2 = int(n1), int(n2)
# 	return jsonify({'message': n1 + n2})

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)