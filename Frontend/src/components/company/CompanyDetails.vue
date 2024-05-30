<template>
  <div>
    <div class="container">
      <h2>{{ companydetail.name }} Company </h2>

      <div class="container mt-5">
        <h2 class="mb-4">Company Details</h2>
        <table class="table table-bordered table-shadow">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Company Name</th>
              <th scope="col">Number of Departments</th>
              <th scope="col">Number of Employees</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ companydetail.name }}</td>
              <td>{{ companydetail.number_of_departments }}</td>
              <td>{{ companydetail.number_of_employees }}</td>
            </tr>
          </tbody>
        </table>

        <h3 class="mt-5 mb-3">Departments Of Company</h3>
        <table class="table table-bordered table-shadow">
          <thead class="thead-light">
            <tr>
              <th scope="col">Department Name</th>
              <th scope="col">Number of Employees</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="department in relatedDepartments" :key="department.name">
              <td>{{ department.name }}</td>
              <td>{{ department.number_of_employees }}</td>
            </tr>
          </tbody>
        </table>

        <h3 class="mt-5 mb-3">Employees in various departments</h3>
        <table class="table table-bordered table-shadow">
          <thead class="thead-light">
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Department</th>
              <th scope="col">Status</th>
              <th scope="col">Email</th>
              <th scope="col">Mobile Number</th>
              <th scope="col">Address</th>
              <th scope="col">Designation</th>
              <th scope="col">Hired On</th>
              <th scope="col">Days Employed</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="employee in relatedEmployees" :key="employee.email">
              <td>{{ employee.name }}</td>
              <td>{{ employee.department }}</td>
              <td>{{ employee.status }}</td>
              <td>{{ employee.email }}</td>
              <td>{{ employee.mobile_number }}</td>
              <td>{{ employee.address }}</td>
              <td>{{ employee.designation }}</td>
              <td>{{ employee.hired_on }}</td>
              <td>{{ employee.days_employed }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CompanyDetails',
  data() {
    return {
      companydetail: '',
      Companyid: this.$route.params.id,
      relatedDepartments: [],
      relatedEmployees: [],
    };
  },
  methods: {
    getCompanyDetails() {
      axios({
        url: `http://127.0.0.1:8000/company/retrieve-destroy/${this.Companyid}/`,
        method: 'get',
      }).then(response => {
        this.companydetail = response.data;
      });
    },
    getRelatedDepartments() {
      axios({
        url: `http://127.0.0.1:8000/department-related/${this.Companyid}/`,
        method: 'get',
      }).then(response => {
        this.relatedDepartments = response.data;
      });
    },
    getRelatedEmployees() {
      axios({
        url: `http://127.0.0.1:8000/employee/related-employee/${this.Companyid}/`,
        method: 'get',
      }).then(response => {
        this.relatedEmployees = response.data;
      });
    },
  },
  mounted() {
    this.getCompanyDetails();
    this.getRelatedDepartments();
    this.getRelatedEmployees();
  },
};
</script>

<style scoped>
.table-shadow {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
