<template>
  <div class="col-sm-4 col-sm-offset-4">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Log In</h3>
      </div>
      <div class="panel-body">
        <p>Log in to your account</p>
        <div class="alert alert-danger" v-if="error">
          <p v-if="error.message">{{ error.response.data.non_field_errors[0] }}</p>
        </div>
        <div class="form-group">
          <input  type="text"  class="form-control" placeholder="Enter your username" v-model="credentials.username">
        </div>
        <div class="form-group">
          <input type="password" class="form-control" placeholder="Enter your password" v-model="credentials.password">
        </div>
        <button class="btn btn-primary" @click="submit()">Login</button>
      </div>
    </div>
    
  </div>
</template>

<script>
import auth from '../auth'

export default {

  data() {
    return {
      credentials: {
        username: '',
        password: ''
      },
      error: ''
    }
  },

  methods: {

    submit() {
      var credentials = {
        username: this.credentials.username,
        password: this.credentials.password
      }

      auth.login(this, credentials, 'home')

    }
  }
  
}
</script>