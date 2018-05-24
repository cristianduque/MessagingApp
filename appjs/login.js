angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope',
    function($http, $log, $scope){
    //aqui va jejejejeje todo
        var thisCtrl = this;
        var mem = sessionStorage;
        // esta parte aqui sesupone que szea donde se guarda toda la infomacion que se hace de login
        var uid = 5;
        var cid = 1;
        var username = kruiz;
        var chatname = helloworld;
        mem.setItem('uid', 1);
        mem.setItem('cid', 2);
        mem.setItem('chatname', chatname);
        mem.setItem('username', username);
    }