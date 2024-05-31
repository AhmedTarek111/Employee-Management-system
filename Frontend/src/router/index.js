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
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Comapny 
    {
      path: '/company/list/',
      name: 'ListCompany',
      component: Listcompany
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
    // Department
    {
      path: '/department/list/',
      name: 'ListDepartment',
      component: ListDeprtment
    },
    
    {
      path: '/department/detail/:id/',
      name: 'DepartemntDetail',
      component: DepartemntDetail
    },
    
    {
      path: '/department/update/:id/',
      name: 'DepartemntUpdate',
      component: DepartemntUpdate
    },
    
    // Employee
    {
      path: '/employee/list/',
      name: 'ListEmployee',
      component: Listemployee
    },
    {
      path: '/employee/detail/:id/',
      name: 'EmployeeDetail',
      component: EmployeeDetail
    },
    
    {
      path: '/employee/detail/:id/',
      name: 'EmployeeDetail',
      component: EmployeeDetail
    },
    
    {
      path: '/employee/create/',
      name: 'EmployeeCreate',
      component: EmployeeCreation
    },
    {
      path: '/employee/update/:id/',
      name: 'EmployeeUpdate',
      component: EmployeeUpdate
    },
    
    
  ]
})

export default router
