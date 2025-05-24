// main.js 
import { createApp } from 'vue'
import App from '../App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from 'axios'


axios.defaults.baseURL = 'http://localhost:8000'  // 设置后端基础地址

const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.mount('#app')

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
