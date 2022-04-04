from application import app
from flask import request, Response
from random import randrange
import json

# letters = ['ABC', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA']

@app.route('/', methods=['POST'])
def prize():
    data = request.json
    letters = data['letters']
    numbers = int(data['numbers'])

    if (numbers % 2 == 0):
        prize = '0'
    elif letters == 'ABC':
        prize = '100'
    elif letters == 'BCA':
        prize = '80'
    elif letters == 'CAB':
        prize = '60'
    elif letters == 'ACB':
        prize = '40'
    elif letters == 'BAC':
        prize = '20'
    elif letters == 'CBA':
        prize = '5'
     

    accountnumber = letters + str(numbers)
    accountnumber_and_prize = {'account_number' : accountnumber, 'prize' : prize}
    return Response(json.dumps(accountnumber_and_prize))
