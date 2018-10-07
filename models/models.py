
# Validate username password
# Import connection and cursor object
from models.connection import Connection


# User Object
class User(object):

    def __init__(self, id, username, fname, lname):
        self.id = id
        self.username = username
        self.fname = fname
        self.lname = lname

    @classmethod
    # Insert into User Table
    def insert_into_user(cls, username, fname, lname):
        conn = Connection()
        query = "INSERT INTO User (FName, LName, Username) VALUES('{fname}', '{lname}', '{username}')".format(fname=fname, lname=lname, username=username)
        cur = conn.get_cursor()
        cur.execute(query)
        conn.connection.commit()
        conn.close_connection()

    @classmethod
    # Fetch from User Table
    def fetch_by_username(cls, username):
        conn = Connection()
        query = "SELECT * FROM User WHERE Username = '{uname}'".format(uname=username)
        cur = conn.get_cursor()
        cur.execute(query)
        user_row_dict = cur.fetchone()

        conn.close_connection()

        if user_row_dict:
            return User(id=user_row_dict['ID'], username=user_row_dict['Username'], fname=user_row_dict['FName'],
                        lname=user_row_dict['LName'])


class Password(object):

    def __init__(self, id, userid):
        self.id = id
        self.userid = userid

    @classmethod
    def insert_into_passwords(cls, password, userid):
        conn = Connection()

        # Update for all passwords of userid iscurrent=False
        query = "UPDATE Passwords SET IsCurrent = False WHERE UserID = {userid}".format(userid=userid)

        cur = conn.get_cursor()
        cur.execute(query)
        conn.connection.commit()

        query = "INSERT INTO Passwords (IsCurrent, Password, UserID) VALUES({iscurrent}, '{password}', {userid})".format(
            iscurrent=True, password=password, userid=userid)
        cur.execute(query)
        conn.connection.commit()
        conn.close_connection()

    @classmethod
    def fetch_by_userid(cls, userid, password):
        conn = Connection()
        query = "SELECT * FROM Passwords WHERE Userid = {userid} AND Password = '{password}'".format(
            userid=userid, password=password)
        cur = conn.get_cursor()
        cur.execute(query)

        passwords_row_dict = cur.fetchone()

        conn.close_connection()

        if passwords_row_dict:
            return Password(id=passwords_row_dict['ID'], userid=passwords_row_dict['UserID'])


class PasswordAnalytics(object):

    def __init__(self, id, aggregate, count, passwordid):
        self.id = id
        self.aggregate = aggregate
        self.count = count
        self.passwordid = passwordid

    @classmethod
    def insert_into_password_analytics(cls, aggregate, count, password_id):
        conn = Connection()
        query = "INSERT INTO PasswordAnalytics (Aggregate, Count, PasswordID) VALUES ({aggregate}, {count}, " \
                "{password_id})".format(aggregate=aggregate, count=count, password_id=password_id)
        cur = conn.get_cursor()
        cur.execute(query)
        conn.connection.commit()
        conn.close_connection()

    @classmethod
    def fetch_by_password_id(cls, password_id):
        conn = Connection()
        query = "SELECT * FROM PasswordAnalytics WHERE PasswordID = {password_id}".format(password_id=password_id)
        cur = conn.get_cursor()
        cur.execute(query)

        passwordanalytics_row_dict = cur.fetchone()

        conn.close_connection()

        if passwordanalytics_row_dict:
            return PasswordAnalytics(id=passwordanalytics_row_dict['ID'],
                                     aggregate=passwordanalytics_row_dict['Aggregate'],
                                     count=passwordanalytics_row_dict['Count'],
                                     passwordid=passwordanalytics_row_dict['PasswordID'])


# Get mean

# Update Total and Count