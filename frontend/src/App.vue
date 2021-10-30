<template>
  <div id="app">
    <div id ="nav">
      <h1 id="title">
       B-Kind
      </h1>
      <button type="button">
    <router-link to="/singup">サインアップ</router-link>
    </button>
      <button type="button">
    <router-link to="/">サインイン</router-link>
    </button>
      <button type="button">
    <router-link to="/singout">サインアウト</router-link>
    </button>
    </div>
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
  font-size:20px;
}
</style>
