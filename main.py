from flask import Flask
from handler.users import UserHandler
from handler.chats import ChatHandler

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/')
def home():
    return "Hello World"

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
def chatOwners():
    handler = ChatHandler()
    return handler.getAllOwners()

@app.route('/SocialMessagingApp/chats/users/<int:cid>')
def chatUsers(cid):
    handler = ChatHandler()
    return handler.getAllUsersInChat(cid)

if __name__ == '__main__':
    app.run()