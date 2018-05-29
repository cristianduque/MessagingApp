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
        }).when('/dashboard',{
            templateUrl: 'pages/dashboard.html',
            controller: 'DashboardController',
            controllerAs : 'dashCtrl'
        }).when('/chatMenu',{
            templateUrl: 'pages/chatmenu.html',
            controller: 'ChatMenuController',
            controllerAs : 'chatMenuCtrl'
        }).when('/contacts', {
            templateUrl: 'pages/contacts.html',
            controller: 'ContactsController',
            controllerAs : 'contactCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);
    //

})();

