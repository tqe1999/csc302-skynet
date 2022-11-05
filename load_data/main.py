import os
import quandl
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector
import sys

# get environment variables
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_USER = "postgres"
POSTGRES_HOST = "db"
POSTGRES_PORT = "5432"

# database connection
conn_str = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/postgres"
)
db = create_engine(conn_str)
inspector = Inspector.from_engine(db)

if "stocks" in inspector.get_table_names():
    sys.exit("already initialized")

metadata = MetaData()

stocks_file = open("stocks.txt", "r")
stocks = stocks_file.readlines()

for stock in stocks:
    stock = stock.strip()
    ticker = f"WIKI/{stock}"
    print(ticker)
    
    try:
        data = quandl.get(
            ticker, collapse='annual'
        )
        data["stock"] = stock
    except:
        print(f"loading stock {ticker} failed")
        continue

    data.to_sql("stocks", con=db, index=True, if_exists="append")

