<template>
    <div>
      <div class="container">
        <h2>Update  Company</h2>
        <form @submit.prevent="companyUpdate">
          <div class="form-group">
            <label for="name">Company Name</label>
            <input type="text" class="form-control" id="name" required v-model="name">
          </div>
          <button type="submit" class="btn btn-primary">Update Company</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'UpdateCompany',
    data() {
      return {
        Companyid: this.$route.params.id,
        name: ''
      };
    },
    methods: {
      getCompanyDetails() {
        axios({
          url: `http://127.0.0.1:8000/company/retrieve-destroy/${this.Companyid}/`,
          method: 'get',
        }).then(response => {
          this.name = response.data.name;
        }).catch(error => {
          console.error('There was an error retrieving the company details:', error);
        });
      },
      companyUpdate() {
        axios({
          url: `http://127.0.0.1:8000/company/update/${this.Companyid}/`,
          method: 'put',
          data: {
            'name': this.name
          }
        }).then(response => {
          alert('Company updated successfully!');
          this.$router.push(`/company/detail/${this.Companyid}/`);
        }).catch(error => {
          console.error('There was an error updating the company:', error);
        });
      }
    },
    mounted() {
      this.getCompanyDetails();
    },
  }
  </script>
  
  <style>

  </style>
  