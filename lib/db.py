import logging
import os
import json
import psycopg2
from psycopg2 import OperationalError, Error


class DB:
    connection = None
    cursor = None
    environment = None

    def __init__(self, param):
        self.environment = param['environment']
        self.connect()

    def connect(self):
        try:
            data = None
            if os.path.exists('/builds/example/path.tmp/CONFIGJSON'):
                filename = '/builds/example/path.tmp/CONFIGJSON'
                data = json.load(open(filename))
            else:
                filename = f"{os.getcwd()}/config.json"
                data = json.load(open(filename))

            db_user = data[0]['environments'][self.environment]['user']
            db_password = data[0]['environments'][self.environment]['password']
            db_host = data[0]['environments'][self.environment]['host']
            db_name = data[0]['environments'][self.environment]['database']
            db_port = data[0]['environments'][self.environment]['port']
            database_uri = f"dbname='{db_name}' user='{db_user}' host='{db_host}' port='{db_port}' password='{db_password}'"
            logging.info(f"Connecting to {db_name}")

            self.connection = psycopg2.connect(database_uri, connect_timeout=10)
            self.cursor = self.connection.cursor()
            logging.info(f"Connected to database: {db_name}")
            return True

        except (FileNotFoundError, OperationalError) as e:
            logging.error(f"\nThe error '{e}' occurred while connecting database")
            return False
