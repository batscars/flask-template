from app.webapp import app
import unittest
import json


class WebAppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.debug = True
        self.app = app.test_client()

    def test_func01(self):
        resp = self.app.post("/func01/query", data=dict(a=1, b=2))
        print(resp.data)

        resp_json = json.loads(resp.data)
        self.assertEqual(resp_json["code"], 200)

