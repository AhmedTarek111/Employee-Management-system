<template>
  <div class="mb-5">
      <nav class="navbar bg-dark border-bottom border-body d-flex justify-content-start" data-bs-theme="dark">
        <router-link to="/" class="btn btn-light ms-5">home </router-link>
        <router-link to="/user/profile/" class="btn btn-light ms-2">Profile  </router-link>
        <div class="container-md d-flex justify-content-center">  <router-link class="navbar-brand" to="/">Employee Management System </router-link>
        </div>
      </nav>
    </div>
    
</template>

<script>
  export default {
      name:'navbar',

  }
</script>