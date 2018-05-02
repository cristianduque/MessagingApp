from dao.MessageDAO import MessageDAO
from flask import jsonify
from dao.HashtagDAO import HashtagDao

class MessageHandler:

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1][0], 'Chat': m[2], 'Date': m[3], 'Username': m[4]}
        return mapped

    def mapChatMessage(self, m):
        return {'Username': m[0], 'MessageID': m[1], 'Time': m[2], 'Text': m[3][0]}

    def mapUserMessage(self, m):
        return {'Chatname': m[0], 'ChatID': m[1], 'MessageID': m[2], 'Time': m[3], 'Text': m[4][0]}

    def getMessageById(self, mid):
        messages = MessageDAO().messageById(mid)
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
            return jsonify(Message=result)

    def getAllMessages(self):
        messages = MessageDAO().allMessages()
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(AllMessages=result)

    def getMessagesFromChat(self, cid):
        messages = MessageDAO().messagesFromChat(cid)
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapChatMessage(m))
        return jsonify(MessagesFromChat=result)

    def getMessagesFromUser(self, uid):
        messages = MessageDAO().messagesFromUser(uid)
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapUserMessage(m))
        return jsonify(MessagesFromUser=result)

    def getalllikes(self):
        dao = MessageDAO().getLikes()
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.maplikes(l))
        return jsonify(AllLikes=result)

    def getalldislikes(self):
        dao = MessageDAO().getDislikes()
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.mapdislikes(l))
        return jsonify(AllDislikes=result)

    def getMessageReplies(self, mid):
        messages = MessageDAO().messageReply(mid)
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapreply(m))
        return jsonify(MessageReplies=result)

    def getMessageRepliesCount(self, mid):
        messages = MessageDAO().countRepliesMessage(mid)
        if messages == None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(MessageReplies=messages)

    def getmessagedislikes(self, mid):
        dao = MessageDAO().messagesDislikes(mid)
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.mapdislikes(l))
        return jsonify(DislikeInMessage=result)

    def getmessagelikes(self, mid):
        dao = MessageDAO().messageLikes(mid)
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.maplikes(l))
        return jsonify(LikesInMessage=result)

    def getmessagedislikesCount(self, mid):
        dao = MessageDAO().countDislikesMessage(mid)
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(DislikeInMessage=dao)

    def getmessagelikesCount(self, mid):
        dao = MessageDAO().countLikesMessage(mid)
        if dao == None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(LikesInMessage=dao)

    def mapdislikes(self, d):
        return {'userThatDisliked': d[0]}

    def maplikes(self, d):
        return {'userThatLiked': d[0]}

    def mapreply(self, d):
        return {'Username': d[1], 'Reply': d[0][0] }

