import datetime

class MessageDAO:
    def __init__(self):

        MT = [0, 'ggg', 1, 145, 1452, 1423]
        M1 = [1, 'Necesito que traigas pan para el desayuno', 45,  "2023, 11, 25", '14, 32, 0, 0', 123]
        M2 = [2, 'Tengo examen esta semana', 105,  "2023, 12, 25", '14, 11, 0, 0', 78]
        M3 = [3, 'Hola', 45,  "2023, 11, 10", '7, 9, 0, 0', 456]
        M4 = [4, ':)', 500,  "1995, 11, 25", '8, 7, 0, 0', 910]
        M5 = [5, 'Tu te vas?', 55,  "4571, 10, 2", '22, 48, 0, 0', 456]
        M6 = [6, 'FELICIDADES!', 55,  "2017, 6, 14", '18, 00, 0, 0', 78]
        M7 = [7, 'Mami estoy bien', 105,  "2023, 11, 25", '23, 23, 0, 0', 123]
        M8 = [8, 'No puedo subir esta semana. #estudiar', 105,  "2023, 11, 3", '0, 45, 0, 0', 123]
        M9 = [9, 'Donde vamos a comer? #Tengohambre', 105,  "2023, 11, 25", '19, 31, 0, 0', 456]

        RMessage1 = [87, 8, 7]
        RMessage2 = [89, 8, 9]

        self.reply = [RMessage1, RMessage2]

        self.messages = []
        self.messages.append(M1)
        self.messages.append(M2)
        self.messages.append(M3)
        self.messages.append(M4)
        self.messages.append(M5)
        self.messages.append(M6)
        self.messages.append(M7)
        self.messages.append(M8)
        self.messages.append(M9)

        self.tryuu = [MT]

    def allMessages(self):
        return self.messages

    def messagesFromChat(self, cid):
        chatmessages=[]
        for m in self.messages:
            if cid == m[2]:
                chatmessages.append(m)
        return chatmessages
    def messagesFromUser(self, uid):
        usermessages=[]
        for m in self.messages:
            if uid == m[5]:
                usermessages.append(m)
        return usermessages
    def messageReply(self, mid):
        replym = []
        for rm in self.reply:
            if rm[1] == mid:
                replym.append(self.messages[rm[2]-1])
        return replym
























