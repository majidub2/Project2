from application import app
from flask import request, Response
import random

letters = ["ABC", "BCA", "CAB", "ACB", "BAC", "CBA"]

def get_letters():
    random_letters = random.choice(letters)  
    return Response(str(random_letters), mimetype='text/plain')
