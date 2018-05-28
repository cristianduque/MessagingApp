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
        query = 'select hashname, date(time), count(mid) from hashtag  natural inner join containhash natural inner join message group by hashname, date(time) order by count(mid) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def trendUser(self):
        cursor = self.conn.cursor()
        query = 'select username, date(time), count(*) from "user" natural inner join message group by date(time), username order by date(time) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def numdislike(self):
        cursor = self.conn.cursor()
        query = 'select count(*), date(time) from message natural inner join dislike group by date(time) order by date(time) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result
    
    def numlike(self):
        cursor = self.conn.cursor()
        query = 'select count(*), date(time) from message natural inner join "like" group by date(time) order by date(time) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result
    
    def numreply(self):
        cursor = self.conn.cursor()
        query = 'select count(*), date(time) from message as m,reply as r where m.mid=r.reply group by date(time) order by date(time) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def nummessage(self):
        cursor = self.conn.cursor()
        query = 'select count(*), date(time) from message group by date(time) order by date(time) desc;'
        cursor.execute(query)
        result = []
        for m in cursor:
            result.append(m)
        return result

    def dashboardInfo(self):
        self.mostusedHashs()
        self.activeUsers()
        return self.partofHashboard

    def mostusedHashs(self):
        self.partofHashboard.append(self.hashtags)
    
    def activeUsers(self):
        self.partofHashboard.append(self.users)


