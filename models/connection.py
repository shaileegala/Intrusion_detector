import pymysql
from envs import DB_HOST, DB_DATABASE, DB_PASSWORD, DB_USER


class Connection(object):

    def __init__(self):
        self.connection = pymysql.connect(user=DB_USER,
                                          password=DB_PASSWORD,
                                          host=DB_HOST,
                                          database=DB_DATABASE,
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cursor = None

    def get_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_cursor(self):
        self.cursor.close()

    def close_connection(self):
        if self.cursor:
            self.close_cursor()
        self.connection.close()
        self.connection = None
