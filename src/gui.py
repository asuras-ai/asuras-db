import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
from sqlalchemy import select
from database import SessionLocal, OHLCV
from data_fetcher import fetch_data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Asuras TradingDB"),
    
    dcc.Input(id="symbol-input", type="text", placeholder="Symbol (e.g., BTC/USD)"),
    dcc.Dropdown(id="exchange-dropdown", options=[
        {'label': 'yfinance', 'value': 'yfinance'},
        {'label': 'binance', 'value': 'binance'},
        {'label': 'coinbase', 'value': 'coinbase'},
    ], placeholder="Select Exchange"),
    dcc.Dropdown(id="timeframe-dropdown", options=[
        {'label': '1 minute', 'value': '1m'},
        {'label': '1 hour', 'value': '1h'},
        {'label': '1 day', 'value': '1d'},
    ], placeholder="Select Timeframe"),
    
    html.Button("Download Data", id="download-button"),
    
    dash_table.DataTable(id="data-table")
])

@app.callback(
    Output("data-table", "data"),
    Input("download-button", "n_clicks"),
    State("symbol-input", "value"),
    State("exchange-dropdown", "value"),
    State("timeframe-dropdown", "value")
)
def update_data(n_clicks, symbol, exchange, timeframe):
    if n_clicks is None:
        return []
    
    fetch_data(symbol, exchange, timeframe)
    
    session = SessionLocal()
    result = session.execute(select(OHLCV).where(OHLCV.symbol == symbol, OHLCV.exchange == exchange))
    data = [row._asdict() for row in result]
    session.close()
    
    return data

def run_dashboard():
    app.run_server(debug=True, host='0.0.0.0', port=8050)