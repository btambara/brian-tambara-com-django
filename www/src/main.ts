import 'vite/modulepreload-polyfill';
import { createApp, } from 'vue'
import './scss/style.scss'
import Index from './views/Index.vue'
import Resume from './views/Resume.vue'
import 'bootstrap'
import "bootstrap-icons/font/bootstrap-icons.css";

createApp(Index).mount('#index')
createApp(Resume).mount('#resume')
