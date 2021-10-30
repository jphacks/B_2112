<template>
    <div>
        <p>Home page</p>
        <p>Random number from backend: {{ randomNumber }}</p>
        <button @click="getRandom">New random number</button>
    </div>
</template>

<script>
import axios from 'axios'
const URL = 'http://127.0.0.1:5000/'

export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  method: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      // const path = `http//localhost:5000/api/random`
      axios.get(`${URL}api/random`)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  create () {
    this.getRandom()
  }
}
</script>
