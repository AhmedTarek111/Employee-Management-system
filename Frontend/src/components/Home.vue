<template>
  <div class="container">
    <h2 class="text-center my-5">Welcome {{user.username}}</h2>
    <h2 class="text-center my-5">Available Option for {{user.role}}</h2>
    <div class="row d-flex justify-content-center">

      <div class="col-lg-4 col-md-6 col-sm-12 shadow-lg card text-center bg-primary-subtle me-4" style="width: 18rem;" v-if="['Admin'].includes(user.role)">
        <div class="card-body p-4">
          <h5 class="card-title">Company Management</h5>
          <router-link to="/company/list" class="btn btn-primary mt-3">Check</router-link>
        </div>
      </div>

      <div class="col-lg-4 col-md-6 col-sm-12 shadow-lg card text-center bg-success-subtle me-4" style="max-width: 19rem;" v-if="['Admin', 'Manager'].includes(user.role)">
        <div class="card-body p-4">
          <h5 class="card-title">Department Management</h5>
          <router-link to="/department/list/" class="btn btn-success mt-3">Check</router-link>
        </div>
      </div>

      <div class="col-lg-4 col-md-6 col-sm-12 shadow-lg card text-center bg-info-subtle me-4" style="width: 18rem;" v-if="['Admin', 'Manager','Employee'].includes(user.role)">
        <div class="card-body p-4">
          <h5 class="card-title">Employee Management</h5>
          <router-link to="/employee/list/" class="btn btn-info mt-3">Check</router-link>
        </div>
      </div>

    </div>
   <div class="container">
    <div class="row d-flex justify-content-center mt-3">
      <div class="col-lg-4 col-md-6 col-sm-12 shadow-lg card text-center bg-primary-subtle me-4" style="width: 18rem;" v-if="['Admin', 'Manager'].includes(user.role)">
        <div class="card-body p-4">
          <h5 class="card-title">Hired Employee</h5>
          <router-link to="/employee/hired/" class="btn btn-primary mt-3">Check</router-link>
        </div>
      </div>
      <div></div>
      <div></div>
    </div>
   </div>
  </div>
</template>


<script>
import axios from 'axios';
export default {
    name:'HomePage',
    data() {
      return {
        user:''
      }
    },
    methods: {
      getUser() {
        axios({
          url: 'http://127.0.0.1:8000/accounts/retrieve/',
          method: 'get',
        })
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error('Error fetching user data:', error);
        });
      },
    },
    mounted() {
      this.getUser()
    },
}
</script>