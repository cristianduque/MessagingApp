angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$window',
    function($http, $log, $scope) {

        // esto sesupone que va en loginpero lo tengo aqui para que all funcione

        var mem = sessionStorage;

        //mem.setItem('uid', 3);
        //mem.setItem('cid', 1);
        //mem.setItem('chatname', 'nena');
        //mem.setItem('username', 'kruiz');


        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.newText = "";
        this.cid = mem.getItem('cid');
        this.uid = mem.getItem('uid');
        this.username = mem.getItem('username');
        this.chatname = mem.getItem('chatname');

        this.refresh = function () {
            return;
        }

        this.loadMessages = function(){
            thisCtrl.loadMessageDB().then(function(response){
                thisCtrl.msgHW = response.data.MessagesFromChat;

                var n=thisCtrl.msgHW.length;
                //$log.error
                //console.log

                for(var i=n; i>=0; i--){
                    mr = thisCtrl.msgHW[i];
                    if (mr!=null)
                        if(mr.ReplyId == 0)
                            thisCtrl.messageList.push({"mid": mr.MessageID, "text": mr.Text, "author": mr.Username, "like": mr.Likes, "nolike": mr.Dislikes, "minfo": mr, "reply": mr.Reply});
                        else
                            thisCtrl.messageList.push({"mid": mr.MessageID, "text": "Reply:" + mr.Text, "author": mr.Username, "like": mr.Likes, "nolike": mr.Dislikes, "minfo": mr, "reply": mr.Reply});

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
            var url = "http://localhost:5000/SocialMessagingApp/chat/message/" + thisCtrl.cid;
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            if (msg=="")
                return;
            // Need to figure out who I am
            //EEHW
            data = {'cid': thisCtrl.cid, 'uid': thisCtrl.uid, 'text': msg,  'reply': null};
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/post',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(response){
                var m = response.data.mid;
                thisCtrl.messageList.unshift({"mid": m, "text": msg, "author": thisCtrl.username, "like": 0, "nolike": 0, "reply": null, "minfo": {'Likedby': null, 'Dislikedby': null}});
            }).catch(function(error){
                console.log("este es el error" + error);
            });
            thisCtrl.newText = "";
        };

        this.loadDislikes = function(m){
            if(m.minfo.Dislikedby == null)
                alert("No dislikes yet :)");
            else {
                var list = "User that disliked the message: \n";
                var ref = m.minfo.Dislikedby;
                for (var i = 0; i < m.minfo.Dislikedby.length; i++)
                    list+= m.minfo.Dislikedby[i] + " \n";
                alert(list);
            }
        }

        this.loadLikes = function(m){
            if(m.minfo.Likedby == null)
                alert("No likes yet :(");
            else {
                var list = "User that liked the message: \n";
                var ref = m.minfo.Likedby;
                for (var i = 0; i < m.minfo.Likedby.length; i++)
                    list+= m.minfo.Likedby[i] + " \n";
                alert(list);
            }

        };

        this.likeadd= function(t) {
            var user;
            if(t.minfo.Likedby != null) {
                for (var i = 0; i < t.minfo.Likedby.length; i++) {
                    user = t.minfo.Likedby[i];
                    if (user == thisCtrl.username) {
                        return
                    }
                }
            }
            var data = {'uid': thisCtrl.uid , 'mid': t['mid']}
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/like/insert',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(){
                if(t.minfo.Likedby != null) {
                    t.minfo.Likedby.push(thisCtrl.username);
                }
                else
                    t.minfo.Likedby = [thisCtrl.username];
                t.like++;
            });
        };

        this.dislikeadd= function(t) {
            var user;
            if(t.minfo.Dislikedby != null) {
                for (var i = 0; i < t.minfo.Dislikedby.length; i++) {
                    user = t.minfo.Dislikedby[i];
                    if (user == thisCtrl.username) {
                        return
                    }
                }
            }
            var data = {'uid': thisCtrl.uid , 'mid': t['mid']}
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/dislike/insert',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(){
                if(t.minfo.Dislikedby != null) {
                    t.minfo.Dislikedby.push(thisCtrl.username);
                }
                else
                    t.minfo.Dislikedby = [thisCtrl.username];
                t.nolike++;
            });
        };

        this.replymsg = function(m){
            var msg = thisCtrl.newText;
            if (msg=="")
                return;
            // Need to figure out who I am
            //EEHW
            data = {'cid': thisCtrl.cid, 'uid': thisCtrl.uid, 'text': msg,  'reply': m['mid'] };
            $http({
                url: 'http://localhost:5000/SocialMessagingApp/message/post',
                method: "PUT",
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(data)
            }).then(function(response){
                var mid = response.data.mid;
                thisCtrl.messageList.unshift({"mid": mid, "text": "Reply:" + msg, "author": thisCtrl.username, "like": 0, "nolike": 0, "reply": m.text, "minfo": {'Likedby': null, 'Dislikedby': null}});
            }).catch(function(error){
                console.log("este es el error");
            });
            thisCtrl.newText = "";

        };

        this.refresh = function(){
            var n=thisCtrl.messageList.length;
            //$log.error
            //console.log
            for(var i=n; i>=0; i--) {
                var t = thisCtrl.messageList.pop();
                thisCtrl.loadMessages();
            }
        };


        this.loadMessages();
    }]);
