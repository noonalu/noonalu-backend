from flask import Flask, request
from dotenv import load_dotenv
from markupsafe import escape
import db
import json

app = Flask(__name__)


@app.route("/calendar", methods=["POST"])
def postCaledar():
    """
    Creates a new calendar
    """
    tag = db.create_new_event()
    return {"id": tag}


@app.route("/calendar/<id>", methods=["GET"])
def getCalendar(id):
    """
    Returns informations for the given clalendar.
    """
    # print(id)
    data = db.get_event(event_tag=id)
    return json.dumps(data)
    # print(data)
    # return f"here's the data for {escape(id)}. Soon it will actually be something!"


@app.route("/calendar/<id>/", methods=["PUT"])
def putCalendar(id):
    """
    Updates the availability of the given user on the given calendar
    """
    user = escape(request.args["user"])

    return f"pretending to put in data for {escape(id)} for user {user}  :)"


if __name__ == "__main__":
    load_dotenv()
    app.run()
