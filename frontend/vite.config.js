import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: false,
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Your backend server
        changeOrigin: true,
        secure: false,
      },
      '/images': {
        target: 'http://localhost:8000', // Your backend server
        changeOrigin: true,
        secure: false,
      },
      '/static': {
        target: 'http://localhost:8000', // Your backend server
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
