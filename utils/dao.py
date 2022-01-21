import random

from passlib.hash import sha512_crypt

from utils.dbconnection import DBConnection
from utils.person import Person


class Dao:
    db_conn: DBConnection = None

    def __init__(self):
        self.db_conn = DBConnection.Instance()

    def add_user(self, first_name: str, last_name: str, email: str, password: str):
        if self.search_user_by_email(email=email) is None:
            insert_user_query = "INSERT INTO persons (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, sha512_crypt.hash(password))
            cursor = self.db_conn.conn.cursor()
            cursor.execute(insert_user_query, values)
            self.db_conn.conn.commit()

    def search_user_by_email(self, email: str):
        get_user_by_email_query = "SELECT * FROM persons where email = %s"
        user_email = (email,)
        cursor = self.db_conn.conn.cursor()
        cursor.execute(get_user_by_email_query, user_email)
        return cursor.fetchone()

    def login(self, email: str, password: str):
        result = self.search_user_by_email(email=email)
        if result is None:
            return False
        person = Person(query_result=result)
        pass_verification = sha512_crypt.verify(password, person.password)
        return pass_verification
