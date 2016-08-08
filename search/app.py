#!/usr/bin/python
from flask import Flask, jsonify
from flask import request

from flask_pymongo import PyMongo
import json
from bson import json_util


app = Flask(__name__, static_url_path='')

# configuration
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'items'

mongo = PyMongo(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    data = mongo.db.article_items.find({'$text': {'$search': query}} , {'_id': 0, 'text': 0, 'hash': 0, 'score': {'$meta': "textScore"}}).sort([('score', {'$meta': "textScore"})])
    #res = json.dumps(data, default=json_util.default)
    res = [r for r in data]
    for r in res:
        del r['score']
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
