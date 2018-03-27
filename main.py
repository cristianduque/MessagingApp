from flask import Flask
from handler.UserHandler import UserHandler
from handler.ChatHandler import ChatHandler

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

@app.route('/SocialMessagingApp/chats/owners')
def chatOwner():
    handler = ChatHandler()
    return handler.get

@app.route('/SocialMessagingApp/chats/users/<int:cid>')
def chatUsers(cid):
    handler = ChatHandler()
    return handler.getAllUsersInChat(cid)



if __name__ == '__main__':
    app.run()