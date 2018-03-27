from dao.MessageDAO import MessageDAO
from flask import jsonify

class MessageHandler:

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1], 'Chat': m[2], 'Date': m[3], 'Time': m[4], 'SenderId': m[5]}
        return mapped

    def getAllMessages(self):
        messages = MessageDAO().allMessages()
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(AllMessages=result)

    def getMessagesFromChat(self, cid):
        messages = MessageDAO().messagesFromChat(cid)
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(MessagesFromChat=result)

    def getMessagesFromUser(self, uid):
        messages = MessageDAO().messagesFromUser(uid)
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(MessagesFromUser=result)

    def getMessageReplies(self, mid):
        messages = MessageDAO().messageReply(mid)
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(MessageReplies=result)
