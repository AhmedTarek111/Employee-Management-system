<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <div class="list-company"> <h2>List of Companies</h2> 
      
     <div class="container">
      <table class="table table-success table-striped table-bordered">
        <thead>
          <tr>
            <th scope="col"><i class="dot fa-solid fa-circle"></i></th>
            <th scope="col">Name</th>
            <th scope="col">Number of Department</th>
            <th scope="col">Number of Employee</th>
          </tr>
        </thead>
        <tbody >
          <tr v-for="company in companies">
            <th scope="row"><i class="dot fa-solid fa-circle"></i></th>
            <td>{{ company.name }}</td>
            <td>{{ company.number_of_departments }}</td>
            <td>{{ company.number_of_employees }}</td>
          </tr>
         
        </tbody>
      </table>
     </div>
      
    </div>
  </template>
  
  <style scoped>
  .dot {
    font-size: 7px;
   }
  </style>

  <script>
  import axios from 'axios';
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
    }
  }
}

  </script>
  