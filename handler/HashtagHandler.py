from dao.HashtagDAO import HashtagDao
from flask import jsonify

class HashtagHandler:
    def maptoDicHash(self, hash):
        mapped = {'HashtagId': hash[0], 'Hashtag': hash[1]}
        return mapped

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1], 'Chat': m[2], 'Date': m[3], 'Time': m[4], 'SenderId': m[5]}
        return mapped

    def getAllhashtags(self):
        hash = HashtagDao().allHashtags()
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for h in hash:
            result.append(self.maptoDicHash(h))
        return jsonify(Allhashtags=result)

    def getmessageswithhash(self):
        hash = HashtagDao().messageswithHashtag()
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in hash:
            result.append(self.maptoDicMessage(m))
        return jsonify(AllMessagesWithHash=result)

    def getmessagewithhas(self, hashtext):
        hash = HashtagDao().messageWSpecificHash(hashtext)
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in hash:
            result.append(self.maptoDicMessage(m))
        return jsonify(MessagesWithHash=result)

    def gethashsInMessage(self, mid):
        hash = HashtagDao().hashtagsInMessage(mid)
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in hash:
            result.append(self.maptoDicHash(m))
        return jsonify(HashInMessage=result)