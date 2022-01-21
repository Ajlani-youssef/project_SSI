from utils.singleton import Singleton
import psycopg2
import config


@Singleton
class DBConnection(object):
    conn = None

    def __init__(self):
        self.conn = psycopg2.connect(
            database=config.database, user=config.user, password=config.bd_password, host=config.host, port=config.port)

    def __str__(self):
        return "connection initialized" if self.conn is None else "connection not initialized"
