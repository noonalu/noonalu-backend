from os import environ
from typing import Any, Collection, Mapping

from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

import logging as log


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


def create_new_calendar(name: str, days: str):
    """Creates a new event, returns the id for the calendar."""

    week = {}
    for day in days:
        week[day] = []
    calendar = {"title": name, "days": week}

    conn = MongConn()
    calendar_collection = conn.get_collection()
    new_cal = calendar_collection.insert_one(calendar)
    conn.close()

    cal_id = str(new_cal.inserted_id)
    log.info(f"Created Calendar: %s", cal_id)
    return cal_id


def get_calendar(cal_id: str):
    """Returns calendar information."""
    conn = MongConn()
    coll = conn.get_collection()
    res = coll.find_one({"_id": ObjectId(cal_id)})
    conn.close()

    if res == None:
        raise KeyError("Event does not exist")

    event = dict(res)
    event.pop("_id")
    log.info(f"Retrieving Calendar %s", cal_id)
    return event

