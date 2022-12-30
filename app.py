from flask import Flask, request, Response
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
   
    resp = Response(status=200)
    resp.set_data(json.dumps({"id": tag}))
    return resp


@app.route("/calendar/<id>", methods=["GET"])
def getCalendar(id):
    """
    Returns informations for the given clalendar.
    """
    try:
        data = db.get_event(event_tag=id)
    except:
        return Response(status=404)
    resp = Response(status=200)
    resp.set_data(json.dumps(data))
    return resp


@app.route("/calendar/<id>/", methods=["PUT"])
def putCalendar(id):
    """
    Updates the availability of the given user on the given calendar
    """
    user = escape(request.args["user"])

    resp =  Response(status=200)
    resp.set_data(f"pretending to put in data for {escape(id)} for user {user}  :)")
    return resp

if __name__ == "__main__":
    load_dotenv()
    app.run()
