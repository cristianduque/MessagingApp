angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {

        var thisCtrl = this;
        this.currentUser = {};

        this.authenticateLogin = function(username, password){
            var reqURL = "http://localhost:5000/SocialMessagingApp/login";
                console.log("reqURL: " + reqURL);
                var data = {'username': username, 'password': password}
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        thisCtrl.currentUser = response.data;
                        console.log(thisCtrl.currentUser);
                        $location.path('/chat')
                    },
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    alert("Username and password do not match. Try again.");

                });

                $log.error("Users Loaded: ", JSON.stringify());
        };

        this.register = function(firstname, lastname, phone, email, password, username){
            var reqURL = "http://localhost:5000/SocialMessagingApp/register";
                console.log("reqURL: " + reqURL);
                var data = {'firstname': firstname, 'lastname': lastname, 'phone': phone, 'email': email, 'password': password, 'username': username}
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        thisCtrl.currentUser = JSON.stringify(response.data);
                        $location.path('/chat')
                    },
                    function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    alert("Invalid username. Try another.");

                });

                $log.error("Users Loaded: ", JSON.stringify());
        };
}]);