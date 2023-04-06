<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
        <router-link class="navbar-brand" :to="{name:'home'}">QuestionTime</router-link>
        <!-- <a class="navbar-brand" href="#">QuestionTime</a> -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto">           
              
                <li>
                    <router-link :to="{name: 'question-editor'}" class="btn btn-outline-danger"  href="/accounts/logout/">Ask Question</router-link>
                </li>  

                <li>
                    <a style="margin-left: 5px;" class="btn btn-outline-secondary" href="/accounts/logout/">Logout</a>
                </li>  
            </ul>
        </div>
    </div>
    </nav>
</template>


<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}
.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>