import os

from peewee import SqliteDatabase, PostgresqlDatabase

# sqlite only for local testing
# SQLITE_DATABASE = './data/ShortURL.db'
# mydatabase = SqliteDatabase(SQLITE_DATABASE)

# Connect to a Postgres database.
pg_host = os.getenv('PG_HOST')
pg_port = os.getenv('PG_PORT')
pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')
pg_dbname = os.getenv('PG_DBNAME')

mydatabase = PostgresqlDatabase(pg_dbname, user=pg_user, password=pg_password, host=pg_host, port=pg_port)
