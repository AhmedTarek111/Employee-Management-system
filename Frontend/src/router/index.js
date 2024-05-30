import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Listcompany from '../components/company/ListCompany.vue'
import ListDeprtment from '../components/department/ListDeprtment.vue'
import Listemployee from '../components/employee/ListEmployee.vue'
import CompanyDetails from '../components/company/CompanyDetails.vue'
import CompanyUpdate from '../components/company/CompanyUpdate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/company/list/',
      name: 'ListCompany',
      component: Listcompany
    },
    {
      path: '/department/list/',
      name: 'ListDepartment',
      component: ListDeprtment
    },
    {
      path: '/employee/list/',
      name: 'ListEmployee',
      component: Listemployee
    },
  
    {
      path: '/company/detail/:id/',
      name: 'CompanyDetail',
      component: CompanyDetails
    },
    {
      path: '/company/update/:id/',
      name: 'CompanyDetails',
      component: CompanyUpdate
    },
  
  ]
})

export default router
