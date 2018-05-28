from dao.MessageDAO import MessageDAO
from flask import jsonify, make_response
from dao.HashtagDAO import HashtagDao

class MessageHandler:

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1], 'Chat': m[2], 'Date': m[3], 'Username': m[4]}
        return mapped

    def mapChatMessage(self, m):
        return {'Username': m[0], 'MessageID': m[1], 'Time': m[2], 'Text': m[3], 'Likedby': m[4], 'Dislikedby': m[5], 'Likes': m[6], 'Dislikes': m[7], 'Reply': m[8]}

    def mapUserMessage(self, m):
        return {'Chatname': m[0], 'ChatID': m[1], 'MessageID': m[2], 'Time': m[3], 'Text': m[4]}

    def getMessageById(self, mid):
        messages = MessageDAO().messageById(mid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
            return jsonify(Message=result)

    def getAllMessages(self):
        messages = MessageDAO().allMessages()
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.maptoDicMessage(m))
        return jsonify(AllMessages=result)

    def getMessagesFromChat(self, cid):
        messages = MessageDAO().messagesFromChat(cid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapChatMessage(m))
        return jsonify(MessagesFromChat=result)

    def getMessagesFromUser(self, uid):
        messages = MessageDAO().messagesFromUser(uid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapUserMessage(m))
        return jsonify(MessagesFromUser=result)

    def getalllikes(self):
        dao = MessageDAO().getLikes()
        if not dao:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.maplikesall(l))
        return jsonify(AllLikes=result)

    def getalldislikes(self):
        dao = MessageDAO().getDislikes()
        if not dao:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.mapdislikesall(l))
        return jsonify(AllDislikes=result)

    def getMessageReplies(self, mid):
        messages = MessageDAO().messageReply(mid)
        if not messages:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in messages:
            result.append(self.mapreply(m))
        return jsonify(MessageReplies=result)

    def getMessageRepliesCount(self, mid):
        messages = MessageDAO().countRepliesMessage(mid)
        if messages==None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(MessageReplies=messages)

    def getmessagedislikes(self, mid):
        dao = MessageDAO().messagesDislikes(mid)
        if not dao:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for l in dao:
            result.append(self.mapdislikes(l))
        return jsonify(DislikeInMessage=result)

    def getmessagelikes(self, mid):
        dao = MessageDAO().messageLikes(mid)
        if not dao:
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

    def postmessageh(self, msginfo):
        uid = msginfo['uid']
        cid = msginfo['cid']
        text = msginfo['text']
        m = MessageDAO().postmessage(cid, uid, text)
        if not m:
            return jsonify(Error="NOT FOUND"), 404
        result = {'mid': m}
        return jsonify(result), 201

    def liked(self, likeinfo):
        uid = likeinfo['uid']
        mid = likeinfo['mid']
        r = MessageDAO().insertlike(uid, mid)
        print("tal veez llego aqui handler")
        return jsonify(Result=r), 200

    def disliked(self, dislikeinfo):
        uid = dislikeinfo['uid']
        mid = dislikeinfo['mid']
        r = MessageDAO().insertdislike(uid, mid)
        print("tal veez llego aqui handler")
        return jsonify(Result=r), 200

    def mapdislikes(self, d):
        return {'userThatDisliked': d[0]}

    def maplikes(self, d):
        return {'userThatLiked': d[0]}

    def maplikesall(self, d):
        return {'MessageID': d[0], 'userThatLiked': d[1]}

    def mapdislikesall(self, d):
        return {'MessageID': d[0], 'userThatDisliked': d[1]}

    def mapreply(self, d):
        return {'Username': d[1], 'Reply': d[0]}

