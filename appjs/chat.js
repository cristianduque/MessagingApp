angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location',
    function($http, $log, $scope, $location) {
        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.newText = "";

        this.loadMessages = function(){
            thisCtrl.loadMessageDB().then(function(response){
                thisCtrl.msgHW = response.data.MessagesFromChat;
                var n=thisCtrl.msgHW.length;

                for(var i=0; i<n; i++){
                    var m = thisCtrl.msgHW[i];
                    if (m!=null)
                        thisCtrl.messageList.unshift({"id": m.MessageID, "text": m.Text, "author": m.Username, "like": m.Likes, "nolike": m.Dislikes});
                }

                thisCtrl.checkmsgHW();
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
            var url = "http://localhost:5000/SocialMessagingApp/chat/message/1";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            thisCtrl.messageList.unshift({"text": msg, "author": author, "like": 0, "nolike": 0});
            thisCtrl.newText = "";
        };

        this.loadLikesAndDislikes = function(){
            window.location = "http://localhost:63342/MessagingApp/pages/interactions.html?_ijt=im9qfn68smuustntffgq15llvp";
        };

        this.likeadd= function(t) {
            t.like++;
        };
        this.dislikeadd= function(t) {
            t.nolike++;
        };

        this.loadMessages();
    }]);
