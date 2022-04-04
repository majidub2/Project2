from application import app, db
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application.routes import Prizes

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
    
    def setUp(self):
        sample_result = Prizes(account_number='CBA2000', prize='0')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get("http://letters:5001", text ="CBA")
            m.get("http://numbers:5002", text ="2000")
            data = {"account_number" : 'CBA2000', "prize" : '0'}
            m.post("http://accountnumber:5003", json=data)
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'CBA2000 won 0', response.data)