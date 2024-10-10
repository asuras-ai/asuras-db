from database import init_db, create_tables
from data_fetcher import fetch_data
from gui import run_dashboard

def main():
    init_db()
    create_tables()
    run_dashboard()

if __name__ == "__main__":
    main()