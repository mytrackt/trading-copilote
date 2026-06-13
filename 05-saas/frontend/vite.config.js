import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Dev/preview lies STRICTEMENT a 127.0.0.1 (jamais d'exposition reseau).
export default defineConfig({
  plugins: [react()],
  server: { host: '127.0.0.1', port: 5173 },
  preview: { host: '127.0.0.1', port: 4173 },
})
