import 'vite/modulepreload-polyfill';
import { createApp } from 'vue'
import './scss/style.scss'
import App from './views/App.vue'
import Index from './views/Index.vue'
import 'bootstrap'
import "bootstrap-icons/font/bootstrap-icons.css";

createApp(App).mount('#app')
createApp(Index).mount('#index')
