import Vue from 'vue'
import Router from 'vue-router'
import QuickStart from './views/QuickStart.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path: '/',
    name: 'quick-start',
    component: QuickStart
  }]
})
