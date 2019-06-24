<template>
  <div id="app">
    <chat
      :feed="feed"
      v-on:onEmit="onEmit"/>
  </div>
</template>

<script>
import chat from './components/chat'

export default {
  name: 'App',
  data: function(){
    return {
      feed: [],
    }
  },
  components: {
    chat
  },
  methods: {
    onEmit(value){
      this.feed.push(value);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
