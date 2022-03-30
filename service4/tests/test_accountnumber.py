from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import json
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
   
    def test_get_accountnumber(self):
        data = {"letters" : 'ABC', "numbers" : '1000'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "ABC1000", "prize": "0"}'
        assert json_response == test_json

     