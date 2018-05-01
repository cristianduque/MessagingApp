from dao.MessageDAO import MessageDAO
import psycopg2
from config.dbconfig import pg_config

class HashtagDao:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def allHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag;"
        cursor.execute(query)
        return cursor

    def messageWSpecificHash(self, hname):
        cursor = self.conn.cursor()
        query = "select mid, text from message natural inner join containhash natural inner join hashtag where hashname=%s;"
        result = []
        cursor.execute(query, (hname, ))
        for m in cursor:
            result.append(m)
        return result

    def hashtagsInMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select hid, hashname from message natural inner join containhash natural inner join hashtag where mid=%s;"
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result