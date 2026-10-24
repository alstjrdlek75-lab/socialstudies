const CACHE_NAME = 'edurecall-cache-v18';
const PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './assets/fsrs.umd.js',
  './assets/tailwind.out.css',
  './data/topics-index.js',
  './data/chunk-edu.js',
  './data/chunk-law.js',
  './data/chunk-soc.js',
  './data/chunk-pol.js',
  './data/chunk-econ.js',
  './data/chunk-exam.js',
  './context-guides-data.js',
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
  const isSameOrigin = url.origin === self.location.origin;
  event.respondWith(
    fetch(req, isSameOrigin ? { cache: 'no-cache' } : undefined)
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
        return caches.match(req, { ignoreSearch: true }).then((cachedRes) => {
          if (cachedRes) return cachedRes;
          if (req.mode === 'navigate') {
            return caches.match('./index.html', { ignoreSearch: true }) || caches.match('./');
          }
          return new Response('', { status: 408, statusText: 'Offline' });
        });
      })
  );
});
