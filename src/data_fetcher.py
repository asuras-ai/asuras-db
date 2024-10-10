import yfinance as yf
import ccxt
from database import SessionLocal, OHLCV

def fetch_data(symbol, exchange, timeframe):
    if exchange == 'yfinance':
        data = fetch_yfinance(symbol, timeframe)
    else:
        data = fetch_ccxt(symbol, exchange, timeframe)
    
    save_to_db(data, symbol, exchange)

def fetch_yfinance(symbol, timeframe):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="max", interval=timeframe)
    return data

def fetch_ccxt(symbol, exchange, timeframe):
    exchange_class = getattr(ccxt, exchange)
    exchange_instance = exchange_class()
    ohlcv = exchange_instance.fetch_ohlcv(symbol, timeframe)
    return ohlcv

def save_to_db(data, symbol, exchange):
    session = SessionLocal()
    for index, row in data.iterrows():
        ohlcv = OHLCV(
            symbol=symbol,
            exchange=exchange,
            timestamp=index,
            open=row['Open'],
            high=row['High'],
            low=row['Low'],
            close=row['Close'],
            volume=row['Volume']
        )
        session.add(ohlcv)
    session.commit()
    session.close()