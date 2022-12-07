import db as db
import utils as duck
from flask_restful import Resource, request
import json


class Event(Resource):
    """
    handles all event stuff
    """

    def get(self):
        event_tag = request.args["id"]
        data = db.get_event_calendar(event_tag=event_tag)
        return json.dumps(data)

    def post(self):
        duck.get_new_event_tag()
        

class ValidateUser(Resource):
    """
    confirms a logged in user is correct user
    """

    def get(self):
        print(request)
        body = request.get_json()
        print(body)

        usern = body["username"]
        event_id = body["event_id"]
        result = duck.confirm_user(event_id, usern)
        return result


if __name__ == "__main__":

    import requests

    # resp = requests.get("http://127.0.0.1:5000/validate", json={"username": "user1", "event_id":"qqeV6u8"})
    # print(resp, resp.json())

    resp = requests.get("http://127.0.0.1:5000/event?id=qqeV6u8")
    print(resp, resp.json())