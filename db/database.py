import psycopg2
from config.settings import DB_SETTINGS

def get_db_connection():
    return psycopg2.connect(**DB_SETTINGS)
