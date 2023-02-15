import requests
import unittest

import json


class CalendarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Tests a post request and sets up for the get test
        """
        url = "http://127.0.0.1:5000/calendar"
        cls.URL = url
        body = {"title": "test", "days": ["monday", "tuesday", "friday"]}
        response = requests.request("POST", url, json=body)
        resp_json_dict = json.loads(response.text)
        cls.EXISTING_CALENDAR_ID = resp_json_dict["id"]
        print(f"Creating example calendar: {cls.EXISTING_CALENDAR_ID}")

    def test_post_calendar_create_calendar(self):
        body = {"title": "test", "days": ["monday", "tuesday", "friday"]}

        response = requests.request("POST", self.URL, json=body)
        resp_json_dict = json.loads(response.text)

        self.assertTrue("id" in resp_json_dict.keys())
        self.assertTrue(len(resp_json_dict["id"]) == len(self.EXISTING_CALENDAR_ID))

    def test_get_calender_exists(self):
        response = requests.request("GET", self.URL + f"/{self.EXISTING_CALENDAR_ID}")

        resp_json_dict = json.loads(response.text)
        self.assertTrue(resp_json_dict["title"] == "test")
        self.assertTrue(
            resp_json_dict["days"] == {"monday": [], "tuesday": [], "friday": []}
        )

    def test_get_calendar_does_not_exist(self):
        self.URL = "http://127.0.0.1:5000/calendar/fake_calendar_id"

        response = requests.request("GET", self.URL + f"/fake_calendar_id")
        self.assertTrue(response.status_code == 404)


if __name__ == "__main__":
    unittest.main()
