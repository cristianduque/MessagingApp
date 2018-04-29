from dao.MessageDAO import MessageDAO
import psycopg2
from config.dbconfig import pg_config

class UserDAO:
    def __init__(self):
        U1 = [123, 'Cristian', 'Duque', 7872015817, 'cduque@upr.edu']
        U2 = [456, 'Kristalys', 'Ruiz', 7874292951, 'kruiz@upr.edu']
        U3 = [78, 'Gladymar', 'Oneill', 7876624695, 'goneill@upr.edu']
        U4 = [910, 'Javier', 'Correa', 7878901234, 'j.correa@upr.edu']

        self.messages = MessageDAO().allMessages()

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def getNumberMessagesByUserId(self, uid):
        a = 0
        for m in self.messages:
            if m[5] == uid:
                a += 1
        return a

    def getMessagesByUserId(self, uid):
        a = []
        for m in self.messages:
            if m[5] == uid:
                a.append(m)
        return a

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select * from "user";'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getAllChatsByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select cid, chatname, owner from participates natural inner join chat where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result