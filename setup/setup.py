from os import environ
import pprint

from typing import Any, Collection, Mapping

from pymongo import MongoClient, errors
from pymongo.database import Database

import dotenv
import pprint

DATABASE_NAME = "noonalu-api"


class MongConn:
    def __init__(self) -> None:
        """Opens a connection to the database and"""
        if (environ.get("MONGO_URL") != None):
            self.mongo_client = MongoClient(environ.get("MONGO_URL"))
        elif (environ.get("MONGO_URI") != None and environ.get("MONGO_PORT") != None):
            self.mongo_client = MongoClient(
                environ.get("MONGO_URI"), int(environ.get("MONGO_PORT"))
            )
        else:
            print(
                "Error: Missing MONGO_URL or MONGO_URI and MONGO_PORT environment variables")
            exit(1)

        self.mongo_client.get_database(DATABASE_NAME)

    def get_db(self) -> Database[Mapping[str, Any] | Any]:
        """Returns noonalu database"""
        noonalu_db = self.mongo_client.get_database(DATABASE_NAME)
        return noonalu_db

    def get_collection(self) -> Collection[Mapping[str, Any] | Any]:
        """Returns calendar collection"""
        coll = self.get_db().get_collection("calendars")
        return coll

    def close(self) -> None:
        """Closes database connection"""
        self.mongo_client.close()


def setup_database() -> None:
    """Creates the calendar collection in the database"""
    conn = MongConn()
    db = conn.get_db()
    db.create_collection("calendar")


def read_all_calendars() -> list:
    """Returns a list of all calendars"""
    conn = MongConn()
    noon_data = conn.get_db()
    coll = noon_data.get_collection("calendars")
    res = coll.find(sort=[("_id", 1)])
    x = list(res)
    conn.close()
    return x


if __name__ == "__main__":
    pprint.pp("Setting up database")

    dotenv.load_dotenv()

    try:
        # SHOULD FAIL IF RUN MORE THAN ONCE ON THE SAME MongoDB Instance
        setup_database()
    except (errors.CollectionInvalid):
        pprint.pp("Collection already instantiated")
    pprint.pp("List of all calendars in database: ")
    pprint.pp(read_all_calendars())
