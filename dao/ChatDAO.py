from dao.UserDAO import UserDAO
import psycopg2
from config.dbconfig import pg_config

class ChatDAO:
    def __init__(self):

       # C1 = [45, 'RUM', 123]
        #C2 = [105, 'GrupoICOM5016', 123]
        #3 = [500, 'Los Guerrilleros', 456]
        #C4 = [55, 'Family', 78]

      #  dao = UserDAO()
       # self.userData = dao.data

        #self.dataChats = []
        #self.dataChats.append(C1)
        #self.dataChats.append(C2)
        #self.dataChats.append(C3)
        #self.dataChats.append(C4)

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
        query = "select firstname, lastname, username, phone, email from 'user' as U inner join chat as C on U.uid = C.owner where cid = %s"
        cursor.execute(query, (cid,))
        result = []
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





