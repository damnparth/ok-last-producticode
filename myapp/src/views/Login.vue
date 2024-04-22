<template>
    <form>
        <h1> Login</h1>
        <label for="">username</label>
        <input type="username" required v-model="username">
        <label for="passText">password</label>
        <input type="password" requried v-model="passText">
        <br>
        <br>
        <br>
        <button class="button-login-signup" @click="validateForm">submit</button>
        <br>
        <br>
        <br>
        
        <br>

    </form>

</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            username:'',
            passText:''

        }
        
    },
    methods:
    {
        validateForm(){
            let isValidated=true
            const fields=[
                {'username':this.username},
                {'passText':this.passText}
            ]
            if(isValidated)
            this.submitForm();


        
        },
        submitForm(){
            axios.post('http://127.0.0.1:8000/apis/login',{
                username:this.username,
                passText:this.passText
            })
            .then(response=>{
                const user={
                    'username':response.data.username,

                }
                setTimeout(()=>{this.$router.push('/')})
            })



        }









    }

}
</script>

<style>

</style>