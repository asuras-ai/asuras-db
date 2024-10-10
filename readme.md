# Asuras TradingDB

This project sets up a Docker environment with a PostgreSQL database to store OHLCV (Open, High, Low, Close, Volume) data from different sources like yfinance and ccxt. It includes a GUI to select trading pairs, timeframes, and exchanges for data download, and to view the currently stored data.

## Project Structure

```
Asuras TradingDB/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── data_fetcher.py
│   └── gui.py
└── README.md
```

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Asuras-TradingDB.git
   cd Asuras-TradingDB
   ```

2. Build and run the Docker containers:
   ```
   docker-compose up -d
   ```

3. Access the GUI by opening a web browser and navigating to `http://localhost:8050`.

## Usage

1. Use the GUI to select trading pairs, timeframes, and exchanges.
2. Click the "Download Data" button to fetch and store the selected data.
3. View the currently stored data in the table on the GUI.