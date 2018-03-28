from flask import Flask
from handler.UserHandler import UserHandler
from handler.ChatHandler import ChatHandler
from handler.ContactListHandler import ContactListHandler
from handler.HashtagHandler import HashtagHandler
from handler.MessageHandler import MessageHandler

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/')
def home():
    return "Welcome Intruder!"

@app.route('/SocialMessagingApp/')
def homeforApp():
    return "Here goes a nice logo of our app and a very short descripion of what this does\r\n Basically we are doing WhatsApp from scratch. Thanks Professor! Very interesting..."

@app.route('/SocialMessagingApp/users/<int:uid>/chats')
def getAllChatsByUserId(uid):
    return UserHandler().getAllChatsByUserId(uid)

@app.route('/SocialMessagingApp/users/<int:uid>/messages')
def getNumberMessagesByUserId(uid):
    return UserHandler().getNumberMessagesByUserId(uid)

@app.route('/SocialMessagingApp/users')
def users():
    handler = UserHandler()
    return handler.getAllUsers()

@app.route('/SocialMessagingApp/chats')
def chats():
    handler = ChatHandler()
    return handler.getAllChats()

@app.route('/SocialMessagingApp/chat/<int:cid>/owner')
def chatOwner(cid):
    handler = ChatHandler()
    return handler.getOwner(cid)

@app.route('/SocialMessagingApp/chats/users/<int:cid>')
def chatUsers(cid):
    handler = ChatHandler()
    return handler.getAllUsersInChat(cid)

@app.route('/SocialMessagingApp/hashtags')
def hashtags():
    handler = HashtagHandler()
    return handler.getAllhashtags()
@app.route('/SocialMessagingApp/hashtag/<string:hname>')
def givenHash(hname):
    handler = HashtagHandler()
    return handler.getmessagewithhas(hname)

@app.route('/SocialMessagingApp/messages')
def allmessages():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/SocialMessagingApp/chat/<int:cid>/messages')
def messagesInchat(cid):
    handler = MessageHandler()
    return handler.getMessagesFromChat(cid)

@app.route('/SocialMessagingApp/user/<int:uid>/contactlist')
def contactsOfUsers(uid):
    handler = ContactListHandler()
    return handler.getUsersInContactList(uid)

@app.route('/SocialMessagingApp/contactlist')
def allContactList():
    handler = ContactListHandler()
    return handler.getAllContactLists()

if __name__ == '__main__':
    app.run()