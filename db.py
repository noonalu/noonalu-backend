from os import environ, path
from pymongo import MongoClient
import logging
import json
from dotenv import load_dotenv

#################################################################
# USING MOCK DATA FOR NOW SHOUL NOT BE KEPT LONG TERM           #
#################################################################

here = path.dirname(__file__)
data = json.loads(open(here + "/mongo.json").read().strip())


def get_mock_data():
    """for use during development"""
    logging.warning("Using Mock Data")
    return data


#################################################################


def open_connection():
    load_dotenv()
    client = MongoClient(environ.get("MONGO_URI"), int(environ.get("MONGO_PORT")))

    return client.noonalu


def get_event_data(event_tag: str) -> dict:
    """returns all data for event"""
    mong_conn = open_connection()
    mong_conn
    return get_all_data()["events"][event_tag]


def get_event_users(event_tag: str) -> dict:
    """return dict of users for event"""
    return get_event_data(event_tag=event_tag)["users"]


def get_event_calendar(event_tag: str) -> dict:
    """returns calendar for event"""
    return get_event_data(event_tag=event_tag)


def get_all_data():
    """This feels like a bad thing to use"""
    return get_mock_data()


if __name__ == "__main__":
    # print(get_event_data("qqeV6u8"))
    print(get_event_users("qqeV6u8"))
    client = MongoClient("localhost", 27107)
    db = client.test
    print(db)
