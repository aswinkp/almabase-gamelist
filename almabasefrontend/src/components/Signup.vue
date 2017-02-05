<template>
  <div class="col-sm-4 col-sm-offset-4">
     <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Sign Up</h3>
      </div>
      <div class="panel-body">
        <div class="alert alert-danger" v-if="error">
          <p v-if="error.description">{{ error.description }}</p>
          <p v-if="error.message">{{ error.response.data.message }}</p>
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your UserName" v-model="credentials.username">
        </div>
        <div class="form-group">
          <input type="password" class="form-control" placeholder="Enter your Password" v-model="credentials.password">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your FirstName" v-model="credentials.first_name">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your Last Name" v-model="credentials.last_name">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your Email" v-model="credentials.email">
        </div>
        <button class="btn btn-primary" @click="submit()">SignUp</button>
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
        password: '',
        first_name: '',
        last_name: '',
        email: ''
      },
      error: ''
    }
  },

  methods: {

    submit() {

      var credentials = {
        username: this.credentials.username,
        password: this.credentials.password,
        first_name: this.credentials.first_name,
        last_name: this.credentials.last_name,
        email: this.credentials.email
      }

      auth.signup(this, credentials, 'login')
    }
  }
}
</script>