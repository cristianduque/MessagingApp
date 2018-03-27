class UserDAO:
    def __init__(self):
        U1 = [123, 'Cristian', 'Duque', 7872015817, 'cduque@upr.edu']
        U2 = [456, 'Kristalys', 'Ruiz', 7874292951, 'kruiz@upr.edu']
        U3 = [78, 'Gladymar', 'Oneill', 7876624695, 'goneill@upr.edu']
        U4 = [910, 'Javier', 'Correa', 7878901234, 'j.correa@upr.edu']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def getNumberMessagesByUserId(self, id):
        if id == 123:
            return 45
        elif id == 456:
            return 105
        elif id == 78:
            return 300
        elif id == 910:
            return 400
        else:
            return None

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

    def contactlistofUser(self, uid):
        result = []
        if uid == 123:
            return result
        elif uid == 456:
            result.append(self.data[0])
            result.append(self.data[2])
            result.append(self.data[3])

            return result
        elif uid == 78:
            result.append(self.data[0])
            return result
        elif uid == 910:
            result.append(self.data[0])
            result.append(self.data[1])
            result.append(self.data[2])
            result.append(self.data[3])
            return result
        else:
            return result



