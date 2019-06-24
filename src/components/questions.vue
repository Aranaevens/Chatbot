<template>
<div>
  <div
    v-for="intitule in choices"
    v-bind:key="intitule.node_id"
    class="intitule"
    id="questions"
    >
    <div class="box">{{ intitule.node_question }}</div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default{
  name: "questions",
  data() {
    return {
      choices: null,
    }
  },
  mounted: function(){
    this.getChildren(1);
  },
  methods: {
    getChildren: function(id){
      let app = this;
      axios
        .get("/api/node/" + id + "/get_children")
        .then(response => {
          app.choices = response.data;
      })
    }
  },
  // components: {
  //   questions
  // }
}
</script>


