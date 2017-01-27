angular.module('app')
  .controller('indexCtrl', ['$scope', function($scope) {
      console.log("Index Controller Executed");
      $scope.GetValue = "GET VALUE";
      $scope.ControllerVariable = 'Controller Variable Value';
  }]);
