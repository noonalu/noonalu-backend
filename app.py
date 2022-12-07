from os import environ
from flask import Flask, json
from bson import json_util
from pymongo import MongoClient
from db import *
from api import *
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)
api.add_resource(Event, "/event")
api.add_resource(ValidateUser, "/validate")


if __name__ == "__main__":
    app.run()
