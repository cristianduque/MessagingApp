angular.module('AppChat').controller('ContactsController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var mem = sessionStorage;
        var thisCtrl = this;
        this.contactList_id;
        this.uid = mem.getItem('uid');
        this.contacts = [];
        thisCtrl.ctid = ""

        this.loadContacts = function() {
            var reqURL = "http://localhost:5000/SocialMessagingApp/user/contactlist/" + thisCtrl.uid;
            console.log("reqURL: " + reqURL);
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller

                    /*
                    * Stores the data received from python call. The jsonyfied data
                    */
                    thisCtrl.contacts = response.data.AllUsersInCOntactList;
                    console.log(thisCtrl.contacts);
                },
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
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

                    }
                    else {

                    }
                });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.addContact = function() {
            var reqURL = "http://localhost:5000/SocialMessagingApp/contactlist/adduser/" + thisCtrl.uid + "/" + thisCtrl.ctid;
            console.log("reqURL: " + reqURL);
//            data = {"owner_id": thisCtrl.currentUser.user_id, "username": username}
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));

                },
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
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

                    }
                    else {
                        //was added;
                    }
                });
            thisCtrl.ctid = ""
        };

        this.showChats = function() {
            $location.path('/chatMenu');
        };

        this.loadContacts();

    }]);