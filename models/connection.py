import pymysql


class Connection(object):
    HOST = ""  # change before deploying
    USER = ""
    PASSWORD = ""
    DATABASE = ""

    def __init__(self):
        self.connection = pymysql.connect(user=self.USER,
                                          password=self.PASSWORD,
                                          host=self.HOST,
                                          database=self.DATABASE,
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
