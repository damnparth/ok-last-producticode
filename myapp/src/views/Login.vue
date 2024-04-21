<template>
    <form>
        <h1> Login</h1>
        <label for="">email</label>
        <input type="email" required v-model="email">
        <label for="">password</label>
        <input type="password" requried v-model="password">
        <br>
        <br>
        <br>
        <button class="button-login-signup"><router-link to="/" style="color: white; text-decoration: none;">submit</router-link></button>
        <br>
        <br>
        <br>
        
        <br>

    </form>

</template>

<script>
export default {
    data(){
        return{
            email:'',
            password:''

        }
        
    }

}
</script>

<style>

</style>