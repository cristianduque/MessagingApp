from dao.HashtagDAO import HashtagDao
from flask import jsonify

class HashtagHandler:
    def maptoDicHash(self, hash):
        mapped = {'HashtagId': hash[0], 'Hashtag': hash[1]}
        return mapped

    def maptoDicHashname(self, hash):
        mapped = {'Hashtag': hash[0] }
        return mapped

    def maptoMess(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1][0]}
        return mapped

    def getAllhashtags(self):
        hash = HashtagDao().allHashtags()
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for h in hash:
            result.append(self.maptoDicHash(h))
        return jsonify(Allhashtags=result)

    def getmessagewithhas(self, hashtext):
        hash = HashtagDao().messageWSpecificHash(hashtext)
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in hash:
            result.append(self.maptoMess(m))
        return jsonify(MessagesWithHash=result)

    def gethashsInMessage(self, mid):
        hash = HashtagDao().hashtagsInMessage(mid)
        if hash == None:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for m in hash:
            result.append(self.maptoDicHash(m))
        return jsonify(HashInMessage=result)