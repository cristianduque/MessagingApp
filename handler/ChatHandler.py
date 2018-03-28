from flask import jsonify
from dao.ChatDAO import ChatDAO

class ChatHandler:
    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)

    def getOwner(self, cid):
        dao = ChatDAO()
        result = dao.getOwnerOfChat(cid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapOwnerToDict(result)
            return jsonify(Owners=mapped_result)

    def getAllUsersInChat(self, cid):
        dao = ChatDAO()
        result = dao.getAllUsersInChat(cid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToUsersInChatDict(r))
            return jsonify(UsersInChat=mapped_result)

    def mapToDict(self, row):
        result = {'cid': row[0], 'chatname': row[1]}
        return result

    def mapOwnerToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4]}
        return result
    def mapToUsersInChatDict(self, row):
        result = {'uid': row[0], 'name': row[1] + row[2]}
        return result
