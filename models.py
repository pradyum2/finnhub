from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ShareValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_close = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
