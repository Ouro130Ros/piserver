var app = angular.module('app',[
    'ngRoute'
]);

app.config(['$routeProvider', function ($routeProvider) {
    //================================================
    // Routes
    //================================================
		console.log('route configured')
    $routeProvider.when('/', {
        templateUrl: 'static/partials/controllerViews/indexTemplate.html',
        controller: 'indexCtrl'
    });
}]);
