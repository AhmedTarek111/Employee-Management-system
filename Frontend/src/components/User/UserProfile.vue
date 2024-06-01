<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="d-flex d-flex justify-content-between align-items-center mb-3">
            <h2 class="text-center mb-4">Profile Details</h2>
            <router-link to="/user/edit/" type="button" class="btn btn-secondary p-2">Edit</router-link>
          </div>
          <ul class="list-group" v-if="user">
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <span>Username:</span>
              <span>{{ user.user.username }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <span>Email:</span>
              <span>{{ user.user.email }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <span>Role:</span>
              <span>{{ user.user.role }}</span>
            </li>
          </ul>
          <p v-else>Loading user data...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserProfileUpdate',
    data() {
      return {
        user: null, // Initialize user as null to avoid errors
      };
    },
    methods: {
      getUser() {
        axios({
          url: 'http://127.0.0.1:8000/accounts/retrive-update/',
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
      this.getUser();
    },
  };
  </script>
  