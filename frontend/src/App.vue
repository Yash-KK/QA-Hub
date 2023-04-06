<template>
  <nav>
    <navbar-component></navbar-component>
  </nav>  
  <router-view/>
</template>


<script>
import axios from 'axios';
import NavbarComponent from './components/NavbarComponent.vue';

  export default {
    components: {
      NavbarComponent
    },

    methods: {
      getUserCredentials(){
        let endpoint = '/auth/users/me/';
        axios.get(endpoint)
        .then(response =>{        
          window.localStorage.setItem('username',response.data.username);
        })
        .catch(error=>console.log(error));
      }
    },

    created(){
      this.getUserCredentials();
    }
  }

</script>

<style>
body {
  font-family: "Noto Sans JP", sans-serif;
  font-weight: 400;
}
</style>
