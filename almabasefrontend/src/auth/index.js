import {router} from '../main'
import Vue from 'vue'

import axios from 'axios'

export default {
  urls: {
    SITE_URL: "http://localhost:8000/",
  },
  user: {
    authenticated: false
  },

  login(context, creds, redirect) {
    var self=this;
    axios.post(this.urls.SITE_URL+'login/', creds).then(function (response) {
      localStorage.setItem('access_token', response.data.token);
      axios.defaults.headers.common['Authorization'] = self.getAuthHeaderToSend();
      self.user.authenticated = true
      if(redirect) {
          context.$router.push(redirect)        
      }
    })
    .catch(function (err) {
      context.error = err
    });
  },

  signup(context, creds, redirect) {
    var self=this;
    axios.post(this.urls.SITE_URL+ 'signup', creds).then(function (response) {
      if(redirect) {
          context.$router.push(redirect)        
      }
    })
    .catch(function (err) {
      context.error = err
    });
  },

  logout() {
    localStorage.removeItem('access_token')
    this.user.authenticated = false
  },

  checkAuth() {
    var jwt = localStorage.getItem('access_token')
    if(jwt) {
      this.user.authenticated = true
    }
    else {
      this.user.authenticated = false      
    }
  },
  matched: function(name) {
    return this.$route.name == name;
  },
  getAuthHeader() {
    return  localStorage.getItem('access_token')
  },

  getAuthHeaderToSend() {
  return  "JWT "+localStorage.getItem('access_token')
  }
}
