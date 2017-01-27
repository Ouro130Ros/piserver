(function(){
  angular.module('app')
  .directive('testApiGetArguments', function(){
    return {
      scope:{
      },
      controller: function($scope, httpExt){
          $scope.apiResult = '';
          httpExt.GetFromHttp($scope, '/api/ExampleAPIGetWithArgument', 'apiResult', null, {'argument': 'success'});
      },
      templateUrl: 'static/partials/directiveViews/testApiGetWithArgument.html'
    }
  })
})();
