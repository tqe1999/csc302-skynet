import os
import quandl
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.reflection import Inspector
import sys
import logging
import time

# init logger
# formatter = logging.Formatter("%(created)f:%(levelname)s:%(name)s:%(module)s:%(message)s")
formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(name)s:%(module)s:%(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("log.txt", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# get environment variables
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

# authenticate quandl
try:
    QUANDL_API_KEY = os.environ.get("QUANDL_API_KEY")
    quandl.ApiConfig.api_key = QUANDL_API_KEY
except Exception as e:
    logger.warning("API key not specified, rate limit reduced")

logger.info(f"Connecting to database {POSTGRES_HOST} on port {POSTGRES_PORT}")

# database connection
conn_str = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/postgres"
)
db = create_engine(conn_str)
inspector = Inspector.from_engine(db)

if "stocks" in inspector.get_table_names():
    logger.info("already initialized")
    sys.exit(0)

metadata = MetaData()

stocks_file = open("stocks.txt", "r")
stocks = stocks_file.readlines()

for stock in stocks:
    stock = stock.strip()
    ticker = f"WIKI/{stock}"
    logger.info(f"loading stock {ticker}")
    backoff_delay = 1
    
    while True:
        try:
            data = quandl.get(
                ticker, collapse='annual'
            )
            data["stock"] = stock
            if backoff_delay > 1:
                backoff_delay -= 1
            break
        except Exception as e:
            logger.warning(f"loading stock {ticker} failed with exception {e}")
            logger.warning(f"backing off for {backoff_delay} seconds")
            time.sleep(backoff_delay)
            backoff_delay *= 2
            continue

    data.to_sql("stocks", con=db, index=True, if_exists="append")

