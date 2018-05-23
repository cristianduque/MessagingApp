angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.newText = "";
        this.username= 2;

        this.loadMessages = function(){
            thisCtrl.loadMessageDB().then(function(response){
                thisCtrl.msgHW = response.data.MessagesFromChat;
                var n=thisCtrl.msgHW.length;
                $log.error("Message Loaded: ", JSON.stringify(thisCtrl.msgHW));


                for(var i=n; i>=0; i--){
                    var m = thisCtrl.msgHW[i];
                    if (m!=null)
                        thisCtrl.messageList.push({"id": m.MessageID, "text": m.Text, "author": m.Username, "like": m.Likes, "nolike": m.Dislikes});
                }

            }, function(error){
                var status = error.status;

                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    //alert("Error interno del sistema.");
                }
            });

        };

        this.loadMessageDB = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            //EEHW
            var url = "http://localhost:5000/SocialMessagingApp/chat/message/1";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            //EEHW
            data = {'cid': 1, 'uid': 4, 'text': msg}
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/post',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(response){
                m = response.data.Message
                thisCtrl.messageList.push({"id": m['mid'], "text": msg, "author": kruiz, "like": m.Likes, "nolike": m.Dislikes});

            });
            thisCtrl.newText = "";
        };

        this.loadLikesAndDislikes = function(){
            window.location = "http://localhost:63343/SocialMessagingApp/pages/interactions.html";
        };

        this.likeadd= function(t) {
            t.like++;
        };
        this.dislikeadd= function(t) {
            t.nolike++;
        };

        this.loadMessages();
    }]);
