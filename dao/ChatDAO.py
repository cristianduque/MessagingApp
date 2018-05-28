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

    def addNewChat(self, chatname, uid):
        cursor = self.conn.cursor()
        query = 'insert into chat(chatname, owner) values(%s, %s) returning cid;'
        cursor.execute(query, (chatname, uid))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result

    def addUsertoChat(self, cid, uid):
        cursor = self.conn.cursor()
        query = 'insert into participateschat values(%s,%s);'
        cursor.execute(query, (uid, cid))
        self.conn.commit()
        return "Done"

    def getChat(self, cid):
        cursor = self.conn.cursor()
        query = 'select cid, chatname, username from chat as C inner join "user" as U on U.uid=C.owner where cid = %s;'
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getOwnerOfChat(self, cid):
        cursor = self.conn.cursor()
        query = 'select uid, firstname, lastname, phone, email, username from "user" as U inner join chat as C on U.uid = C.owner where cid = %s;'
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getAllUsersInChat(self, cid):
        cursor = self.conn.cursor()
        query ='select U.uid, firstname, lastname, phone, email, username from participateschat as C inner join "user" as U on C.uid = U.uid where C.cid = %s;'
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result





