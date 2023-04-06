<template>
  <div class="home">
      <div class="container">
        <div v-for="question in questions" :key="question.pk">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Posted by:
              <span class="question-author">{{ question.author }}</span>
            </p>            
            
            <router-link :to="{name:'question', params: {slug: question.slug}}"  class="question-link">
                <h2>{{ question.content }}</h2>          
            </router-link>
               
           
            <p class="mb-0">
              <span style="color: black;" >Answers:</span>  {{ question.answer_count }}
            </p>
          </div>          
        </div>
      </div>
      <div class="my-4">
      <button  v-show="next" @click="getQuestions" class="btn btn-sm btm-outline-success">
      Load More</button>
    </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';
  export default {
  
    data(){
      return {
        questions: [],
        next: null
      }
    },
    methods: {
      getQuestions(){
        let endpoint  = '/questions/';
        if(this.next){
          endpoint = this.next
        }
        axios.get(endpoint)
        .then(response=>{       
          for(let i=0; i<response.data.results.length; i++){
            this.questions.push(response.data.results[i]);
          }          
          
          if(response.data.next){
            this.next = response.data.next
          } else{
            this.next = null;
          }
        })
        .catch(error => console.log(error));
      }
    },


    created(){
      document.title = 'QA Hub'
      this.getQuestions();
    }
  
  }
</script>



<style>
.question-author {
  font-weight: bold;
  color: #dc3545;
}

.question-link{
  font-weight: 400;
  color: black;
  text-decoration: none;
}
.question-link:hover{
  color: #454545;
}
</style>