from application import app, db
from flask import render_template
import requests
from sqlalchemy import desc
import json

class Prizes(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    account_number = db.Column(db.String(10))
    prize = db.Column(db.String(10))


@app.route('/', methods=['GET', 'POST'])
def index():
    
    letters_response = requests.get("http://letters:5001")
    numbers_response = requests.get("http://numbers:5002")

    data = {"letters" : letters_response.text, "numbers" : numbers_response.text}
    accountnumber_response = requests.post("http://accountnumber:5003", json = data)
    json_accountnumber_response =  accountnumber_response.json()

    
    newentry = Prizes(account_number=accountnumber_response.json()["account_number"], prize=accountnumber_response.json()['prize'])
    db.session.add(newentry)
    db.session.commit()
    all_entries = Prizes.query.order_by(desc("pk")).limit(5).all()

    return render_template("index.html", account_number = json_accountnumber_response["account_number"], prize = json_accountnumber_response["prize"], all_entries = all_entries)
    

    
 

    

    
