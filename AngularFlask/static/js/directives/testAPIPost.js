(function(){
  angular.module('app')
  .directive('testApiPost', function(){
    return {
      scope:{
      },
      controller: function($scope, httpExt){
          $scope.apiResult = '';
          httpExt.PostToHttp('/api/ExampleAPIPOST', {'value': 'success'}, function(data, status, headers, config){
            $scope.apiResult = data
          })
      },
      templateUrl: 'static/partials/directiveViews/testApiPost.html'
    }
  })
})();
