import redis
from flask import Flask
app = Flask(__name__)
redis = redis.Redis(host=35.222.53.4, port=30007, db=0)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/visitor')
def visitor():
    redis.incr('visitor')
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor: %s" % (visitor_num)
@app.route('/visitor/reset')
def reset_visitor():
    redis.set('visitor', 0)
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor is reset to %s" % (visitor_num)

