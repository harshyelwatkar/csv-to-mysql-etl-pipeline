
import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text

load_dotenv()

db_url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME", "sales_etl"),
)

engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE()"))
        print("Connected successfully!")
        print("Database:", result.scalar())
finally:
    engine.dispose()
