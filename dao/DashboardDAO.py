from dao.MessageDAO import MessageDAO
from dao.HashtagDAO import HashtagDao
from dao.UserDAO import UserDAO
import psycopg2
from config.dbconfig import pg_config

class DashboardDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

        numdis = self.numdislike()
        numlike = self.numlike()
        numMessage = self.nummessage()
        numReply = self.numreply()

        self.hashtags = self.trendHash()
        self.users = self.trendUser()

        self.partofHashboard = []
        self.partofHashboard.append(numdis)
        self.partofHashboard.append(numlike)
        self.partofHashboard.append(numMessage)
        self.partofHashboard.append(numReply)

    def trendHash(self):
        cursor = self.conn.cursor()
        query = 'select hashname from hashtag;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def trendUser(self):
        cursor = self.conn.cursor()
        query = 'select username from "user";'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def numdislike(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from dislike;'
        cursor.execute(query)
        return cursor.fetchone()
    
    def numlike(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from "like";'
        cursor.execute(query)
        return cursor.fetchone()
    
    def numreply(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from reply;'
        cursor.execute(query)
        return cursor.fetchone()

    def nummessage(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message;'
        cursor.execute(query)
        return cursor.fetchone()

    def dashboardInfo(self):
        self.mostusedHashs()
        self.activeUsers()
        return self.partofHashboard

    def mostusedHashs(self):
        self.partofHashboard.append(self.hashtags)
    
    def activeUsers(self):
        self.partofHashboard.append(self.users)
