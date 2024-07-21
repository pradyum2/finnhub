import requests
from flask import Flask, jsonify
from datetime import date
from models import db, ShareValue
from config import Config
from __init__ import create_app

app = create_app()

def get_share_value(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={app.config['FINNHUB_API_KEY']}"
    response = requests.get(url)
    data = response.json()
    return data

def store_share_value(symbol, current_price, previous_close):
    share_value = ShareValue(
        symbol=symbol,
        current_price=current_price,
        previous_close=previous_close,
        date=date.today()
    )
    db.session.add(share_value)
    db.session.commit()

@app.route('/fetch', methods=['GET'])
def fetch_share_values():
    symbols = ['AAPL', 'MSFT']
    for symbol in symbols:
        data = get_share_value(symbol)
        store_share_value(symbol, data['c'], data['pc'])
    return jsonify({"message": "Share values fetched and stored successfully"}), 200

@app.route('/profit-loss', methods=['GET'])
def get_profit_loss():
    shares = ShareValue.query.filter_by(date=date.today()).all()
    profit_loss = {}
    for share in shares:
        quantity = 10
        profit_loss[share.symbol] = (share.current_price - share.previous_close) * quantity
    return jsonify(profit_loss), 200

if __name__ == '__main__':
    app.run(debug=True)
