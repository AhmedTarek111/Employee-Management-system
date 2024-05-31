<template>
    <div class="container">
      <h2>Employee Details</h2>
      <table class="table table-striped mt-5">
        <thead class="text-center">
          <tr>
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
          <tr >
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
            <td>
                <router-link :to="{ path: '/department/update/' + this.Departmentid +'/'}">
                    <a href=""><i class="fa-regular fa-pen-to-square ms-3" ></i></a>
                  </router-link>
                  <a @click="deleteEmployee()"><i class="fa-solid fa-trash ms-4" style="color: red;"></i></a>
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
            employeeId:this.$route.params.id,
            employee:''
        }
    },
    methods: {
        getEmployeeDetails(){
            axios({
                url:`http://127.0.0.1:8000/employee/retrieve-destroy/${this.employeeId}/`,
                method:'get',

            }).then(response => this.employee = response.data)
        },
        deleteEmployee(){
      axios({
        url:`http://127.0.0.1:8000/employee/retrieve-destroy/${this.employeeId}/`,
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
        this.getEmployeeDetails()
    }
    
}
</script>  