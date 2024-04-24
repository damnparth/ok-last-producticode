<template>
     
     <form @submit.prevent="validateForm">
        <h1> Sign Up</h1>
        <label for="">username</label>
        <input type="username" required v-model="username">
        <label for="">password</label>
        <input type="password" requried v-model="password">
        <label for="">confirm password</label>
        <input type="password" required v-model="confirm">
        <br>

        
        
        <div v-if="passwordError" class="error">{{ passwordError }}</div>


        

        <br>
        <br>
        <br>
       <button class="button-login-signup" @click="validateForm">submit</button>
        <br>
        <br>
        <br>
    



        
        

       
    </form>
    
  
</template>

<script>
import axios from 'axios'





export default{
    data(){
        return{
            username:'',            
            password:'',
            confirm:'',
            passwordError:''
        }
    },
    methods:{
        validateForm(){
            let isValidated=true
            this.passwordError=this.password == this.confirm ? '': 'passwords do not match'





            if(isValidated)
                this.submitForm();
           
          

        
        },
        submitForm(){
            const userData = {
                username:this.username,
                password:this.password
                
            }
            axios.post('http://127.0.0.1:8000/apis/register',userData)
            .then(Response=>{
                setTimeout(() => {this.$router.push('/Login')}, 1500)
            })
            .catch(error=>{
                console.error(error.response.data);

            })
           

           

            
           
        }
       


    }
    

    }



</script>



<style>
form{
    max-width: 420px;
    margin: 30px auto;
    background:#B5C0D0;
    text-align: left;
    padding:40px;
    border-radius:20px;
    width: 400px;
    
    
    


}
label{
    display:flex;
    justify-content: center;
    align-items:center;
    color: black;
    display:inline block;
    margin:25px 0 15px;
    text-transform:uppercase;
    letter-spacing: 1px;
    font-weight:bold;
    
    



}
input{
    display:block;
    padding:10px 6px;
    width:300px;
    box-sizing:border-box;
    border:none;
    border-bottom: 1px  solid #ddd;
    color:#474545;
    border-radius: 10px;
    margin: auto;



}
h1{
    display:flex;
    justify-content: center;
    align-items: center;
    color: #2D3250;
}
.button-login-signup{
    display: flex;
    justify-content: center;
    align-items:center;
    border-radius:20px;
    height:50px;
    width:200px;
    margin:auto;
    padding:0;
    border:none;
    cursor:pointer;
    background-color: #2D3250;
    color:white;
    outline: 10cap;
    box-shadow: black;


}
body{
    background-color:#F5E8DD;
}
.error{
    display:flex;
    justify-content: center;
    align-items:center;
    color:red;
    
}




</style>