from dao.UserDAO import UserDAO
import psycopg2
from config.dbconfig import pg_config

class ChatDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def getAllChats(self):
        cursor = self.conn.cursor()
        query = "select * from chat"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getOwnerOfChat(self, cid):
        cursor = self.conn.cursor()
        query = 'select firstname, lastname, username, phone, email from "user" as U inner join chat as C on U.uid = C.owner where cid = %s'
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getAllUsersInChat(self, cid):
        cursor = self.conn.cursor()
        query ="select firstname, lastname, username, phone, email from participateschat as C inner join 'user' as U on C.uid = U.uid where C.cid = 1;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result





