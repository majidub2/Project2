from application import app
from flask import request, Response
import random

@app.route("/", methods=["GET"])
def get_numbers():
    numbers = random.randint(1000,9999)
    return Response(str(numbers), mimetype='text/plain')