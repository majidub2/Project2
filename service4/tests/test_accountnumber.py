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

    def test_get_accountnumber(self):
        data = {"letters" : 'ABC', "numbers" : '1001'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "ABC1001", "prize": "100"}'
        assert json_response == test_json

    def test_get_accountnumber(self):
        data = {"letters" : 'BCA', "numbers" : '1353'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "BCA1353", "prize": "80"}'
        assert json_response == test_json

    
    def test_get_accountnumber(self):
        data = {"letters" : 'CAB', "numbers" : '1003'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "CAB1003", "prize": "60"}'
        assert json_response == test_json

    def test_get_accountnumber(self):
        data = {"letters" : 'ACB', "numbers" : '1005'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "ACB1005", "prize": "40"}'
        assert json_response == test_json

    def test_get_accountnumber(self):
        data = {"letters" : 'BAC', "numbers" : '1007'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "BAC1007", "prize": "40"}'
        assert json_response == test_json

    def test_get_accountnumber(self):
        data = {"letters" : 'BAC', "numbers" : '1011'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "BAC1011", "prize": "20"}'
        assert json_response == test_json

    def test_get_accountnumber(self):
        data = {"letters" : 'CBA', "numbers" : '1013'}
        response = self.client.post(url_for('prize'), json=data)
        json_response = response.data
        test_json = b'{"account_number": "CBA1013", "prize": "5"}'
        assert json_response == test_json

    

        


# python3 -m pytest -p no:warnings --cov=application     
