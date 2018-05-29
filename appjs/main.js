(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).otherwise({
            templateUrl: 'pages/dashboard.html',
            //controller: 'DashboardController',
            controllerAs : 'dashCtrl'
        });
    }]);
    //

})();
