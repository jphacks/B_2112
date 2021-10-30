<template>
  <div>
    <h1>SING UP</h1>
    <div>
      <h3>E-mail</h3>
      <input type='text' placeholder='E-mail' v-model='email' />
    </div>
    <div>
      <h3>Password</h3>
      <input type='password' placeholder='Password' v-model='password' />
    </div>
    <button @click='createUserAccount'>Sing UP!!</button>
  </div>
</template>

<script>
import axios from 'axios'
import firebase from '../firebase.js'
const URL = 'http://127.0.0.1:5000/'
export default {
  name: 'singup',
  data () {
    return {
      email: '',
      password: '',
      name: ''
    }
  },
  methods: {
    createUserAccount () {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(() => {
          alert('Create Account')
          var params = new FormData()
          this.name = this.email.substring(0, this.email.indexOf('@'))
          params.append('name', this.name)
          axios.post(`${URL}api/createdb`, params)
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              alert(error)
            })
          this.$router.push('/')
        })
        .catch(error => {
          alert('Error!', error.message)
          console.error('Account Regeister Error', error.message)
        })
    }
  }
}
</script>
