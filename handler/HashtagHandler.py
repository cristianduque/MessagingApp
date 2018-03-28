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
        result = []
        for h in hash:
            result.append(self.maptoDicHash(h))
        return jsonify(Allhashtags=result)

    def getmessageswithhash(self):
        hash = HashtagDao().messageswithHashtag()
        result = []
        for m in hash:
            result.append(self.maptoDicMessage(m))
        return jsonify(AllMessagesWithHash=result)

    def getmessagewithhas(self, hashtext):
        hash = HashtagDao().messageWSpecificHash(hashtext)
        result = []
        for m in hash:
            result.append(self.maptoDicMessage(m))
        return jsonify(MessagesWithHash=result)