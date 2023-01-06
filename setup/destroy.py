from setup import *
import dotenv
import sys


def destroy_database():
    """Destroys all collections in the database"""
    conn = MongConn()
    db = conn.get_db()
    # print(db.list_collection_names())/
    for name in db.list_collection_names():
        db.drop_collection(name)


if __name__ == "__main__":
    print("PREPARING TO DESTROY ALL MONGO COLLECTIONS")
    dotenv.load_dotenv()
    if sys.argv[1] == "-f" or sys.argv[1] == "--force":
            print("DROPPING ALL DATABASE TABLES")
            destroy_database()
    
    print("THIS WILL ONLY DROP ALL DATABASE COLLECTIONS IF RUN WITH -f or --force")
