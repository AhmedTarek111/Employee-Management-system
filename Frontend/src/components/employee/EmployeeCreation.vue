<template>
    <div class="container">
      <h2>Create Employee</h2>
      <form @submit.prevent="createEmployee" class="form">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="newEmployee.name" required class="form-control">
        </div>
        <div class="form-group">
          <label for="company">Company:</label>
          <select id="company" v-model="newEmployee.company" required class="form-control">
            <option value="">Select Company</option>
            <option v-for="company in companies" :key="company.id" :value="company.id">{{ company.name }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="department">Department:</label>
          <select id="department" v-model="newEmployee.department" @click="getDepartments(newEmployee.company)" required class="form-control">
            <option value="">Select Department</option>
            <option v-for="department in departments" :key="department.id" :value="department.id">{{ department.name }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="newEmployee.email" required class="form-control">
        </div>
        <div class="form-group">
          <label for="mobile_number">Mobile Number:</label>
          <input type="tel" id="mobile_number" v-model="newEmployee.mobile_number" required class="form-control">
        </div>
        <div class="form-group">
          <label for="address">Address:</label>
          <textarea id="address" v-model="newEmployee.address" rows="3" required class="form-control"></textarea>
        </div>
        <div class="form-group">
          <label for="designation">Designation:</label>
          <input type="text" id="designation" v-model="newEmployee.designation" required class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Create Employee</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CreateEmployee',
    data() {
      return {
        companies: [],
        departments: [],
        newEmployee: {
          name: '',
          company: '',
          department: '',
          email: '',
          mobile_number: '',
          address: '',
          designation: '',
        },
      };
    },
    methods: {
      listCompany() {
        axios.get('http://127.0.0.1:8000/company/list/')
          .then(response => {
            this.companies = response.data;
          })
          .catch(error => {
            console.error('Error fetching companies:', error);
          });
      },
      getDepartments(companyId) {
        if (companyId) {
          axios({
            url:`http://127.0.0.1:8000/department-related/${companyId}/`,
            method:'get'
          }).then(response => {
              this.departments = response.data;
            })
            .catch(error => {
              console.error('Error fetching departments:', error);
            });
        } else {
          this.departments = [];
        }
      },
      createEmployee() {
          axios({
            url: 'http://127.0.0.1:8000/employee/create/',
            method: 'post',
            data: this.newEmployee
          })
          .then(response => {
            if (response.status === 201) {
              alert('The employee has been created');
              this.$router.push('/employee/list/');
            } else {
              console.error('Error:', response.status);
              alert('Creation failed. Please check the console for details.');
            }
          })
          .catch(error => {
            console.error('faield creating employee:', error);
          });
    },

    },
    mounted() {
      this.listCompany();
    },
    watch: {
      'newEmployee.company'(newCompanyId) {
        this.getDepartments(newCompanyId);
      },
    },
  };
  </script>
  
  <style scoped>

  </style>
  