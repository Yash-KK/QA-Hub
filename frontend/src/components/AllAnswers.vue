<template>
    <div>
        <p class="text-muted">
            <strong>{{ answer.author }} :{{ answer.created_at }}</strong>
        </p>
        <p style="white-space: pre-wrap;">{{ answer.body }}</p>         
        <hr>
         
    </div>
</template>

<script>
    export default {
        props: ['answer']
    }
</script>