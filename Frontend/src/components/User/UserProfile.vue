<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="d-flex d-flex justify-content-between align-items-center mb-3">
                <h2 class="text-center mb-4">Profile Details</h2>
                <router-link to="/user/edit/" type="button" class="btn btn-secondary p-2 ">Edit</router-link>
              </div>
          <ul class="list-group">
            <li class="list-group-item d-flex justify-content-between align-items-center">
              Username:
              <span>{{ user.user.username }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              Email:
              <span>{{ user.user.email }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              Role:
              <span>{{ user.user.role }}</span>
              
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'UserProfileUpdate',
    data() {
      return {
        user: ''
      };
    },
    methods: {
      getUser() {
        axios({
          url: 'http://127.0.0.1:8000/accounts/retrive-update/',
          method: 'get'
        })
        .then(response => {
          this.user = response.data
          console.log( response.data)
        })
        .catch(error => {
          console.error('Error fetching user data:', error);
        })
      }
    },
    mounted() {
      this.getUser()
    }
  };
  </script>
  