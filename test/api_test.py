import requests
import unittest
import json


class CalendarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Slightly redundant to since another calendar is added in the tests,
        however we need a guaranteed existing calendar for later tests
        """
        url = "http://127.0.0.1:5000/calendar"
        response = requests.request("POST", url)
        resp_json_dict = json.loads(response.text)
        cls.EXISTING_CALENDAR = resp_json_dict["cal_id"]
        print(f"Creating example calendar: {cls.EXISTING_CALENDAR}")

    def test_post_calendar_create_calendar(self):
        url = "http://127.0.0.1:5000/calendar"

        response = requests.request("POST", url)
        resp_json_dict = json.loads(response.text)

        assert "cal_id" in resp_json_dict.keys()
        assert len(resp_json_dict["cal_id"]) == len("LBKFoaFIyA")

    def test_put_calendar_update_user_data(self):

        url = "http://127.0.0.1:5000/calendar/aHX3j8x1Ww/?user=peter"

        response = requests.request("PUT", url)

        assert (
            response.text
            == "pretending to put in data for aHX3j8x1Ww for user peter  :)"
        )

    def test_get_calender_exists(self):

        url = f"http://127.0.0.1:5000/calendar/{self.EXISTING_CALENDAR}"
        response = requests.request("GET", url)

        resp_json_dict = json.loads(response.text)

        assert resp_json_dict["cal_id"] == str(self.EXISTING_CALENDAR)

    def test_get_calendar_does_not_exist(self):

        url = "http://127.0.0.1:5000/calendar/fake_calendar_id"

        response = requests.request("GET", url)

        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
