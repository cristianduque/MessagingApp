angular.module('AppChat').controller('ChatMenuController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.chatList = [];
        this.chatHW = [];

        this.loadChats = function(){
            thisCtrl.loadChatsDB().then(function(response){
                thisCtrl.chatHW = response.data.ChatsList;
                var n=thisCtrl.chatHW.length;
                $log.error("Chat Loaded: ", JSON.stringify(thisCtrl.chatHW));


                for(var i=n; i>=0; i--){
                    var c = thisCtrl.chatHW[i];
                    if (c!=null)
                        thisCtrl.chatList.push({"id": c.ChatID, "name": c.ChatName, "creator": c.Owner});
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

        this.loadChatsDB = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            //EEHW
            var url = "http://localhost:5000/SocialMessagingApp/chat";
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };


     //   this.loadLikesAndDislikes = function(){
     //       window.location = "http://localhost:63343/SocialMessagingApp/pages/interactions.html";
      //  };


    }]);