from  dao.UserDAO import UserDAO

class ContactListDAO:
    def __init__(self):

        CL1 = [1, 123]
        CL2 = [2, 456]
        CL3 = [3, 78]
        CL4 = [4, 910]

        self.contactList = [CL1, CL2, CL3, CL4]
        self.users = UserDAO().getAllUsers()


    def allContactLists(self):
        return self.contactList


    def contactlistofUser(self, uid):
        result = []
        if uid == 123:
            return
        elif uid == 456:
            result.append(self.users[0])
            result.append(self.users[2])
            result.append(self.users[3])
            return result
        elif uid == 78:
            result.append(self.users[0])
            return result
        elif uid == 910:
            result.append(self.users[0])
            result.append(self.users[1])
            result.append(self.users[2])
            result.append(self.users[3])
            return result
        else:
            return result