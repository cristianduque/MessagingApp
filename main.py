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


@app.route('/') #OK
def home():
    return "Welcome Intruder!"

@app.route('/SocialMessagingApp/login') #OK
def login():
    return "LOGIN GOES HERE"

@app.route('/SocialMessagingApp/') #OK
def homeforApp():
    return "Here goes a nice logo of our app and a very short descripion of what this does\n Basically we are doing WhatsApp from scratch. Thanks Professor! Very interesting..."

@app.route('/SocialMessagingApp/dashboard') #OK
def dashboardsiplay():
    handler = DashboardHandler()
    return handler.dashboard()

@app.route('/SocialMessagingApp/user/chat/<int:uid>') #wrong outputs, 2 es el 3, 3 es el 4, pero sale bien el Error: not found
def getAllChatsByUserId(uid):
    return UserHandler().getAllChatsByUserId(uid)

@app.route('/SocialMessagingApp/user/message/num/<int:uid>')#wrong outputs, 2 es el 3, 3 es el 4, pero sale bien el Error: not found
def getNumberMessagesByUserId(uid):
    return UserHandler().getNumberMessagesByUserId(uid)

@app.route('/SocialMessagingApp/user/message/<int:uid>') #wrong outputs, 2 es el 3, 3 es el 4, pero sale bien el Error: not found
def getMessagesByUserId(uid):
    return MessageHandler().getMessagesFromUser(uid)

@app.route('/SocialMessagingApp/user') #OK
def users():
    handler = UserHandler()
    return handler.getAllUsers()

@app.route('/SocialMessagingApp/user/<int:uid>') #OK
def getInformationOfUserById(uid):
    return UserHandler().getInformationOfUserById(uid)

@app.route('/SocialMessagingApp/user/<string:username>') #ISE
def getInformationOfUserByUsername(username):
    return UserHandler().getInformationOfUserByUsername(username)

@app.route('/SocialMessagingApp/chat') #OK
def chats():
    handler = ChatHandler()
    return handler.getAllChats()

@app.route('/SocialMessagingApp/chat/owner/<int:cid>') #ISE, index error, arrgelar 404
def chatOwner(cid):
    handler = ChatHandler()
    return handler.getOwner(cid)

@app.route('/SocialMessagingApp/chat/user/<int:cid>') #mismo output to-do el tiempo, arrglar 404
def chatUsers(cid):
    handler = ChatHandler()
    return handler.getAllUsersInChat(cid)

@app.route('/SocialMessagingApp/chat/message/<int:cid>') #OK, vacio si no hay nada
def messagesInchat(cid):
    handler = MessageHandler()
    return handler.getMessagesFromChat(cid)

@app.route('/SocialMessagingApp/message') #OK
def allmessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/SocialMessagingApp/message/<int:mid>') #ISE
def messagebyid(mid):
    handler = MessageHandler()
    return handler.getMessageById(mid)

@app.route('/SocialMessagingApp/hashtag') #OK
def hashtags():
    handler = HashtagHandler()
    return handler.getAllhashtags()

@app.route('/SocialMessagingApp/message/hashtag/<int:mid>') #empty result
def messagehashtags(mid):
    handler = HashtagHandler()
    return handler.gethashsInMessage(mid)

@app.route('/SocialMessagingApp/hashtag/<string:hname>') #OK, except name y los que no existan
def givenHash(hname):
    handler = HashtagHandler()
    return handler.getmessagewithhas(hname)

@app.route('/SocialMessagingApp/dislike') #OK, pero no dice que usuario
def getalldislikes():
    handler = MessageHandler()
    return handler.getalldislikes()

@app.route('/SocialMessagingApp/like')   #OK, pero no dice que usuario
def getalllikes():
    handler = MessageHandler()
    return handler.getalllikes()

@app.route('/SocialMessagingApp/message/like/<int:mid>') #OK
def getlikesinmessage(mid):
    handler = MessageHandler()
    return handler.getmessagelikes(mid)

@app.route('/SocialMessagingApp/message/reply/<int:mid>') #OK
def getreplyinmessage(mid):
    handler = MessageHandler()
    return handler.getMessageReplies(mid)

@app.route('/SocialMessagingApp/message/dislike/<int:mid>') #OK
def getdislikesinmessage(mid):
    handler = MessageHandler()
    return handler.getmessagedislikes(mid)

@app.route('/SocialMessagingApp/message/like/num/<int:mid>') #OK
def getlikesinmessagenum(mid):
    handler = MessageHandler()
    return handler.getmessagelikesCount(mid)

@app.route('/SocialMessagingApp/message/reply/num/<int:mid>')  #OK
def getreplyinmessagenum(mid):
    handler = MessageHandler()
    return handler.getMessageRepliesCount(mid)

@app.route('/SocialMessagingApp/message/dislike/num/<int:mid>') #OK
def getdislikesinmessagenum(mid):
    handler = MessageHandler()
    return handler.getmessagedislikesCount(mid)

@app.route('/SocialMessagingApp/user/contactlist/<int:uid>') #OK
def contactsOfUsers(uid):
    handler = ContactListHandler()
    return handler.getAllContactsFromUser(uid)

@app.route('/SocialMessagingApp/contactlist') #ok
def allContactList():
    handler = ContactListHandler()
    return handler.getAllContactLists()

@app.route('/SocialMessagingApp/chat/<int:cid>')
def getChat(cid):
    handler = ChatHandler()
    return handler.getChat(cid)

if __name__ == '__main__':
    app.run()