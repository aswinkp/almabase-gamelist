<template>
  <div id="app">
    <nav class="navbar navbar-default">
    <div class="">
      <a class="navbar-brand" href="/"><img src="https://images.g2crowd.com/uploads/product/image/1473787046/almabase.png" alt="Almabase">
        </a>
      <ul class="nav navbar-nav">
        <li><a href="http://stackoverflow.com/cv/aswinkumar" target="black">SO CV</a></li>
        <li><a href="https://in.linkedin.com/in/aswin-kumar-kp" target="black">LinkedIn</a></li>
        <li><a href="https://github.com/aswinkp" target="black">Github</a></li>
        <li></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li v-if="!user.authenticated"><router-link to="login">Login</router-link></li>
        <li v-if="!user.authenticated"><router-link to="signup">Signup</router-link></li>
        <li v-if="user.authenticated" @click="logout()"><router-link to="login">Logout</router-link></li>
      </ul>
    </div>    
  </nav>
  <div class="">
    <router-view></router-view>
  </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<script>
import auth from './auth'

export default {
  data() {
    return {
      user: auth.user
    }
  },

  methods: {

    logout() {
      auth.logout()
    }
  }
}
</script>
