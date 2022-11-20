from os import environ 
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(environ.get("MONGO_URI"))
db = client.noonalu

@app.route('/')
def hello_world():
    calenders_collection = db['calender']
    return list(calenders_collection.find({}))



if __name__ == '__main__':
    app.run()
