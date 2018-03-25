from flask import jsonify
from dao.chat import ChatDAO

class ChatHandler:
    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)

    def getAllOwners(self):
        dao = ChatDAO()
        result = dao.getAllOwners()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToOwnerDict(r))
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

    def mapToOwnerDict(self, row):
        result = {'cid': row[0], 'chatname': row[1], 'owner': row[2], 'ownerid': row[3]}
        return result
    def mapToUsersInChatDict(self, row):
        result = {'uid': row[0], 'name': row[1] + row[2]}
        return result
