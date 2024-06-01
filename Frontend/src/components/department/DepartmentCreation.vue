<template>
    <div>
        <div class="container">
            <h2>Create Department</h2>
            <form @submit.prevent="createdepartment" class="form">
                <div class="form-group">
                    <label for="name">Department Name</label>
                    <input type="text" class="form-control" id="name" required v-model="department.name">
                </div>
                <div class="form-group">
                    <label for="department">Company:</label>
                    <select id="department" v-model="department.company" @click="listcompany()" required class="form-control">
                      <option value="">Select Department</option>
                      <option v-for="company in listCompany" :key="company.id" :value="company.id">{{ company.name }}</option>
                    </select>
                  </div>
                <button type="submit" class="btn btn-primary">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'createdepartment',
    data() {
        return {
            department: {
                name:'',
                company:''
            },
            listCompany:[]
        }
    },
    methods: {
        listcompany(){
            axios({
                url:'http://127.0.0.1:8000/company/list/',
                method:'get',
            }).then(response => this.listCompany = response.data)
    },
        createdepartment() {
            axios({
                url: 'http://127.0.0.1:8000/department/create/',
                method: 'post',
                data: this.department
                    
            }).then(response => {
                alert('Department Created successfully');
                this.$router.push('/department/list/');
            }).catch(error => {
                console.error('There was an error creating the department', error);
            });
        }
    },
    mounted() {
        this.listcompany()
    },
}
</script>
