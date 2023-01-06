from flask import Flask, request, Response
from dotenv import load_dotenv
from markupsafe import escape
import db
import json

app = Flask(__name__)


@app.route("/calendar", methods=["POST"])
def post_caledar():
    """
    Creates a new calendar
    """
    cal_id = db.create_new_calendar()

    resp = Response(status=200)
    resp.set_data(json.dumps({"cal_id": cal_id}))
    return resp


@app.route("/calendar/<cal_id>", methods=["GET"])
def get_calendar(cal_id):
    """
    Returns informations for the given clalendar.
    """
    try:
        data = db.get_calendar(cal_id=cal_id)
    except:
        return Response(status=404)
    
    resp = Response(status=200)
    resp.set_data(json.dumps(data))
    return resp


@app.route("/calendar/<cal_id>/", methods=["PUT"])
def put_calendar(cal_id):
    """
    Updates the availability of the given user on the given calendar
    """
    user = escape(request.args["user"])

    resp = Response(status=200)
    resp.set_data(f"pretending to put in data for {escape(cal_id)} for user {user}  :)")
    return resp


if __name__ == "__main__":
    load_dotenv()
    app.run()
