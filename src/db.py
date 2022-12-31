from os import environ, path
import sys
from typing import Any, Mapping

from pymongo import MongoClient
import logging as log
import json

from pymongo.database import Database

import utils


##################################################################
# USING MOCK DATA FOR NOW SHOULD NOT BE KEPT LONG TERM           #
##################################################################


def get_mock_data():
    """for use during development"""
    here = path.dirname(__file__)
    data = json.loads(open(here + "/mongo.json").read().strip())
    log.warning("Using Mock Data")
    return data


##################################################################
class MongConn:
    def __init__(self) -> None:
        """Opens a connection to the database and"""
        self.mongo_client = MongoClient(
            environ.get("MONGO_URI"), int(environ.get("MONGO_PORT"))
        )

    def get_db(self) -> Database[Mapping[str, Any] | Any]:
        """Returns noonalu database"""
        noonalu_db = self.mongo_client.get_database("noonalu")
        return noonalu_db

    def close(self) -> None:
        """Closes database connection"""
        self.mongo_client.close()


def get_event_users(event_tag: str) -> dict:
    """return dict of users for event"""
    return get_event(event_tag=event_tag)["users"]


def get_event_availability(event_tag: str) -> dict:
    """returns calendar for event"""
    event = get_event(event_tag=event_tag)
    return event["availability"]


def _read_all_events() -> list:
    """Returns a list of all events"""
    conn = MongConn()
    noon_data = conn.get_db()
    coll = noon_data.get_collection("events")
    res = coll.find(sort=[("tag", 1)])
    conn.close()
    return list(res)


def create_new_event():
    """Creates a new event, returns the tag for the event"""
    conn = MongConn()
    noon_data = conn.get_db()
    tag = utils.get_new_event_tag()
    event = {
        "tag": tag,
        "availability": {},
        "users": [],
    }
    event_collection = noon_data.get_collection("events")
    event_collection.insert_one(event)
    conn.close()
    log.info(event)
    return tag


def get_event(event_tag: str):
    """returns dictionary containing event tied to the data"""
    conn = MongConn()
    noon_data = conn.get_db()

    coll = noon_data.get_collection("events")
    res = coll.find_one({"tag": event_tag})
    conn.close()

    if res == None:
        raise KeyError("Event does not exist")

    event = dict(res)
    event.pop("_id")
    return event


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG, stream=sys.stdout)
    tag = create_new_event()
    assert get_event(event_tag=tag)["tag"] == tag
    assert get_event_availability(tag) == {}
    assert get_event_users(tag) == []

    import pprint

    pprint.pp(_read_all_events())
    # client = MongoClient("localhost", 27017)
    # pprint.pp(get_event_data("qqeV6u8"))

    # client.server_info()
    # print(client.server_info())
