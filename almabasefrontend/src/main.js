import Vue from 'vue'
import App from './App.vue'

import Login from './components/Login.vue'
import Signup from './components/Signup.vue'
import Home from './components/Home.vue'

import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueRouter)
Vue.use(VueAxios, axios)

const routes = [
  { 
    path: '/home', 
    name: 'home', 
    component: Home, 
    meta: { requiresAuth: true}
  },{ 
    path: '/login', 
    name: 'login', 
    component: Login, 
    meta: { requiresAuth: false}
  },{ 
    path: '/signup', 
    name: 'signup', 
    component: Signup, 
    meta: { requiresAuth: false}
  },{
    path: '*', 
    redirect: '/home', 
    meta: { requiresAuth: true}
  }]

const router = new VueRouter({
  routes // short for routes: routes
})

router.beforeEach((to, from, next) => {
  if(to.meta.requiresAuth){
    if(!localStorage.getItem('access_token')){
      next('/login')
    } 
  }
  next()
})

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  components: { App }
})
