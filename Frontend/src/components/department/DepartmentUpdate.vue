<template>
  <div>
    <div class="container">
      <h2>Update Department</h2>
      <form @submit.prevent="departmentUpdate">
        <div class="form-group">
          <label for="name">Department Name</label>
          <input type="text" class="form-control" id="name" v-model="Department.name">
        </div>

        <div class="form-group">
          <label for="company">Department:</label>
          <select id="company" v-model="Department.company" class="form-control" required>
            <option value="">Select Company</option>
            <option v-for="company in companies" :key="company.id" :value="company.id">{{ company.name }}</option>
          </select>
        </div>
       
        <button type="submit" class="btn btn-primary">Update Department</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DepartmentUpdate',
  data() {
    return {
      companies: [], 
      Department: {
        name: '',
        company: ''
      },
      Departmentid: this.$route.params.id
    };
  },
  methods: {
    getDepartmentDetails() {
      axios({
        url: `http://127.0.0.1:8000/department/retrieve-destroy/${this.Departmentid}/`,
        method: 'get'
      }).then(response => {
        this.Department = response.data;
      }).catch(error => {
        console.error('There was an error fetching the department details:', error);
      });
    },
    departmentUpdate() {
      axios({
        url: `http://127.0.0.1:8000/department/update/${this.Departmentid}/`,
        method: 'put',
        data: this.Department,
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => {
        alert('Department updated successfully');
        this.$router.push(`/department/detail/${this.Departmentid}/`);
      }).catch(error => {
        console.error('There was an error updating the department:', error.response.data);
      });
    },
    listCompany() {
      axios({
        url: 'http://127.0.0.1:8000/company/list/',
        method: 'get'
      }).then(response => {
        this.companies = response.data;
      }).catch(error => {
        console.error('There was an error fetching the companies:', error);
      });
    }
  },
  mounted() {
    this.getDepartmentDetails();
    this.listCompany();
  }
}
</script>
