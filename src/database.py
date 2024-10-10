from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://asuras:asuras_password@db/tradingdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class OHLCV(Base):
    __tablename__ = "ohlcv"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    exchange = Column(String, index=True)
    timestamp = Column(DateTime, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

def init_db():
    Base.metadata.create_all(bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)