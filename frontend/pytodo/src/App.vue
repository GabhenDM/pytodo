<template>
  <div id="app">
    <Navbar/>
    <div>
      <b-jumbotron header="YATAP" id="jumbotron" lead="Yet Another Todo App in Python">
        <p>For more information visit website</p>
        <b-button variant="primary" href="#">More Info</b-button>
      </b-jumbotron>
    </div>
  </div>
</template>

<script>
import Navbar from './components/layout/Navbar.vue'
export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#jumbotron{ 
  background-color:#666666;
  color: white;
  }
  #jumbotron .btn-primary {
    background-color: #FE7F2D;
    color:white;
    border-color:#FE7F2D;
    border-radius:10px;
  }
  #jumbotron .btn-primary:hover {
    background-color: #B64A02;
    border-color: #B64A02
  }
html {
  background-color: #8F8F8F
}
</style>
