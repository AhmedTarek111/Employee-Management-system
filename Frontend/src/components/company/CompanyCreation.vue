<template>
    <div>
        <div class="container">
            <h2>Update Company</h2>
            <form @submit.prevent="createCompany">
                <div class="form-group">
                    <label for="name">Company Name</label>
                    <input type="text" class="form-control" id="name" required v-model="companyName">
                </div>
                <button type="submit" class="btn btn-primary">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'createcompany',
    data() {
        return {
            companyName: ''
        }
    },
    methods: {
        createCompany() {
            axios({
                url: 'http://127.0.0.1:8000/company/create/',
                method: 'post',
                data: {
                    name: this.companyName
                }
            }).then(response => {
                alert('Company Created successfully');
                this.$router.push('/company/list/');
            }).catch(error => {
                console.error('There was an error creating the company', error);
            });
        }
    },
}
</script>
