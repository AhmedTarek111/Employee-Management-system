<template>
    <div class="container" >
        <h2 class="text-center my-5 ">Welcome</h2>
        <div class="d-flex justify-content-center">
            <div class="shadow-lg card text-center  bg-primary-subtle me-4" style="width: 18rem; ">
                <div class="card-body p-4">
                  <h5 class="card-title">Company Management</h5>
                  <router-link to="/company/list" class="btn btn-primary mt-3">Go somewhere</router-link>
                </div>
              </div>
            
            <div class="shadow-lg card text-center  bg-success-subtle me-4 " style="width: 18rem; ">
                <div class="card-body p-4">
                  <h5 class="card-title">Department Management</h5>
                  <router-link to="/department/list/" class="btn btn-success mt-3">Go somewhere</router-link>
                </div>
              </div>
            
            <div class="shadow-lg card text-center  bg-info-subtle me-4" style="width: 18rem; ">
                <div class="card-body p-4">
                  <h5 class="card-title">Employee Management</h5>
                  <router-link to="/employee/list/" class="btn btn-info mt-3">Go somewhere</router-link>
                </div>
              </div>
            
              
        </div>

    </div>
</template>

<script>

export default {
    name:'HomePage',
}
</script>