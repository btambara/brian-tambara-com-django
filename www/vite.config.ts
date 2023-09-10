import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/',
  build: {
    manifest: true,
    emptyOutDir: true,
    target: "ES2020",
    rollupOptions: {
      input: {
        main: "./src/main.ts",
      },
      output: {
        chunkFileNames: undefined,
      },
    }
  }
})
