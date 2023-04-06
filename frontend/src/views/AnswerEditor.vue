<template>
    <div class="container">
        <form @submit.prevent="submitForm">
            <textarea  v-model="answerBody" class="form-control" rows="4"></textarea>
            <button type="submit" style="margin-top: 5px;" class="btn btn-success">Update</button>
        </form>
    </div>
</template>


<script>
import axios from 'axios';


// import axios from 'axios';
    export default {
        props: ['id'],
        data(){
            return {
                answerBody: ''
            }
        },
        methods: {
            submitForm(){
                if(this.answerBody){
                   let endpoint = `/answers/${this.id}/`;

                   axios.defaults.xsrfCookieName = 'csrftoken'; 
                   axios.defaults.xsrfHeaderName = 'X-CSRFToken'; 
                   axios.put(endpoint,{
                    body: this.answerBody
                   })                   
                   .then(response =>{                    
                    this.$router.push({
                        name: 'question',
                        params: {
                            slug: response.data.question_slug
                        }                       
                    })
                   })
                } else{
                    alert("Empty answer can't be published")
                }
            }
        },

        beforeRouteEnter(to, from,next){
            let endpoint = `/answers/${to.params.id}/`
            
            axios.get(endpoint)
            .then(response=>{             
                next(vm => vm.answerBody = response.data.body);
            })
            
        }
    }
</script>
