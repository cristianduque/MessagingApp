from dao.MessageDAO import MessageDAO

class UserDAO:
    def __init__(self):
        U1 = [123, 'Cristian', 'Duque', 7872015817, 'cduque@upr.edu']
        U2 = [456, 'Kristalys', 'Ruiz', 7874292951, 'kruiz@upr.edu']
        U3 = [78, 'Gladymar', 'Oneill', 7876624695, 'goneill@upr.edu']
        U4 = [910, 'Javier', 'Correa', 7878901234, 'j.correa@upr.edu']

        self.messages = MessageDAO().allMessages()

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def getNumberMessagesByUserId(self, uid):
        a = 0
        for m in self.messages:
            if m[5] == uid:
                a += 1
        return a

    def getAllUsers(self):
        return self.data

    def getAllChatsByUserId(self, uid):
        result = []
        if uid == 123:
            result.append(['45', 'RUM'])
            result.append(['105', 'GroupICOM5016'])
            result.append(['500', 'Los Guerrilleros'])
            return result
        elif uid == 456:
            result.append(['45', 'RUM'])
            result.append(['105', 'GroupICOM5016'])
            result.append(['500', 'Los Guerrilleros'])
            result.append(['55', 'Family'])
            return result
        elif uid == 78:
            result.append(['45', 'RUM'])
            result.append(['105', 'GrupoICOM5016'])
            result.append(['55', 'Family'])
            return result
        elif uid == 910:
            result.append(['45', 'RUM'])
            result.append(['500', 'Los Guerrilleros'])
            result.append(['55', 'Family'])
            return result
        else:
            return result


