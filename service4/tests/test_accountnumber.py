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

        # with patch('random.randrange') as random:
        #     random.return_value = "1000"
        #     data = {"letters" : 'ABC', "numbers" : '1000'}
        #     response = self.client.post(url_for('prize'), json=data)
        #     test_json = b'{"account_number": "AB14CDG", "prize": "blue"}'
        
        # data = {"letters" : 'ABCDE', "numbers" : '4'}
        # response = self.client.post(url_for('get_numberplate'), json=data)
        # json_response = response.data
        # test_json = b'{"account_number": "AB04CDE", "prize": "yellow"}'
        # assert json_response == test_json