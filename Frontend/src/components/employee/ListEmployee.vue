<template>
    <div class="container">
      <div class="d-flex d-flex justify-content-between align-items-center mb-3">
        <h2 class="my-5"> List Employee</h2>
        <router-link to="/employee/create/" type="button" class="btn btn-success p-2 ">Add Employee</router-link>
      </div>
      <table class="table table-secondary  table-striped table-bordered">
        <thead class="text-center">
          <tr>
            <th scope="col"><i class="dot fa-solid fa-circle"></i></th>
            <th scope="col">Name</th>
            <th scope="col">Details</th>
           


          </tr>
        </thead>
        <tbody class="text-center">
          <tr v-for="employee in employees">
            <th scope="row"><i class="dot fa-solid fa-circle"></i></th>
            <td>{{ employee.name}}</td>
            <td>
              <router-link :to="`/employee/detail/${employee.id}/`" style="color: black;">
                <i class="fa-solid fa-circle-info"></i>
              </router-link>
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
  