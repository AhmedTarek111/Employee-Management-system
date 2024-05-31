<template>
    <div class="container">
      <h2>Update Employee</h2>
      <form @submit.prevent="updateEmployee" class="form">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="newUpdatedData.name" class="form-control">
        </div>
        <div class="form-group">
          <label for="company">Company:</label>
          <div v-if="!newUpdatedData.company"></div>
          <select id="company" v-model="newUpdatedData.company" class="form-control">
            <option value="">Select Company</option>
            <option v-for="company in companies" :key="company.id" :value="company.id">{{ company.name }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="department">Department:</label>
          <select id="department" v-model="newUpdatedData.department" @click="getDepartments(newUpdatedData.company)" class="form-control">
            <option value="">Select Department</option>
            <option v-for="department in departments" :key="department.id" :value="department.id">{{ department.name }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="status">Status:</label>
          <select id="status" v-model="newUpdatedData.status" class="form-control">
            <option value="">Select Status</option>
            <option value="Application Received">Application Received</option>
            <option value="Interview Scheduled">Interview Scheduled</option>
            <option value="Hired">Hired</option>
            <!-- Add more status options if needed -->
          </select>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="newUpdatedData.email" class="form-control">
        </div>
        <div class="form-group">
          <label for="mobile_number">Mobile Number:</label>
          <input type="tel" id="mobile_number" v-model="newUpdatedData.mobile_number" class="form-control">
        </div>
        <div class="form-group">
          <label for="address">Address:</label>
          <textarea id="address" v-model="newUpdatedData.address" rows="3" class="form-control"></textarea>
        </div>
        <div class="form-group">
          <label for="designation">Designation:</label>
          <input type="text" id="designation" v-model="newUpdatedData.designation" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Update Employee</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'EmployeeUpdate',
    data() {
      return {
        employeeId: this.$route.params.id,
        companies: [],
        departments: [],
        newUpdatedData: {
          name: '',
          company: '',
          department: '',
          email: '',
          mobile_number: '',
          address: '',
          designation: '',
          status: ''
        }
      };
    },
    methods: {
      // Method to fetch employee details
      getEmployeeDetails() {
        axios.get(`http://127.0.0.1:8000/employee/retrieve-destroy/${this.employeeId}/`)
          .then(response => {
            this.newUpdatedData = response.data;
            // After fetching employee details, get departments
            this.getDepartments(this.newUpdatedData.company);
          })
          .catch(error => {
            console.error('Error fetching employee details:', error);
          });
      },
      // Method to fetch list of companies
      listCompany() {
        axios.get('http://127.0.0.1:8000/company/list/')
          .then(response => {
            this.companies = response.data;
          })
          .catch(error => {
            console.error('Error fetching companies:', error);
          });
      },
      // Method to fetch departments based on selected company
      getDepartments(companyId) {
        if (companyId) {
          axios.get(`http://127.0.0.1:8000/department-related/${companyId}/`)
            .then(response => {
              this.departments = response.data;
            })
            .catch(error => {
              console.error('Error fetching departments:', error);
            });
        } else {
          this.departments = [];
        }
      },
      // Method to update employee
      updateEmployee() {
        axios.put(`http://127.0.0.1:8000/employee/update/${this.employeeId}/`, this.newUpdatedData)
          .then(response => {
            alert('Employee updated successfully');
            this.$router.push(`/employee/detail/${this.employeeId}/`);
          })
          .catch(error => {
            console.error('Error updating employee:', error.response.data);
          });
      }
    },
    mounted() {
      this.listCompany();
      this.getEmployeeDetails();
    },
    watch: {
      'newUpdatedData.company'(newCompanyId) {
        this.getDepartments(newCompanyId);
      }
    }
  };
  </script>
  