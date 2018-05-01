angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;


        this.msgHW = [];
        //   0MID, 1TEXT, 2AUTHOR, 3LIKE, 4DISLIKE
        var m1 = [1, "Holita", "Gladymar", 7, 10];
        var m2 = [2, "ADIOSSSS", "Cristian", 10, 5];
        var m3 = [3, "JAJAJAJA", "Kristalys", 0, 4];
        var m4 = [4, "Hola Mi Amigo", "Bob", 4, 1];
        var m5 = [5, "Hello World", "Joe", 11, 12];

        thisCtrl.msgHW.push(m5);
        thisCtrl.msgHW.push(m4);
        thisCtrl.msgHW.push(m3);
        thisCtrl.msgHW.push(m2);
        thisCtrl.msgHW.push(m1);

        this.messageList = [];
        this.newText = "";

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            var n=thisCtrl.msgHW.length;
            for(var i=0; i<n; i++){
                var m = thisCtrl.msgHW.pop();
                thisCtrl.messageList.unshift({"id": m[0], "text": m[1], "author": m[2], "like": m[3], "nolike": m[4]});
            }

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var id= thisCtrl.messageList.length+1;
            thisCtrl.msgHW.unshift([id, msg, author, 0, 0]);
            thisCtrl.newText = "";
            this.loadMessages();
        };

        this.loadMessages();
    }]);
