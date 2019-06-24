<template>
  <div id="chat">
    <div class="totheleft">
      <p>
        {{message}}
      </p>
    </div>
    <div class="totheright">
      <questions />
    </div>
    <div>{{ feed }}</div>
  </div>
</template>

<script>
import axios from 'axios'
import questions from './questions'

export default{
  name: "Chat",
  data() {
    return {
      message: null,
      choices: [],
      current_id: null,
    }
  },
  mounted: function(){
    this.getMessage(1);
    this.$emit('onEmit', "<chat />");
  },
  methods: {
    getMessage: function(id){
      let app = this;
      axios.get("/api/node/" + id).then(response => {
        app.message = response.data.node_text;
      });
    },

    onQuestionClick: function(value){

    }
  },
  components: {
    questions
  },
  props: {
    feed: Object,
  }
}
</script>


