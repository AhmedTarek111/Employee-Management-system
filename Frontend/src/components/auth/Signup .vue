<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Register</h2>
        <form @submit.prevent="handleSignup">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" v-model="user.username" required>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" v-model="user.email" required>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model="user.password" required>
          </div>
          <div class="mb-4">
            <label for="role" class="form-label">Role</label>
            <select class="form-select" id="role" v-model="user.role" required>
              <option value="Admin">Admin</option>
              <option value="Manager">Manager</option>
              <option value="Employee">Employee</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary w-100">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
        role: ''
      }
    };
  },
  methods: {
    ...mapActions(['registerUser']),
    handleSignup() {
      this.registerUser(this.user)
        .then(() => {
          this.$router.push('/login');
        })
        .catch(err => {
          console.error('Registration error:', err);
          alert('Registration failed. Please try again.');
        });
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}
</style>
