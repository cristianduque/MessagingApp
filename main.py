from flask import Flask
from handler.users import UserHandler

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


# solo quiero provar que sirve
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
def parts():
    handler = UserHandler()
    return handler.getAllUsers()
if __name__ == '__main__':
    app.run()