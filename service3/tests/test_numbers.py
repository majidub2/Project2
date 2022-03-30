from application import app
from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
   
    def test_get_numbers(self):
        with patch('random.randint') as r:
            r.return_value = '1006'
            response = self.client.get(url_for('get_numbers'))
            self.assert200(response)
            self.assertIn(b'1006', response.data)
            
            



