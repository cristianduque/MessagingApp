from dao.ContactListDAO import ContactListDAO
from flask import jsonify

class ContactListHandler:

    def maptoDicContactList(self, cl):
        mapped= {'ContactListID': cl[0], 'OwnerID': cl[1]}
        return mapped

    def mapToDict(self, row):
        result = {'uid': row[0], 'first_name': row[1], 'last_name': row[2], 'phone': row[3], 'email': row[4]}
        return result

    def getAllContactLists(self):
        contactList = ContactListDAO().allContactLists()
        result = []
        for cl in contactList:
            result.append(self.maptoDicContactList(cl))
        return jsonify(AllContactList=result)

    def getUsersInContactList(self, uid):
        users = ContactListDAO().contactlistofUser(uid)
        result = []
        for u in users:
            result.append(self.mapToDict(u))
        return jsonify(AllUsersInCOntactList=result)

