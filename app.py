import os
from pathlib import Path
from dotenv import load_dotenv
import pymysql

load_dotenv(Path.cwd() / ".env")

connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT", "3306")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM transactions")
    print("Total transactions:", cursor.fetchone()[0])

connection.close()