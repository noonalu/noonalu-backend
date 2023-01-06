import secrets
import db


def get_new_cal_id():
    return secrets.token_urlsafe(7)


def get_events():
    pass


def confirm_user(event_tag: int, username: str, password: str = None):
    return db.get_event_users(cal_id=event_tag)[username]


if __name__ == "__main__":
    print(confirm_user("qqeV6u8","user1", None))
