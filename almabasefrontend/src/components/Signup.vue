<template>
  <div class="col-sm-4 col-sm-offset-4">
     <div class="panel panel-success">
      <div class="panel-heading">
        <h3 class="panel-title">Sign Up</h3>
      </div>
      <div class="panel-body">
        <div class="alert alert-danger" v-if="error">
          <p v-if="error.description">{{ error.description }}</p>
          <p v-if="error.message">{{ error.response.data.message }}</p>
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your username" v-model="credentials.username">
        </div>
        <div class="form-group">
          <input type="password" class="form-control" placeholder="Enter your password" v-model="credentials.password">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your first_name" v-model="credentials.first_name">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your last_name" v-model="credentials.last_name">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your email_id" v-model="credentials.email_id">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your phone_no" v-model="credentials.phone_no">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your address" v-model="credentials.address">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Enter your ekryp_partner_id" v-model="credentials.ekryp_partner_id">
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
        email_id: '',
        phone_no: '',
        address: '',
        ekryp_partner_id: '',
        role_id: 1

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
        email_id: this.credentials.email_id,
        phone_no: this.credentials.phone_no,
        address: this.credentials.address,
        ekryp_partner_id: this.credentials.ekryp_partner_id,
        role_id: this.credentials.role_id
      }

      auth.signup(this, credentials, 'login')
    }
  }
}
</script>