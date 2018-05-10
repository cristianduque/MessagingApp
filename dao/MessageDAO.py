import psycopg2
from config.dbconfig import pg_config

class MessageDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def allMessages(self):
        cursor = self.conn.cursor()
        query = 'select  mid, text, chatname, time, username from chat natural inner join message natural inner join "user";'
        cursor.execute(query)
        return cursor

    def messageById(self, mid):
        cursor = self.conn.cursor()
        query =  'select mid, text, chatname, time, username  from chat natural inner join message natural inner join "user" where mid=%s'
        cursor.execute(query, (mid, ))
        result = []
        for m in cursor:
            result.append(m)
        return result

    def messagesFromChat(self, cid):
        cursor = self.conn.cursor()
        query = 'with likes as (select count(uid) as likes, mid from "like" group by mid), dislikes as (select count(uid) as dislikes, mid from dislike group by mid) select distinct u.username, m.mid, time, text, coalesce(likes.likes, 0) as likes, coalesce(dislikes.dislikes,0) as dislikes from chat as c natural inner join message as m natural inner join "user" as u left join dislikes on (m.mid = dislikes.mid) left join likes on (m.mid = likes.mid) where c.cid=%s group by likes.likes, dislikes.dislikes, u.username, m.mid;'
        result = []
        cursor.execute(query, (cid, ))
        for m in cursor:
            result.append(m)
        return result

    #original one
    def messagesFromChatwith(self, cid):
        cursor = self.conn.cursor()
        query = 'select username, mid, time, text  from chat natural inner join message natural inner join "user" where cid=%s;'
        result = []
        cursor.execute(query, (cid, ))
        for m in cursor:
            result.append(m)
        return result

    def messagesFromUser(self, uid):
        cursor = self.conn.cursor()
        query = 'select chatname, cid, mid, time, text  from chat natural inner join message natural inner join "user" where uid=%s;'
        result = []
        cursor.execute(query, (uid, ) )
        for m in cursor:
            result.append(m)
        return result

    def messageReply(self, mid):
        cursor = self.conn.cursor()
        query = 'select m2.text, u.username  from message as m1, reply as r, message as m2, "user" as u where u.uid=m2.uid and m1.mid=r.mid and m2.mid=r.reply and m1.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countRepliesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m1, reply as r, message as m2, "user" as u where u.uid=m2.uid and m1.mid=r.mid and m2.mid=r.reply and m1.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

    def getLikes(self):
        cursor = self.conn.cursor()
        query = 'select mid, username from "like" natural inner join "user";'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messageLikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select username from message as m, "like" as l, "user" as u where m.mid=l.mid and u.uid=l.uid and m.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def getDislikes(self):
        cursor = self.conn.cursor()
        query = 'select mid, username from "user" natural inner join dislike;'
        result = []
        cursor.execute(query)
        for m in cursor:
            result.append(m)
        return result

    def messagesDislikes(self, mid):
        cursor = self.conn.cursor()
        query = 'select username from message as m, dislike as d, "user" as u where m.mid=d.mid and u.uid=d.uid and m.mid=%s;'
        result = []
        cursor.execute(query, (mid, ))
        for m in cursor:
            result.append(m)
        return result

    def countLikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m, "like" as l, "user" as u where m.mid=l.mid and u.uid=l.uid and m.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

    def countDislikesMessage(self, mid):
        cursor = self.conn.cursor()
        query = 'select count(*) from message as m, dislike as d, "user" as u where m.mid=d.mid and u.uid=d.uid and m.mid=%s;'
        cursor.execute(query, (mid, ))
        return cursor.fetchone()[0]

