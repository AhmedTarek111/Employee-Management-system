<template>
    <div class="container">
        <h2 class="mb-4">Department Details Details</h2>
            
        <table class="table table-bordered table-shadow">
          <thead class="thead-dark text-center">
            <tr>
              <th scope="col">Department Name</th>
              <th scope="col">Company Name</th>
              <th scope="col">Number of Employees</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody class="text-center">
            <tr>
                <td>{{ departmentdetail.name }}</td>
                <td>{{ departmentdetail.company }}</td>
              <td>{{ departmentdetail.number_of_employees }}</td>
              <td>
                <router-link :to="{ path: '/department/update/' + this.Departmentid +'/'}">
                    <a href=""><i class="fa-regular fa-pen-to-square ms-3" ></i></a>
                  </router-link>
                  <a @click="deleteDepartment()"><i class="fa-solid fa-trash ms-4" style="color: red;"></i></a>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'DepartmentDetails',
    data() {
        return {
            Departmentid:this.$route.params.id,
            departmentdetail:''
        }
    },
    methods: {
        
    getDepartmentDetails() {
      axios({
        url: `http://127.0.0.1:8000/department/retrieve-destroy/${this.Departmentid}/`,
        method: 'get',
      }).then(response => {
        this.departmentdetail = response.data;
      });
    },
 
    deleteDepartment(){
      axios({
        url:`http://127.0.0.1:8000/department/retrieve-destroy/${this.Departmentid}/`,
        method:'delete',
      }).then((response) => {
      if (response.status === 204) { 
        this.$router.push('/department/list/'); 
        alert('The department has been deleted');
      } else {
        console.error('Error:', response.status);
        alert('Deletion failed. Please check the console for details.');
      }
    })
      .then(alert('The department has been deleted'))
      .catch(error => {
    console.error(error);
  });
    }
  },
  mounted() {
    this.getDepartmentDetails();
  },
    
   
}
</script>