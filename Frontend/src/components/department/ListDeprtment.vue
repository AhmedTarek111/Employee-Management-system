<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />      
  
    <div class="container">
      <h2 class="my-5"> List Departments</h2>
      <table class="table table-primary table-striped table-bordered">
        <thead>
          <tr>
            <th scope="col"><i class="dot fa-solid fa-circle"></i></th>
            <th scope="col">Company</th>
            <th scope="col">Name</th>
            <th scope="col">Number Of Employee</th>
            <th  scope="col">details</th>
            <th scope="col">Modifications</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="department in departments">
            <th scope="row"><i class="dot fa-solid fa-circle"></i></th>
            <td>{{ department.company}}</td>
            <td>{{ department.name}}</td>
            <td>{{ department.number_of_employees}}</td>
            <td >
              <router-link  to="/department/details/" style="color: black;"><i class="fa-solid fa-circle-info "></i></router-link>
            </td>
            <td>
              <router-link to="/department/edit/"><i class="fa-regular fa-pen-to-square ms-3" ></i></router-link>
              <a @click="deletedepartment(department.id)"><i class="fa-solid fa-trash ms-4" style="color: red;"></i></a>
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
    name: 'ListDepartment', 
    data() {
      return {
        departments: '' 
      };
    },
    mounted() {
      this.listdepartments()
    },
    methods:{

      listdepartments(){
            axios({
                url:'http://127.0.0.1:8000/department/list/',
                method:'get',
            }).then(response => this.departments = response.data)
    },
    
    deletedepartment(id){
      axios({
        url:'http://127.0.0.1:8000/department/retrieve-destroy/'+id+'/',
        method:'delete',
      }).then(alert('The departments has been deleted'))
      .catch(error => {
    console.error(error);
  });
    }
    
  }
}

  </script>
  