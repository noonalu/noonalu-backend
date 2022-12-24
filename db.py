from os import environ, path
from typing import Any, Mapping

from pymongo import MongoClient
import logging as log
import json
from dotenv import load_dotenv
import sys

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


def open_connection() -> Database[Mapping[str, Any] | Any]:
    load_dotenv()
    mongo_client = MongoClient(environ.get("MONGO_URI"), int(environ.get("MONGO_PORT")))
    return mongo_client.get_database("noonalu")


def get_event_users(event_tag: str) -> dict:
    """return dict of users for event"""
    return get_event_data(event_tag=event_tag)["users"]


def get_event_availability(event_tag: str) -> dict:
    """returns calendar for event"""
    return get_event_data(event_tag=event_tag)["availability"]



def _list_all_events():
    conn = open_connection()
    coll = conn.get_collection("events")
    coll.create_index('tag')
    return list(coll.find())
    


def create_new_event():
    conn = open_connection()
    tag = utils.get_new_event_tag()
    event = {
        "tag": tag,
        "availability": {},
        "users": [],
    }
    coll = conn.get_collection("events")
    coll.insert_one(event)
    log.info(event)
    return tag


def get_event_data(event_tag):
    conn = open_connection()
    coll = conn.get_collection("events")
    res = coll.find_one({"tag": event_tag})
    return dict(res)


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG, stream=sys.stdout)
    tag = create_new_event()
    assert get_event_data(event_tag=tag)["tag"] == tag
    assert get_event_availability(tag) == {}
    assert get_event_users(tag) == []

    import pprint 
    pprint.pp(_list_all_events())
    # client = MongoClient("localhost", 27017)
    # pprint.pp(get_event_data("qqeV6u8"))

    # client.server_info()
    # print(client.server_info())
