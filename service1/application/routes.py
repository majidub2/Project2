from application import app, db
import requests
from flask import render_template
from sqlalchemy import desc
import json 

@app.route('/', methods=['GET', 'POST'])
def index():
    
    letters_response = requests.get("http://letters:5001")
    numbers_response = requests.get("http://numbers:5002")

    data = {"letters" : letters_response.text, "numbers" : numbers_response.text}
    accountnumber_response = requests.post("http://accountnumber:5003", json = data)
    json_accountnumber_response =  accountnumber_response.json()
    
 

    

    
