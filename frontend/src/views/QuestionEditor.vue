<template>
    <div class="container">
        <form @submit.prevent="submitForm">
            <textarea v-model="questionBody" class="form-control" rows="4"></textarea>
            <button style="margin-top: 10px;" class="btn btn-success">Publish</button>
        </form>
    </div>
</template>


<script>
import axios from 'axios';
    export default {
        props: ['slug'],
        data(){
            return {                
                questionBody: '',               
                
            }
        },

        methods: {
            callAxios(){
                if(this.questionBody){
                    let endpoint = `/questions/`;
                    axios.defaults.xsrfCookieName = 'csrftoken'; 
                    axios.defaults.xsrfHeaderName = 'X-CSRFToken';  
                    if(this.slug !== '' || this.slug !== undefined){
                        endpoint += `${this.slug}/`
                        axios.put(endpoint, {
                            content: this.questionBody
                        })
                        .then(response =>{
                            this.$router.push(
                                {
                                    name: 'question',
                                    params: {
                                        slug: response.data.slug
                                    }
                                }                                
                            )
                        })
                    } else{
                        axios.post(endpoint,{
                        content: this.questionBody
                        })
                        .then(response =>{
                            console.log(response)
                            this.$router.push({ name: 'home' });                      
                        })
                        .catch(error => console.log(error));
                    }              

                } else{
                    alert("Your question hasn't been written yet, so it can't be published")
                }
            },
            submitForm(){
                this.callAxios();
            }
        },
        created(){
            document.title = 'Ask Question'
        },

        beforeRouteEnter(to,from,next){
            if(to.params.slug == '' || to.params.slug == undefined){                           
                return next();
            } else{
                let endpoint = `/questions/${to.params.slug}/`
                axios.get(endpoint)
                .then(response=>{
                    return next(vm => vm.questionBody = response.data.content);
                })
                .catch(error => console.log(error));               
            }
        }
    }

</script>