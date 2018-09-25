# -*- coding: utf-8 -*-

import os
import redis
import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__) # create the application instance

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
r = redis.from_url(redis_url)

counter_key = os.getenv('COUNTER_KEY', 'counters')

def validate_key(key):
    if key == None or key == '':
        return 418
    if len(key) > 256:
        return 413
    return 200

@app.route('/')
def index():
    return render_template('index.html', counters=r.hgetall(counter_key))

@app.route('/c/<key>')
def get_counter(key):
    validate = validate_key(key)
    if validate == 200:
        return r.hget(counter_key, key)
    return jsonify({ 'error': validate }), validate

@app.route('/c', methods=['POST'])
def inc_counter():
    data = json.loads(request.data.decode())
    key = data.get('key') or None
    validate = validate_key(key)
    if validate == 200:
        ret = r.hincrby(counter_key, key, 1)
    return jsonify({ 'status': validate })

if __name__ == "__main__":
    app.run()