import secrets
import db


def get_new_event_tag():
    return secrets.token_urlsafe(5)


def get_events():
    pass


def confirm_user(event_tag: int, username: str, password: str = None):
    return db.get_event_users(event_tag=event_tag)[username]


if __name__ == "__main__":
    print(confirm_user("qqeV6u8","user1", None))
