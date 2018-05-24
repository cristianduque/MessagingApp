angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$window',
    function($http, $log, $scope) {

        // esto sesupone que va en loginpero lo tengo aqui para que all funcione

        var mem = sessionStorage;


        var uid = 5;
        var cid = 1;
        var username = 'kruiz';
        var chatname = 'helloworld';
        mem.setItem('uid', 1);
        mem.setItem('cid', 2);
        mem.setItem('chatname', chatname);
        mem.setItem('username', username);


        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.newText = "";
        this.cid = mem.getItem('cid');
        this.uid = mem.getItem('uid');

        console.log(thisCtrl.uid);

        this.loadMessages = function(){
            console.log(thisCtrl.cid);
            thisCtrl.loadMessageDB().then(function(response){
                thisCtrl.msgHW = response.data.MessagesFromChat;
                var n=thisCtrl.msgHW.length;
                $log.error("Message Loaded: ", JSON.stringify(thisCtrl.msgHW));


                for(var i=n; i>=0; i--){
                    var m = thisCtrl.msgHW[i];
                    if (m!=null)
                        thisCtrl.messageList.push({"mid": m.MessageID, "text": m.Text, "author": m.Username, "like": m.Likes, "nolike": m.Dislikes});
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

            var url = "http://localhost:5000/SocialMessagingApp/chat/message/" + thisCtrl.chatinfo['cid'];
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            //EEHW
            data = {'cid': 1, 'uid': 4, 'text': msg};
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/post',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(response){
                var m = response.data.mid;
                console.log(JSON.stringify(response.data));
                console.log(m)
                thisCtrl.messageList.unshift({"mid": m, "text": msg, "author": 'SALIO', "like": 0, "nolike": 0});
            }).catch(function(error){
                console.log("este es el error" + error);
            });
            thisCtrl.newText = "";
        };

        this.loadLikesAndDislikes = function(){
            window.location = "http://localhost:63343/SocialMessagingApp/pages/interactions.html";
        };

        this.likeadd= function(t) {
            var data = {'uid': thisCtrl.userinfo['uid'] , 'mid': t['mid']}
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/like/insert',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(){
                t.like++;
            });

        };
        this.dislikeadd= function(t) {
            var data = {'uid': thisCtrl.userinfo['uid'] , 'mid': t['mid']}
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/dislike/insert',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(){
                t.nolike++;
            });

        };

        this.loadMessages();
    }]);
