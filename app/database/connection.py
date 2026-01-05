import os 
import psycopg as pg
from dotenv import load_dotenv

load_dotenv()

user= os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
address = os.getenv("DATABASE_ADDRESS")
port = os.getenv("DATABASE_PORT")
dbname = os.getenv("DATABASE_NAME")

def connect():
    try:
        connection = pg.connect(f"user={user} password={password} host={address} port={port} dbname={dbname}")
        return connection
    
    except Exception as e:
        print(f"error: {e}")