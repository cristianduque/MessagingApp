from flask import jsonify
from dao.UserDAO import UserDAO


class UserHandler:

    def mapToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4], 'password': row[5], 'active': row[6], 'username': row[7]}
        return result

    def mapToDict2(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4],
                  'password': row[5], 'username': row[6]}
        return result

    def mapToDict3(self, row):
        result = {'username': row[0], 'password': row[1]}
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)

    def getAllChatsByUserId(self, id):
        dao = UserDAO()
        result = dao.getAllChatsByUserId(id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.maptoChatDict(r))
        return jsonify(Chats=mapped_result)

    def getNumberMessagesByUserId(self,id):
        dao = UserDAO()
        result = dao.getNumberMessagesByUserId(id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            return jsonify(NumberMessages=result)

    def getInformationOfUserById(self, id):
        dao = UserDAO()
        result = dao.getInformationOfUserById(id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(UserInfo=mapped_result)

    def getInformationOfUserByUsername(self, uname):
        dao = UserDAO()
        result = dao.getInformationOfUserByUsername(uname)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict2(r))
        return jsonify(UserInfo=mapped_result)

    def getMessagesByUserId(self,id):
        dao = UserDAO()
        result = dao.getMessagesByUserId(id)
        r = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for m in result:
                r.append(self.maptoDicMessage(m))

            return jsonify(Messages=r)

    def getCredentials(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        username = form['username']
        password = form['password']
        if not username or not password:
            return jsonify(Error="Unexpected attributes in post request"), 400
        dao = UserDAO()
        result = dao.getCredentials(username, password)
        return jsonify(User=self.mapToDict3(result))

    def insertUser(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = form['firstname']
            lastname = form['lastname']
            phone = form['phone']
            email = form['email']
            password = form['password']
            username = form['username']
            if firstname and lastname and email and phone and password and username:
                dao = UserDAO()
                uid = dao.insertUser(firstname, lastname, phone, email, password, username)
                result = self.mapToDict2([uid, firstname, lastname, phone, email, password, username])
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def maptoChatDict(self, row):
        result = {'cid': row[0], 'chatname': row[1]}
        return result

    def maptoDicMessage(self, m):
        mapped = {'MessageId': m[0], 'Message': m[1], 'Chat': m[2], 'Date': m[3], 'Time': m[4], 'SenderId': m[5]}
        return mapped
