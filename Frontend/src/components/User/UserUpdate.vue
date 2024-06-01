<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <h2 class="text-center mb-4">Update Profile</h2>
          <form @submit.prevent="handleSubmit" v-if="user">
            <div class="form-group mb-3">
              <label for="username">Username</label>
              <input type="text" class="form-control" id="username" v-model="user.username" required>
            </div>
            <div class="form-group mb-3">
              <label for="email">Email</label>
              <input type="email" class="form-control" id="email" v-model="user.email" required>
            </div>
            <div class="form-group mb-4">
              <label for="role">Role</label>
              <select class="form-control" id="role" v-model="user.role" required>
                <option value="Admin">Admin</option>
                <option value="Manager">Manager</option>
                <option value="Employee">Employee</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary w-100">Update Profile</button>
          </form>
          <p v-else>loading ...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'UserProfileUpdate',
    data() {
      return {
        user: {
            username:'',
            role:'',
            email:'',
        }
      };
    },
    methods: {
      async getUser() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/accounts/retrieve/');
          this.user = response.data;
        } catch (error) {
          console.error('Error fetching user data:', error);
        }
      },
      async handleSubmit() {
        try {
          const response = await axios.put(`http://127.0.0.1:8000/accounts/update/${this.user.id}/`, this.user);
          console.log('User updated successfully:', response.data);
          this.$router.push('/user/profile/');
        } catch (error) {
          console.error('Error updating user:', error);
        }
      },
    },
    mounted() {
      this.getUser();
    },
  };
  </script>
  