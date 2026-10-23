/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./data/**/*.js",
    "./context-guides-data.js"
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#2563eb",
        "primary-light": "#60a5fa",
        "primary-dark": "#1d4ed8",
        "surface": "#f8f9ff",
        "card": "#ffffff",
        "border": "#e2e8f0",
        "text-main": "#0f172a",
        "text-muted": "#64748b",
        "masking": "#10b981",
        "masking-bg": "#d1fae5"
      },
      spacing: {
        "sidebar-width": "320px",
        "essay-width": "400px"
      }
    }
  },
  plugins: []
};
