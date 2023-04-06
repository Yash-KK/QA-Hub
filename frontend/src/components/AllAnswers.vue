<template>
    <div>
        <p class="text-muted">
            <strong>{{ answer.author }} :{{ answer.created_at }}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{ answer.body }}</p>        

        
        <router-link :to="{name:'answer-editor', params: {id: answer.id }}" v-if="loggedUser === answer.author" class="btn btn-outline-secondary btn-sm">Edit</router-link>   
        <button @click="deleteAnswer" v-if="loggedUser === answer.author" style="margin-left: 5px;" class="btn btn-outline-danger btn-sm" >Delete</button>
        <br>
        <button style="margin-top: 5px;" type="button" class="btn"
            @click="toggleLike"
            :class="{
            'btn-warning': userHasLikedAnswer,
            'btn-outline-danger': !userHasLikedAnswer,
            }">
            Like Answer&nbsp;
            <span class="badge bg-danger">{{ likesCount }}</span>
         </button> 
       <hr>
         
    </div>
</template>

<script>
import axios from 'axios';
    export default {
        props: ['answer', 'loggedUser'],
        data(){
            return {
                userHasLikedAnswer: this.answer.user_has_liked,
                likesCount: this.answer.likes_count
            }
        },
        methods: {
            toggleLike(){
            this.userHasLikedAnswer === false ? this.likeAnswer() : this.unlikeAnswer();
            },

            deleteAnswer(){
                let endpoint = `/answers/${this.answer.id}/`
                axios.defaults.xsrfCookieName = 'csrftoken'; 
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'; 
                axios.delete(endpoint)
                .then(response=>{
                    console.log(response);
                    this.$router.push({
                        name: 'home'                        
                    })
                })
            },

            likeAnswer(){
                this.userHasLikedAnswer = true;
                this.likesCount +=1;
                let endpoint = `/answers/${this.answer.id}/like/`
                axios.defaults.xsrfCookieName = 'csrftoken'; 
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'; 
                try{
                    axios.post(endpoint)
                } catch(error){
                    console.log(error);
                }
            },

            unlikeAnswer(){
                this.userHasLikedAnswer = false;
                this.likesCount -=1;
                let endpoint = `/answers/${this.answer.id}/like/`
                axios.defaults.xsrfCookieName = 'csrftoken'; 
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'; 
                try{
                    axios.delete(endpoint)
                } catch(error){
                    console.log(error);
                }
            }
        }

    }
</script>