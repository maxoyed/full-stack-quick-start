import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

const axiosInstance = axios.create({
  // baseURL: location.protocol + '//workbook.maxoyed.com'
  // baseURL: location.protocol + '//127.0.0.1:5000'
  baseURL: '/'
})

// Vue.use(Button)
Vue.use(VueAxios, axiosInstance)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
