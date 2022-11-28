from os import environ
from flask import Flask, json
from bson import json_util
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(environ.get("MONGO_URI"))
db = client.noonalu


@app.route('/')
def hello_world():
    # calenders_collection = db['calender']
    # return json.loads(json_util.dumps(list(calenders_collection.find({}))))
    return 'Hello, World!'
