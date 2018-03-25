from flask import jsonify
from dao.user import UserDAO

class UserHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)

    def mapToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4]}
        return result

    def getAllChatsByUserId(self, id):
        dao = UserDAO()
        result = dao.getAllChatsByUserId(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.maptoChatDict(r))
        return jsonify(Chats=mapped_result)

    def maptoChatDict(self, row):
        result = {'cid': row[0], 'chatname': row[1]}
        return result


