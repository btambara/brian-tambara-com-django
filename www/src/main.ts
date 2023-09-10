import 'vite/modulepreload-polyfill';
import { createApp } from 'vue'
import './style.css'
import App from './views/App.vue'
import Index from './views/Index.vue'

createApp(App).mount('#app')
createApp(Index).mount('#index')
