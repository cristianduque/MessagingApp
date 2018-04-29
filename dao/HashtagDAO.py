from dao.MessageDAO import MessageDAO
import psycopg2
from config.dbconfig import pg_config

class HashtagDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)
        H1 = [1, 'Tengohambre']
        H2 = [2, "estudiar"]
        HinM1 = [19, 1, 9]
        HinM2 = [28, 2, 8]
        self.messages = MessageDAO().allMessages()
        self.hash = []
        self.hash.append(H1)
        self.hash.append(H2)
        self.messagewithhash = []
        self.messagewithhash.append(HinM1)
        self.messagewithhash.append(HinM2)

    def allHashtags(self):
        cursor = self.conn.cursor()
        query = "select count(*) from hashtag;"
        cursor.execute(query)
        return cursor

    def messageswithHashtag(self):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join containhash;"
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messageWSpecificHash(self, hname):
        cursor = self.conn.cursor()
        query = ("select * from message natural inner join containhash natural inner join hashtag where hname=%s;", (hname))
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def hashtagsInMessage(self, mid):
        cursor = self.conn.cursor()
        query = ("select hname from message natural inner join containhash natural inner join hashtag where mid=%s;", (mid))
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result