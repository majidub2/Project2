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
   
    def test_get_letters(self):
        with patch('random.choice') as r:
            r.return_value = "ABC"
            response = self.client.get(url_for('get_letters'))
            self.assert200(response)
            self.assertIn(b'ABC', response.data)
            



