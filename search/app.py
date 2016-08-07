#!/usr/bin/python
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    return jsonify([{'text': "Hello, World!", 'author': 'Name'}, {'query': query}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
