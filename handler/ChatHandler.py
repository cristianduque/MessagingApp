from flask import jsonify
from dao.ChatDAO import ChatDAO

class ChatHandler:

    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        if not result:
            return jsonify(Error="No chats"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)

    def getChat(self, cid):
        dao = ChatDAO()
        result = dao.getChat(cid)
        if not result:
            return jsonify(Error= "Chat does not exist."), 404
        else:
            mapped_result = []
            for r in result:
              mapped_result.append(self.mapToDict(r))
            return jsonify(Chats=mapped_result)

    def getOwner(self, cid):
        dao = ChatDAO()
        result = dao.getOwnerOfChat(cid)
        if not result:
            return jsonify(Error="No chat with that ID"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapOwnerToDict(r))
            return jsonify(Owner=mapped_result)

    def getAllUsersInChat(self, cid):
        dao = ChatDAO()
        result = dao.getAllUsersInChat(cid)
        if not result:
            return jsonify(Error="No chat with that ID or no users in that chat"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToUsersInChatDict(r))
            return jsonify(UsersInChat=mapped_result)

    def addusertochat(self, cid, uid):
        r = ChatDAO().addUsertoChat(cid, uid)
        return jsonify(Result=r), 200

    def createchat(self, owner, chatname):
        cid = ChatDAO().addNewChat(chatname, owner)
        r = self.addusertochat(cid, owner)
        return r

    def mapToDict(self, row):
        result = {'cid': row[0], 'chatname': row[1]}
        return result

    def mapChatToDict(self, row):
        result = {'cid': row[0], 'chatname': row[1], 'owner': row[2]}
        return result

    def mapOwnerToDict(self, row):
        result = {'uid': row[0], 'firstname': row[1], 'lastname': row[2], 'phone': row[3], 'email': row[4], 'user_name': row[5]}
        return result

    def mapToUsersInChatDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4], 'user_name': row[5]}
        return result
