from os import environ, path
from typing import Any, Collection, Mapping

from pymongo import MongoClient
from pymongo.database import Database

import logging as log
import json


import utils


##################################################################
# USING MOCK DATA FOR NOW SHOULD NOT BE KEPT LONG TERM           #
##################################################################


##################################################################
class MongConn:
    def __init__(self) -> None:
        """Opens a connection to the database and"""
        self.mongo_client = MongoClient(
            environ.get("MONGO_URI"), int(environ.get("MONGO_PORT"))
        )
        self.mongo_client.get_database("noonalu")

    def get_db(self) -> Database[Mapping[str, Any] | Any]:
        """Returns noonalu database"""
        noonalu_db = self.mongo_client.get_database("noonalu")
        return noonalu_db

    def get_collection(self) -> Collection[Mapping[str, Any] | Any]:
        """Returns calendar collection"""
        coll = self.get_db().get_collection("calendars")
        return coll

    def close(self) -> None:
        """Closes database connection"""
        self.mongo_client.close()


def get_event_users(cal_id: str) -> dict:
    """return dict of users for event"""
    return get_calendar(cal_id=cal_id)["users"]


def get_calendar_availability(cal_id: str) -> dict:
    """returns calendar for event"""
    cal = get_calendar(cal_id=cal_id)
    return cal["availability"]


def create_new_calendar():
    """Creates a new event, returns the tag for the calendars"""
    conn = MongConn()
    cal_id = utils.get_new_cal_id()
    calendar = {
        "cal_id": cal_id,
        "availability": {},
        "users": [],
    }
    calendar_collection = conn.get_collection()
    calendar_collection.insert_one(calendar)
    conn.close()
    log.info(calendar)
    return cal_id


def get_calendar(cal_id: str):
    """returns dictionary containing event tied to the data"""
    conn = MongConn()
    coll = conn.get_collection()
    res = coll.find_one({"cal_id": cal_id})
    conn.close()

    if res == None:
        raise KeyError("Event does not exist")

    event = dict(res)
    event.pop("_id")
    return event
