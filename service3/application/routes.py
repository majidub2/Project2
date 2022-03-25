from application import app
from flask import request, Response
import random


def get_numbers():
    numbers = random.randint(1000,9999)
    return Response(str(numbers), mimetype='text/plain')