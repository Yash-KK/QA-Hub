<template>
    <div class="container mt-3">
        <div v-if="question">
            <h1>{{ question.content }}</h1>
            
            <p class="mb-0">
                Posted by:
                <span class="author-name">{{ question.author }}</span>
            </p>
            <p>{{ question.created_at }}</p>

            <router-link v-if="loggedUser == question.author" :to="{name: 'question-editor', params: {slug:question.slug}}" class="btn btn-warning btn-sm">Edit</router-link>
            <p style="color: green;" v-if="userHasAnswered">You have answered...</p>
            <div v-else>
                <button @click="showForm=!showForm" class="btn btn-success" >Answer the Question</button>
            </div>
            <hr>
            <div v-if="showForm">
                <form @submit.prevent="submitForm">
                    <textarea v-model="answerBody" class="form-control" rows="4"></textarea>
                    <button style="margin-top: 5px;" type="submit" class="btn btn-success">Publish Answer</button>
                </form>
            </div>
        </div>
        <div v-else>
            <h1 class="error text-center">404- Question Not Found!</h1>
        </div>       
       
        <div v-if="answers">
            <all-answers v-for="answer in answers"
            :key="answer.pk"
            :answer="answer">
            </all-answers>
        </div>
      
        <div class="my-4">
            <button v-show="next" @click="getAnswers" class="btn btn-sm btm-outline-success">
            Load More</button>
        </div>
    </div>
     
 </template>

<script>
import axios from 'axios';
import AllAnswers from '@/components/AllAnswers.vue';

    export default {
        props: ['slug'],
        components: {
            AllAnswers
        },
        data(){
            return {
                question: '',
                answers: [],
                next: null,
                userHasAnswered: false,
                showForm: false,

                answerBody: '',
                loggedUser:''
            }
        },
        methods: {
            setTitle(){
                document.title = this.question.slug
            },
            getQuestionData(){
                let endpoint = `/questions/${this.slug}/`;
                axios.get(endpoint)
                .then(response=>{         
                    if (response.data.answer_count){
                        this.getAnswers();
                    }
                    this.userHasAnswered = response.data.user_has_answered;                  
                    this.question = response.data;
                    this.setTitle();


                   this.loggedUser = window.localStorage.getItem('username');
                   


                })
                .catch(error =>console.log(error))
            },

            getAnswers(){
                let endpoint = `/questions/${this.slug}/answers/`;
                if(this.next){
                    endpoint = this.next
                }
                axios.get(endpoint)
                .then(response =>{
                
                    for(let i=0; i<response.data.results.length; i++){
                        this.answers.push(response.data.results[i]);
                    }
                   
                    if(response.data.next){
                        this.next = response.data.next
                    } else{
                        this.next = null
                    }
                    
                })
                .catch(error => console.log(error));
            },

            submitForm(){
                if(this.answerBody){
                    let endpoint = `/questions/${this.slug}/answer-create/`;
                    axios.defaults.xsrfCookieName = 'csrftoken'; 
                    axios.defaults.xsrfHeaderName = 'X-CSRFToken'; 
                    axios.post(endpoint,{
                        body: this.answerBody
                    })
                    .then(response =>{                        
                        this.answers.unshift(response.data);
                        this.userHasAnswered = true;
                        this.showForm = false;

                    })
                    .catch(error => console.log(error));
                } else{
                    alert("Do not submit an empty form!")
                }
            }
        },

        created(){
            this.getQuestionData();
        }
      
    }

</script>