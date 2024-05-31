<!-- src/components/Login.vue -->
<template>
    <div class="container">
      <h2>Login</h2>
      <form @submit.prevent="login" class="form">
        <div class="form-group">
          <label for="username">Username or Email:</label>
          <input type="text" id="username" v-model="username" required class="form-control">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required class="form-control">
        </div>
        <p class="d-flex justify-content-center">
          <router-link to="/signup/" class="link-offset-2 link-underline link-underline-opacity-25" href="#">Sign up</router-link>
        </p>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    name: 'Login',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      ...mapActions(['loginUser']),
      login() {
        const credentials = {
          username: this.username,
          password: this.password,
        };
        this.loginUser(credentials)
          .then(() => {
            this.$router.push('/');
          })
          .catch(error => {
            console.error('Error logging in:', error);
            alert('Login failed. Please check your credentials.');
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
  }
  .form-group {
    margin-bottom: 15px;
  }
  .btn {
    width: 100%;
  }
  </style>
  