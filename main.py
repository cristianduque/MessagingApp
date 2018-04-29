from flask import Flask
from handler.UserHandler import UserHandler
from handler.ChatHandler import ChatHandler
from handler.ContactListHandler import ContactListHandler
from handler.HashtagHandler import HashtagHandler
from handler.MessageHandler import MessageHandler
from handler.DashboardHandler import DashboardHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
app.config["JSON_SORT_KEYS"] = False


@app.route('/')
def home():
    return "Welcome Intruder!"

@app.route('/SocialMessagingApp/login')
def login():
    return "LOGIN GOES HERE"

@app.route('/SocialMessagingApp/')
def homeforApp():
    return "Here goes a nice logo of our app and a very short descripion of what this does\n Basically we are doing WhatsApp from scratch. Thanks Professor! Very interesting..."

@app.route('/SocialMessagingApp/dashboard')
def dashboardsiplay():
    handler = DashboardHandler()
    return handler.dashboard()

@app.route('/SocialMessagingApp/user/chat/<int:uid>')
def getAllChatsByUserId(uid):
    return UserHandler().getAllChatsByUserId(uid)

@app.route('/SocialMessagingApp/user/message/num/<int:uid>')
def getNumberMessagesByUserId(uid):
    return UserHandler().getNumberMessagesByUserId(uid)

@app.route('/SocialMessagingApp/user/message/<int:uid>')
def getMessagesByUserId(uid):
    return UserHandler().getMessagesByUserId(uid)

@app.route('/SocialMessagingApp/user')
def users():
    handler = UserHandler()
    return handler.getAllUsers()

@app.route('/SocialMessagingApp/user/<int:uid>')
def getInformationOfUserById(uid):
    return UserHandler().getInformationOfUserById(uid)

@app.route('/SocialMessagingApp/user/<string:username>')
def getInformationOfUserByUsername(username):
    return UserHandler().getInformationOfUserByUsername(username)

@app.route('/SocialMessagingApp/chat')
def chats():
    handler = ChatHandler()
    return handler.getAllChats()

@app.route('/SocialMessagingApp/chat/owner/<int:cid>')
def chatOwner(cid):
    handler = ChatHandler()
    return handler.getOwner(cid)

@app.route('/SocialMessagingApp/chat/user/<int:cid>')
def chatUsers(cid):
    handler = ChatHandler()
    return handler.getAllUsersInChat(cid)

@app.route('/SocialMessagingApp/chat/message/<int:cid>')
def messagesInchat(cid):
    handler = MessageHandler()
    return handler.getMessagesFromChat(cid)

@app.route('/SocialMessagingApp/message')
def allmessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/SocialMessagingApp/message/<int:mid>')
def messagebyid(mid):
    handler = MessageHandler()
    return handler.getMessageById(mid)

@app.route('/SocialMessagingApp/hashtag')
def hashtags():
    handler = HashtagHandler()
    return handler.getAllhashtags()

@app.route('/SocialMessagingApp/message/hashtag/<int:mid>')
def messagehashtags(mid):
    handler = HashtagHandler()
    return handler.gethashsInMessage(mid)

@app.route('/SocialMessagingApp/hashtag/<string:hname>')
def givenHash(hname):
    handler = HashtagHandler()
    return handler.getmessagewithhas(hname)

@app.route('/SocialMessagingApp/dislike')
def getalldislikes():
    handler = MessageHandler()
    return handler.getalldislikes()

@app.route('/SocialMessagingApp/like')
def getalllikes():
    handler = MessageHandler()
    return handler.getalllikes()

@app.route('/SocialMessagingApp/message/like/<int:mid>')
def getlikesinmessage(mid):
    handler = MessageHandler()
    return handler.getmessagelikes(mid)

@app.route('/SocialMessagingApp/message/dislike/<int:mid>')
def getdislikesinmessage(mid):
    handler = MessageHandler()
    return handler.getmessagedislikes(mid)

@app.route('/SocialMessagingApp/message/like/num/<int:mid>')
def getlikesinmessagenum(mid):
    handler = MessageHandler()
    return handler.getmessagelikesCount(mid)

@app.route('/SocialMessagingApp/message/dislike/num/<int:mid>')
def getdislikesinmessagenum(mid):
    handler = MessageHandler()
    return handler.getmessagedislikesCount(mid)

@app.route('/SocialMessagingApp/user/contactlist/<int:uid>')
def contactsOfUsers(uid):
    handler = ContactListHandler()
    return handler.getUsersInContactList(uid)

@app.route('/SocialMessagingApp/contactlist')
def allContactList():
    handler = ContactListHandler()
    return handler.getAllContactLists()

if __name__ == '__main__':
    app.run()