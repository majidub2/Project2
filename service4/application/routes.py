from application import app
from flask import request, Response
from random import randrange
import json

# letters = ["ABC", "BCA", "CAB", "ACB", "BAC", "CBA"]

@app.route("/", methods=["POST"])
def prize():
    data = request.json
    letters = data["letters"]
    numbers = int(data["numbers"])

    if (numbers % 2 == 0):
        Prize = "NO PRIZE, SORRY"
    elif letters == "ABC":
        Prize = "£100"
    elif letters == "BCA":
        Prize = "£80"
    elif letters == "CAB":
        Prize = "£60"
    elif letters == "ACB":
        Prize = "£40"
    elif letters == "BAC":
        Prize = "£20"
    elif letters == "CBA":
        Prize = "£5"
     
a
    accountnumber = letters + numbers
    accountnumber_and_prize = {"accoutnumber" : accoutnumber, "prize" : prize}
    return Response(json(accountnumber_and_prize))
