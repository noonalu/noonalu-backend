from flask import Flask, request, Response
from dotenv import load_dotenv
import logging
import db
import json

app = Flask(__name__)


@app.route("/calendar", methods=["POST"])
def post_caledar():
    """
    Creates a new calendar
    """

    body = request.get_json()

    name = body["title"]
    days = body["days"]

    cal_id = db.create_new_calendar(name, days)

    resp = Response(status=200)
    resp.set_data(json.dumps({"id": cal_id}))
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


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.DEBUG)
    app.run()
