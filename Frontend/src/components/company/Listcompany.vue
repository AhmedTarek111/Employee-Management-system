<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  
  <div class="container">
    <div class="d-flex d-flex justify-content-between align-items-center mb-3">
      <h2 class="my-5"> List Company</h2>
      <router-link to="/company/create/" type="button" class="btn btn-success p-2 ">Add Company</router-link>
    </div>
    <table class="table table-success table-striped table-bordered ">
        <thead>
          <tr class="text-center">
            <th scope="col"><i class="dot fa-solid fa-circle"></i></th>
            <th scope="col">Name</th>
        
            <th  scope="col">details</th>
          </tr>
        </thead>
        <tbody >
          <tr v-for="company in companies" class="text-center">
            <th scope="row"><i class="dot fa-solid fa-circle"></i></th>
            <td>{{ company.name }}</td>
           
            <td >
              <router-link :to="`/company/detail/${company.id}/`" style="color: black;"><i class="fa-solid fa-circle-info"></i></router-link>
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
    name: 'ListCompany', 
    data() {
      return {
        companies: '' 
      };
    },
    mounted() {
      this.listCompany()
    },
    methods:{

      listCompany(){
            axios({
                url:'http://127.0.0.1:8000/company/list/',
                method:'get',
            }).then(response => this.companies = response.data)
    },
    
    deleteCompany(id){
      axios({
        url:'http://127.0.0.1:8000/company/retrieve-destroy/'+id+'/',
        method:'delete',
      }).then(alert('The company has been deleted'))
      .catch(error => {
    console.error(error);
  });
    }
    
  }
}

  </script>
  