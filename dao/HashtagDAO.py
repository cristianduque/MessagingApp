from dao.MessageDAO import MessageDAO

class HashtagDao:
    def __init__(self):

        H1 = [1, 'Tengohambre']
        H2 = [2, "estudiar"]

        HinM1 = [19, 1, 9]
        HinM2 = [28, 2, 8]

        self.messages = MessageDAO().allMessages()

        self.hash = []
        self.hash.append(H1)
        self.hash.append(H2)

        self.messagewithhash = []
        self.messagewithhash.append(HinM1)
        self.messagewithhash.append(HinM2)

    def allHashtags(self):
        return self.hash

    def messageswithHashtag(self):
        mwh = []
        for m in self.messagewithhash:
            mwh.append(self.messages[m[2]])
        return mwh

    def messageWSpecificHash(self, hash):
        result = []
        for m in self.messagewithhash:
            if self.hash[m[1]-1][1] == hash:
                result.append(self.messages[m[2]-1])
        return result







