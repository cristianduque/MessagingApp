angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.msgHW = [20];
        this.backup = [];
        //   0MID, 1TEXT, 2AUTHOR, 3LIKE, 4DISLIKE
        var m1 = [0, "Holita", "Gladymar", 7, 10];
        var m2 = [1, "ADIOSSSS", "Cristian", 10, 5];
        var m3 = [2, "JAJAJAJA", "Kristalys", 0, 4];
        var m4 = [3, "Hola Mi Amigo", "Bob", 4, 1];
        var m5 = [4, "Hello World", "Joe", 11, 12];

        thisCtrl.msgHW[0] = m1;
        thisCtrl.msgHW[1] = m2;
        thisCtrl.msgHW[2] = m3;
        thisCtrl.msgHW[3] = m4;
        thisCtrl.msgHW[4] = m5;

        this.messageList = [];
        this.newText = "";

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            var n=thisCtrl.msgHW.length;
            for(var i=0; i<n; i++){
                var m = thisCtrl.msgHW[i]
                if (m!=null)
                    thisCtrl.messageList.unshift({"id": m[0], "text": m[1], "author": m[2], "like": m[3], "nolike": m[4]});
            }

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var id= thisCtrl.msgHW.length;
            thisCtrl.msgHW[id] = [id, msg, author, 0, 0];
            thisCtrl.newText = "";
            thisCtrl.refresh();
        };

        this.loadLikesAndDislikes = function(){
            window.location = "http://localhost:63342/MessagingApp/pages/interactions.html";
        };

        this.likeadd= function(t) {
            var msg = thisCtrl.msgHW[t];
            msg[3]++;
            thisCtrl.refresh();

        }
        this.dislikeadd= function(t) {
            var msg = thisCtrl.msgHW[t];
            msg[4]++;
            thisCtrl.refresh();
        }

        this.refresh= function () {
            var size = thisCtrl.messageList.length;
            for (var i=0; i<size;i++)
                var meh = thisCtrl.messageList.pop();
            thisCtrl.loadMessages();

        }



        this.loadMessages();
    }]);
