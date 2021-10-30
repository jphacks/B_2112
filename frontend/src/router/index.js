import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import About from '@/components/About'
import Singup from '../components/singup.vue'
import Singin from '../components/singin.vue'
import Singout from '../components/singout.vue'
import Mypage from '../components/mypage.vue'
import firebase from '../firebase.js'

Vue.use(Router)

const routes = [
  {
    path: '/mypage',
    name: 'HelloWorld',
    component: HelloWorld,
    meta: { requiresAuth: true }
  },
  {
    path: '/home',
    name: Home,
    component: Home
  },
  {
    path: '/about',
    name: About,
    component: About
  },
  {
    path: '/singup',
    name: 'singup',
    component: Singup
  },
  {
    path: '/',
    name: 'singin',
    component: Singin
  },
  {
    path: '/singout',
    name: 'singout',
    component: Singout
  },
  {
    path: '/mypaga',
    name: 'mypage',
    component: Mypage,
    meta: { requiresAuth: true }
  }
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some(recode => recode.meta.requiresAuth)
  if (requiresAuth && !(await firebase.getCurrentUser())) {
    next({ path: '/singin', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router
