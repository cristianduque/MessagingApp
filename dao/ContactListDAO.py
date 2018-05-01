from  dao.UserDAO import UserDAO
import psycopg2
from config.dbconfig import pg_config

class ContactListDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def allContactLists(self):
        cursor = self.conn.cursor()
        query = "select * from contactlist;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def contactlistofUser(self, uid):
        cursor = self.conn.cursor()
        query = "select contact from contactlist where uid = %s;"
        cursor.execute(query, (uid, ))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result
