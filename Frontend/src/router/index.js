import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Listcompany from '../components/company/ListCompany.vue'
import ListDeprtment from '../components/department/ListDeprtment.vue'
import Listemployee from '../components/employee/ListEmployee.vue'
import CompanyDetails from '../components/company/CompanyDetails.vue'
import CompanyUpdate from '../components/company/CompanyUpdate.vue'
import DepartemntDetail from '../components/department/DepartmentDetails.vue'
import DepartemntUpdate from '../components/department/DepartmentUpdate.vue'
import EmployeeDetail from '../components/employee/EmployeeDetails.vue'
import EmployeeCreation from '../components/employee/EmployeeCreation.vue'
import EmployeeUpdate from '../components/employee/EmployeeUpdate.vue'
import store from '../store'
import HomePage from '../components/Home.vue'
import Login from '../components/auth/Login.vue'
import Signup from '../components/auth/Signup .vue'
import CreateCompany from '../components/company/CompanyCreation.vue'
import CreateDepartment from '../components/department/DepartmentCreation.vue'
import UserProfile from '../components/User/UserProfile.vue'

const routes = [
  // company
  {
    path: '/company/list/',
    name: 'ListCompany',
    component: Listcompany,
    meta: { requiresAuth: true }
  },
  {
    path: '/company/create/',
    name: 'CreateCompany',
    component: CreateCompany,
    meta: { requiresAuth: true }
  },
  {
    path: '/company/detail/:id/',
    name: 'CompanyDetail',
    component: CompanyDetails,
    meta: { requiresAuth: true }
  },
  {
    path: '/company/update/:id/',
    name: 'CompanyUpdate',
    component: CompanyUpdate,
    meta: { requiresAuth: true }
  },
  // department
  {
    path: '/department/list/',
    name: 'ListDepartment',
    component: ListDeprtment,
    meta: { requiresAuth: true }
  },
  {
    path: '/department/detail/:id/',
    name: 'DepartemntDetail',
    component: DepartemntDetail,
    meta: { requiresAuth: true }
  },
  {
    path: '/department/update/:id/',
    name: 'DepartemntUpdate',
    component: DepartemntUpdate,
    meta: { requiresAuth: true }
  },
  {
    path: '/department/create/',
    name: 'CreateDepartment',
    component: CreateDepartment,
    meta: { requiresAuth: true }
  },
  // employee
  {
    path: '/employee/list/',
    name: 'ListEmployee',
    component: Listemployee,
    meta: { requiresAuth: true }
  },
  {
    path: '/employee/detail/:id/',
    name: 'EmployeeDetail',
    component: EmployeeDetail,
    meta: { requiresAuth: true }
  },
  {
    path: '/employee/create/',
    name: 'EmployeeCreate',
    component: EmployeeCreation,
    meta: { requiresAuth: true }
  },
  {
    path: '/employee/update/:id/',
    name: 'EmployeeUpdate',
    component: EmployeeUpdate,
    meta: { requiresAuth: true }
  },
  // home page
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    meta: { requiresAuth: true }
  },
  // login page
  {
    path: '/login/',
    name: 'login',
    component: Login,
  },
  // sign up 
  {
    path:'/signup/',
    name:'Signup ',
    component:Signup
  },
  {
    path:'/user/profile/',
    name:'UserProfile ',
    component:UserProfile
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;