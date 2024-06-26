import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import AboutView from '../views/AboutView.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',      
    component: AboutView
  },
  {
    path:'/SignUp',
    name:'SignUp',
    component: SignUp

  },
  {
    path:'/Login',
    name:'Login',
    component: Login

  },
  {
    path:'/Profile',
    name:Profile,
    component:Profile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
