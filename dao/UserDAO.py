from dao.MessageDAO import MessageDAO
import subprocess
import psycopg2
import os
from config.dbconfig import pg_config

class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def getNumberMessagesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select count(*) from message where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        self.conn.close()
        return result[0]

    def getMessagesByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from message where uid = %s;"
        cursor.execute(query, (uid, ))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = 'select uid, firstname, lastname, phone, email, is_active, username from "user";'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getAllChatsByUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select cid, chatname, owner from participateschat natural inner join chat where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getInformationOfUserById(self, uid):
        cursor = self.conn.cursor()
        query = 'select uid, firstname, lastname, phone, email, is_active, username from "user" where uid = %s;'
        cursor.execute(query, (uid, ))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getInformationOfUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = 'select uid, firstname, lastname, phone, email, is_active, username from "user" where username = %s;'
        cursor.execute(query, (username, ))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result

    def getCredentials(self, username, password):
        cursor = self.conn.cursor()
        query = 'select username, password from "user" where username = %s and password = %s;'
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        self.conn.close()
        return result[0]