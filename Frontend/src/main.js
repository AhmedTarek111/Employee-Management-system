import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex'

const app = createApp(App)

app.use(router)

app.mount('#app')

const store = createStore({
    state: {},
    mutations: {},
    getters:{},
    actions:{},
  })