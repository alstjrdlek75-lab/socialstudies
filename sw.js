const CACHE_NAME = 'edurecall-cache-v15';
const PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './assets/fsrs.umd.js',
  './data/topics-index.js',
  './assets/edu_cover_1x1.png',
  './assets/edu_cover_16x9.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_URLS).catch(() => {});
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  // Skip Supabase API requests so cloud sync is always live
  if (url.hostname.includes('supabase.co')) return;

  // Network-first with cache fallback for HTML and JS data files so online users always get latest updates, while offline works seamlessly
  event.respondWith(
    fetch(req)
      .then((networkRes) => {
        if (networkRes && networkRes.status === 200 && (url.origin === self.location.origin || url.hostname.includes('cdn.jsdelivr.net'))) {
          const resClone = networkRes.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(req, resClone).catch(() => {});
          });
        }
        return networkRes;
      })
      .catch(() => {
        return caches.match(req).then((cachedRes) => {
          if (cachedRes) return cachedRes;
          if (req.mode === 'navigate') {
            return caches.match('./index.html') || caches.match('./');
          }
          return new Response('', { status: 408, statusText: 'Offline' });
        });
      })
  );
});
