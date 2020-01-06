var CACHE_NAME = 'tutorial-db-cache-v1';
var urlsToCache = [
  '/',
  '/static/app/css/customCSS.css',
  '/static/app/js/burger.js',
  '/static/app/js/colorpad.js',
  '/static/app/js/custom.js',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - return response
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});