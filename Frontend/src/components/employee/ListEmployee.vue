<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />  
    <div class="container">
      <h2 class="my-5"> List Employee</h2>
      <table class="table table-secondary  table-striped table-bordered">
        <thead>
          <tr>
            <th scope="col"><i class="dot fa-solid fa-circle"></i></th>
            <th scope="col">Company</th>
            <th scope="col">Department</th>
            <th scope="col">Status</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Address</th>
            <th scope="col">Designation</th>
            <th scope="col">Hired On</th>
            <th scope="col">Days Employed</th>
            <th scope="col">details</th>
            <th scope="col">Modifications</th>


          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees">
            <th scope="row"><i class="dot fa-solid fa-circle"></i></th>
            <td>{{ employee.company}}</td>
            <td>{{ employee.department}}</td>
            <td>{{ employee.status}}</td>
            <td>{{ employee.name}}</td>
            <td>{{ employee.email}}</td>
            <td>{{ employee.mobile_number}}</td>
            <td>{{ employee.address}}</td>
            <td>{{ employee.designation}}</td>
            <td v-if="employee.status == 'Hired'">{{ employee.hired_on}}</td>
            <td v-else>Not Hired </td>
            <td v-if="employee.status == 'Hired'">{{ employee.days_employed}}</td>
            <td v-else>Not Hired </td>
            <td>
              <router-link  to="/employee/details/" style="color: black;"><i class="fa-solid fa-circle-info "></i></router-link>
            </td>
            <td>
              <router-link to="/employee/edit/"><i class="fa-regular fa-pen-to-square ms-3" ></i></router-link>
              <a @click="deleteemployee(department.id)"><i class="fa-solid fa-trash ms-4" style="color: red;"></i></a>
            </td>
          
            
          </tr>
         
        </tbody>
      </table>
    </div>
  </template>
  
  <style scoped>
  .dot {
    font-size: 7px;
   }
  </style>

  <script>
  import axios from 'axios';
  import { useRouter } from 'vue-router';

  export default {
    name: 'Listemployee', 
    data() {
      return {
        employees: '' 
      };
    },
    mounted() {
      this.listemployees()
    },
    methods:{

      listemployees(){
            axios({
                url:'http://127.0.0.1:8000/employee/list/',
                method:'get',
            }).then(response => this.employees = response.data)
    },
    
    deleteemployee(id){
      axios({
        url:'http://127.0.0.1:8000/employee/retrieve-destroy/'+id+'/',
        method:'delete',
      }).then(alert('The employee has been deleted'))
      .catch(error => {
    console.error(error);
  });
    }
    
  }
}

  </script>
  