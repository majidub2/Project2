from application import db

class Prizes(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    Account_number = db.Column(db.String(10), nullable=false)
    Prize_money = db.Column(db.integer(100), nullable=false)
    