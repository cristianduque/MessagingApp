from flask import jsonify
from dao.UserDAO import UserDAO


class UserHandler:

    def mapToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4]}
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)

    def getAllChatsByUserId(self, id):
        dao = UserDAO()
        result = dao.getAllChatsByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.maptoChatDict(r))
        return jsonify(Chats=mapped_result)

    def getNumberMessagesByUserId(self,id):
        dao = UserDAO()
        result = dao.getNumberMessagesByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            return jsonify(Messages=result)

    def getMessagesByUserId(self,id):
        dao = UserDAO()
        result = dao.getMessagesByUserId(id)
        r = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for m in result:
                r.append(self.maptoDicMessage(m))

            return jsonify(Messages=r)

    def maptoChatDict(self, row):
        result = {'cid': row[0], 'chatname': row[1], 'ownerid': row[2]}
        return result

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1], 'Chat': m[2], 'Date': m[3], 'Time': m[4], 'SenderId': m[5]}
        return mapped