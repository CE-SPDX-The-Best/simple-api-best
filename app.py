from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def welcome():
	return jsonify({'message': 'Hello, KMITL'})

@app.route('/plus/<string:n1>/<string:n2>', methods=['GET'])
def plus(n1, n2):
	n1, n2 = int(n1), int(n2)
	return jsonify({'message': n1 + n2})

@app.route('/is_prime/<string:x>', methods=['GET'])
def is_prime(x):
    x = int(x)
    if x<=1:
        return jsonify({'message': False})
    if x==2:
        return jsonify({'message': True})
    if x%2==0:
        return jsonify({'message': False})
    for i in range(3, int(x**0.5)+1, 2):
        if x%i==0:
            return jsonify({'message': False})
    return jsonify({'message': True})
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)