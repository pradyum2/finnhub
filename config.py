import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///stocks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY', 'cqeduo1r01qgmug470ugcqeduo1r01qgmug470v0')  # Replace with your actual Finnhub API key
