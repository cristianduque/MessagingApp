from dao.ContactListDAO import ContactListDAO
from flask import jsonify

class ContactListHandler:

    def maptoDicContactList(self, cl):
        mapped= {'uid': cl[0], 'username': cl[1], 'Number of contacts': cl[2]}
        return mapped

    def mapToDict(self, row):
        result = {'contactid': row[0], 'contactusername': row[1]}
        return result

    def getAllContactLists(self):
        contactList = ContactListDAO().allContactLists()
        if not contactList:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for cl in contactList:
            result.append(self.maptoDicContactList(cl))
        return jsonify(AllContactList=result)

    def getAllContactsFromUser(self, uid):
        users = ContactListDAO().contactlistofUser(uid)
        if not users:
            return jsonify(Error="NOT FOUND"), 404
        result = []
        for u in users:
            result.append(self.mapToDict(u))
        return jsonify(AllUsersInCOntactList=result)

    def contactaddition(self, owner, uid):
        dao = ContactListDAO().insertContacttoList(owner, uid)
        return jsonify(Result=dao), 200
