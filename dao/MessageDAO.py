import psycopg2
from config.dbconfig import pg_config

class MessageDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)
        M1 = [1, 'Necesito que traigas pan para el desayuno', 45,  "2023, 11, 25", '14, 32, 0, 0', 123]
        M2 = [2, 'Tengo examen esta semana', 105,  "2023, 12, 25", '14, 11, 0, 0', 78]
        M3 = [3, 'Hola', 45,  "2023, 11, 10", '7, 9, 0, 0', 456]
        M4 = [4, ':)', 500,  "1995, 11, 25", '8, 7, 0, 0', 910]
        M5 = [5, 'Tu te vas?', 55,  "4571, 10, 2", '22, 48, 0, 0', 456]
        M6 = [6, 'FELICIDADES!', 55,  "2017, 6, 14", '18, 00, 0, 0', 78]
        M7 = [7, 'Mami estoy bien', 105,  "2023, 11, 25", '23, 23, 0, 0', 123]
        M8 = [8, 'No puedo subir esta semana. #estudiar', 105,  "2023, 11, 3", '0, 45, 0, 0', 123]
        M9 = [9, 'Donde vamos a comer? #Tengohambre', 105,  "2023, 11, 25", '19, 31, 0, 0', 456]
        self.messages = []
        self.messages.append(M1)
        self.messages.append(M2)
        self.messages.append(M3)
        self.messages.append(M4)
        self.messages.append(M5)
        self.messages.append(M6)
        self.messages.append(M7)
        self.messages.append(M8)
        self.messages.append(M9)
        RMessage1 = [87, 8, 7]
        RMessage2 = [89, 8, 9]
        self.reply = [RMessage1, RMessage2]
        L1 = [1123, 1, 123]
        L2 = [2456, 2, 456]
        self.likes = [L1, L2]
        D1 = [178, 1, 78]
        D2 = [1910, 1, 910]
        self.dislikes = [D1, D2]

    def allMessages(self):
        cursor = self.conn.cursor()
        query = "select * from message;"
        cursor.execute(query)
        return cursor

    def messageById(self, mid):
        cursor = self.conn.cursor()
        query =  "select * from message where mid=%s"
        cursor.execute(query, (mid, ))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def messagesFromChat(self, cid):
        cursor = self.conn.cursor()
        query = "select * from chat natural inner join message where cid=%s;"
        result = []
        cursor.execute(query, (cid, ))
        for m in cursor:
            result.append(m)
        return result

    def messagesFromUser(self, uid):
        cursor = self.conn.cursor()
        query = "select * from 'user' natural inner join message where uid=%s;"
        result = []
        cursor.execute(query, (uid, ) )
        for m in cursor:
            result.append(m)
        return result

    def getReply(self):
        cursor = self.conn.cursor()
        query = "select * from message, reply, message where message.mid=reply.reply and message.mid=reply.mid;"
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messageReply(self, mid):
        cursor = self.conn.cursor()
        query = "select * from message inner join reply inner join message on message.mid=reply.mid, message.mid=reply.reply where mid=%s;"
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def getLikes(self):
        cursor = self.conn.cursor()
        query = 'select * from message natural inner join "like" natural inner join "user";'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messageLikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select * from message natural inner join "like" natural inner join "user" where mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def getDislikes(self):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join dislike natural inner join 'user';"
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messagesDislikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select * from message natural inner join dislike natural inner join "user" where mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countLikes(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join like natural inner join "user";'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def countDislikes(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join dislike natural inner join "user";'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def countReplies(self):
        cursor = self.conn.cursor()
        query = "select count(*) from message, reply, message where message.mid=reply.mid and message.mid=reply.reply;"
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def countLikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join "like" natural inner join "user" where mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countDislikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join dislike natural inner join "user" where mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countRepliesMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from message, reply, message where message.mid=reply.mid and message.mid=reply.reply and mid=%s;"
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countMessages(self):
        cursor = self.conn.cursor()
        query = "select count(*) from message;"
        cursor.execute(query)
        return cursor