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
        query = 'select hashname, count(*) from hashtag  natural inner join containhash natural inner join message where age(time)<=INTERVAL %s group by hashname order by count(*) desc limit 10;'
        cursor.execute(query, ('7 days',))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def trendUser(self):
        cursor = self.conn.cursor()
        query = 'select username, count(*) from "user" natural inner join message where age(time)<=INTERVAL %s group by username order by count(*) desc limit 10;'
        cursor.execute(query, ('7 days',))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def numdislike(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join dislike where age(time)<=INTERVAL %s;'
        cursor.execute(query, ('7 days',))
        result = []
        return cursor.fetchone()[0]

    def numlike(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join "like" where age(time)<=INTERVAL %s;'
        cursor.execute(query, ('7 days',))
        return cursor.fetchone()[0]

    def numreply(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message natural inner join reply where age(time)<=INTERVAL %s;'
        cursor.execute(query, ('7 days',))
        return cursor.fetchone()[0]

    def nummessage(self):
        cursor = self.conn.cursor()
        query = 'select count(*) from message where age(time)<=INTERVAL %s;'
        cursor.execute(query, ('7 days',))
        return cursor.fetchone()[0]

    def dashboardInfo(self):
        self.mostusedHashs()
        self.activeUsers()
        return self.partofHashboard

    def mostusedHashs(self):
        self.partofHashboard.append(self.hashtags)
    
    def activeUsers(self):
        self.partofHashboard.append(self.users)


