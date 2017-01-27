(function () {
    angular.module('app')
    .service('httpExt', function ($http) {
        this.get = $http.get;
        this.post = $http.post;

        this.GetFromHttp = function (scope, url, target, callback, prms) {
            var parameters = typeof prms !== 'undefined' && prms !== null ? prms : {};
            $http.get(url, { params: parameters })
                .success(function (data, status, headers, config) {
                    if (target !== null) { scope[target] = data; }
                    if (typeof callback !== 'undefined' && callback !== null) { callback(data, status, headers, config); }
                });
        }

        this.PostToHttp = function (url, object, callback) {
            $http.post(url, object)
                .success(function (data, status, headers, config) {
                    if (typeof callback !== 'undefined' && callback !== null) { callback(data, status, headers, config); }
                });
        }

        this.PostToGetPDF = function (url, object, callback) {
            $http.post(url, object, {responseType:'arraybuffer'})
                .success(function (data, status, headers, config) {
                    if (typeof callback !== 'undefined' && callback !== null) { callback(data, status, headers, config); }
                });
        }
    });
})();
