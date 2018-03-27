from dao.UserDAO import UserDAO
class ChatDAO:
    def __init__(self):

        C1 = [45, 'RUM', 123]
        C2 = [105, 'GrupoICOM5016', 123]
        C3 = [500, 'Los Guerrilleros', 456]
        C4 = [55, 'Family', 78]

        dao = UserDAO()
        self.userData = dao.data

        self.dataChats = []
        self.dataChats.append(C1)
        self.dataChats.append(C2)
        self.dataChats.append(C3)
        self.dataChats.append(C4)

    def getAllChats(self):
        return self.dataChats

    def getAllOwners(self):
        owner = []
        for o in self.dataChats:
            owner.append(o)


    def getAllUsersInChat(self, cid):
        result = []
        if cid == 45:
            result.append(self.userData[0])
            result.append(self.userData[1])
            result.append(self.userData[2])
            result.append(self.userData[3])
            return result
        elif cid == 105:
            result.append(self.userData[0])
            result.append(self.userData[1])
            result.append(self.userData[2])
            return result
        elif cid == 500:
            result.append(self.userData[1])
            result.append(self.userData[0])
            result.append(self.userData[3])
            return result
        elif cid == 55:
            result.append(self.userData[2])
            result.append(self.userData[1])
            result.append(self.userData[3])
            return result
        else:
            return result




