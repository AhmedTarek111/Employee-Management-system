<template>
    <div class="container">
      <div class="d-flex d-flex justify-content-between align-items-center mb-3">
        <h2>Employee Hired</h2>
        
      </div>
      <table class="table table-striped mt-5">
        <thead class="text-center">
          <tr >
            <th>Name</th>
            <th>Company</th>
            <th>Department</th>
            <th>Status</th>
            <th>Email</th>
            <th>Mobile Number</th>
            <th>Address</th>
            <th>Designation</th>
            <th>Hired On</th>
            <th>Days Employed</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody class="mt-4 text-center">
          <tr v-for="employee in HiredEmployees">
            <td>{{ employee.name }}</td>
            <td>{{ employee.company }}</td>
            <td>{{ employee.department }}</td>
            <td>{{ employee.status }}</td>
            <td>{{ employee.email }}</td>
            <td>{{ employee.mobile_number }}</td>
            <td>{{ employee.address }}</td>
            <td>{{ employee.designation }}</td>
            <td>{{ employee.hired_on }}</td>
            <td>{{ employee.days_employed }}</td>
            <td class="d-flex">
                <router-link :to="`/employee/update/${employee.id}/`">
                    <a href=""><i class="fa-regular fa-pen-to-square me-3" ></i></a>
                  </router-link>
                  <a @click="deleteEmployee(employee.id)"><i class="fa-solid fa-trash " style="color: red;"></i></a>
              </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
<script>
import axios from 'axios';

 
export default {
    name:'EmployeeDetails',
    data() {
        return {
            HiredEmployees:''
        }
    },
    methods: {
        listHiredEmployee(){
            axios({
                url:`http://127.0.0.1:8000/employee/list/hired/`,
                method:'get',

            }).then(response => this.HiredEmployees = response.data)
        },
        deleteEmployee(id){
      axios({
        url:`http://127.0.0.1:8000/employee/retrieve-destroy/${id}/`,
        method:'delete',
      }).then((response) => {
      if (response.status === 204) { 
        this.$router.push('/employee/list/'); 
        alert('The employee has been deleted');
      } else {
        console.error('Error:', response.status);
        alert('Deletion failed. Please check the console for details.');
      }
    })
      .then(alert('The employee has been deleted'))
      .catch(error => {
    console.error(error);
  });
    }
    },
    mounted() {
        this.listHiredEmployee()
    }
    
}
</script>  