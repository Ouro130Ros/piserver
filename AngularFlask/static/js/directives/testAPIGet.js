(function(){
  angular.module('app')
  .directive('testApiGet', function(){
    return {
      scope:{
        injectedValue: '='
      },
      controller: function($scope, httpExt){
          $scope.apiResult = '';
          httpExt.GetFromHttp($scope, '/api/ExampleAPIGET', 'apiResult');
      },
      templateUrl: 'static/partials/directiveViews/testApiGet.html'
    }
  })
})();
