import db as db
import utils
from flask_restful import Resource, request
from flask import Response
import json


class Calendar(Resource):
    """
    handles all event creation/deletion
    """

    
    def get(self):
        event_tag = request.args["id"]
        print(event_tag)
        data = db.get_event_availability(event_tag=event_tag)
        print(data)
        return data

    def post(self):
        tag = db.create_new_event()
        return {'clendar_tag':tag}

class ValidateUser(Resource):
    """
    confirms a logged in user is correct user
    """

    @staticmethod
    def get():
        print(request)
        body = request.get_json()
        print(body)

        user_id = body["username"]
        event_id = body["event_id"]
        result = utils.confirm_user(event_id, user_id)
        return result


if __name__ == "__main__":
    import requests

    # resp = requests.get("http://127.0.0.1:5000/validate", json={"username": "user1", "event_id":"qqeV6u8"})
    # print(resp, resp.json())

    resp = requests.get("http://127.0.0.1:5000/event?id=qqeV6u8")
    print(resp, resp.json())
