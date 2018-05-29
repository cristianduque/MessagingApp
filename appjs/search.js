angular.module('AppChat').controller('SearchController', ['$http', '$log', '$location', '$scope', '$window',
    function($http, $log, $scope) {
        var mem = sessionStorage;

        var thisCtrl = this;

        this.msgHW = [];
        this.messageList = [];
        this.cid = mem.getItem('cid');
        this.hashname = "";

        this.searchhash = function(){
            thisCtrl.loadMessageDB().then(function(response){
                console.log(response.data);
                thisCtrl.msgHW = response.data.SearchHash;
                console.log(thisCtrl.msgHW);
                console.log(thisCtrl.msgHW[0])
                var n=thisCtrl.msgHW.length;
                for(var i=n-1; i>=0; i--){
                    thisCtrl.messageList.push({"mid": thisCtrl.msgHW[i].MessageID, "text": thisCtrl.msgHW[i].Message, "author": thisCtrl.msgHW[i].Username});
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
            this.hashname = ""

        };

        this.loadMessageDB = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            //EEHW
            console.log("LLE GA AQUIIIII");
            var url = "http://localhost:5000/SocialMessagingApp/chat/hashtag/message/" + thisCtrl.cid +"/" +thisCtrl.hashname;
            console.log(url);
            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            return $http.get(url)
        };

    }]);
