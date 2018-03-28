from dao.MessageDAO import MessageDAO
from dao.HashtagDAO import HashtagDao
from dao.UserDAO import UserDAO

class DashboardDAO:
    def __init__(self):

        numdis = MessageDAO().countDislikes()
        numlike = MessageDAO().countLikes()
        numMessage = MessageDAO().countMessages()
        numReply = MessageDAO().countReplies()

        self.hashtags = HashtagDao().allHashtags()
        self.users = UserDAO().getAllUsers()
        self.messages = MessageDAO().allMessages()

        self.partofHashboard = []
        self.partofHashboard.append(numdis)
        self.partofHashboard.append(numlike)
        self.partofHashboard.append(numMessage)
        self.partofHashboard.append(numReply)

    def dashboardInfo(self):
        self.mostusedHashs()
        self.activeUsers()
        return self.partofHashboard

    def mostusedHashs(self):
        self.partofHashboard.append([self.hashtags[0]])
    
    def activeUsers(self):
        self.partofHashboard.append([self.users[0], self.users[1]])
