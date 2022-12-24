from flask import Flask
from api import *
from flask_restful import Api
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

# Handles all event data
api.add_resource(Event, "/event")

# Handles all user related services
api.add_resource(ValidateUser, "/validate")

if __name__ == "__main__":
    load_dotenv()
    app.run()
