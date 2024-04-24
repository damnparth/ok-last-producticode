<template>
  <div class="homepage">

  <div class="navbar">
    <div class="container-fluid">
      <h2>ProductiCode</h2>

    </div>
    <div class="navbar-left">
      <button class="login"><router-link to="/Profile" style="color:white; text-decoration: none;font-weight: bold;">Profile</router-link></button>

      
      
      <br>
      <br>
    </div>
    <div class="navbar-right">
      
      <button class="login"> <router-link  to="/SignUp" style="color:white; text-decoration: none; font-weight: bold;">SignUp</router-link></button>

      <button class="login"><router-link to="/Login" style="color:white; text-decoration: none;font-weight: bold;">Login</router-link></button>
     
    </div>
    

  </div>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <img src="../assets/vue-img.jpeg" alt="">
  
  <div class="dashboard">
    <h1>Dashboard</h1>
    <h4>Important Tip: Studying computer science in college means juggling coursework, side projects, internships, and more. Use this template to help you get organized and stay on top of your school to-dos.</h4>
    <br>
  </div> 
  <br>
  
  <div class="container">
    <div class="grid1">
      <div class="quick-access"><h1>Quick Access</h1>
        <div class="quick-access-pill"><h4>GitHub</h4> <a href="https://github.com/" style="color: white;">www.github.com</a></div>
        <div class="quick-access-pill"><h4>LinkedIn</h4> <a href="https://www.linkedin.com/" style="color:white">www.linkedin.com</a></div>
        <div class="quick-access-pill"><h4>LeetCode</h4><a href="https://leetcode.com/" style="color:white;">www.leetcode.com</a></div>


      </div>
      <div class="habit-tracker">
  <h1>To Do List</h1>
  {{ date }}
  <input style="width:auto" type="text" required v-model="entry" @keyup.enter="addList" placeholder="enter task">
  <ul>
    <li v-for="(todo, index) in skills" :key="index" class="">
      
      <div class="">
        <Checkbox v-model="checked" :binary="true" />
    </div>
     
      <span class="pill">{{ todo }}</span>
      <i class="bi bi-trash-fill" style="color: black;" @click="deleteList"></i>
    </li>
  </ul>
</div>

      <div class="clock"><h1>calendar</h1>

        <div class="mwah">
          
        <Calendar v-model="date" inline showWeek />
    </div>
       
        
  
        
    

      </div>
    
      
    </div>
    <br>

    <div class="internship">
      <h1>Summer internship</h1>
      <div class="card flex justify-content-center">
        <Calendar v-model="date" />
    </div>
      

      

      
    </div>
    <br>
    <h1>Courses</h1>

    <div class="grid2">
     
      <br>
      <div class="maths4"><h3>  Mathematics 4</h3> <div class="moodle">  <a href="http://moodle.apsit.org.in/moodle/" style="color: white; text-align: center;">Notes</a>   </div>  <br> <div class="moodle" style="text-decoration: underline;color: white;"> <a href="https://youtu.be/T4bE0K14QLU?si=pGGb6ZnlmJNbnWT7" style="color: white;" >Resources</a></div></div>
      <div class="os"><h3>Operating Systems</h3> <div class="moodle">  <a href="http://moodle.apsit.org.in/moodle/" style="color: white; text-align: center;">Notes</a>   </div>  <br> <div class="moodle" style="text-decoration: underline;color: white;"> <a href="https://youtu.be/bkSWJJZNgf8?si=-KqZ83AtAxwF3_-G" style="color: white;">Resources</a></div></div>
      <div class="dbms"><h3>DBMS</h3><div class="moodle">  <a href="http://moodle.apsit.org.in/moodle/" style="color: white; text-align: center;">Notes</a>   </div>  <br> <div class="moodle" style="text-decoration: underline;color: white;">  <a href="https://youtu.be/kBdlM6hNDAE?si=SfJBcYnaZntcuYTO" style="color: white;"> Resources</a></div></div>
      <div class="aoa"><h3>Analysis of Algorithms</h3><div class="moodle">  <a href="http://moodle.apsit.org.in/moodle/" style="color: white; text-align: center;">Notes</a>   </div>  <br> <div class="moodle" style="text-decoration: underline;color: white;">  <a href="https://youtu.be/u8JZ9gU5o4g?si=Y8TQlLCvE5btpXxT" style="color: white;">Resources</a></div></div>
      <div class="mp"><h3>Microprocessor</h3><div class="moodle">  <a href="http://moodle.apsit.org.in/moodle/" style="color: white; text-align: center;">Notes</a>   </div>  <br> <div class="moodle" style="text-decoration: underline;color: white;"> <a href="https://youtu.be/nVumL1rZ768?si=zngsGC_3HanlYnyB" style="color: white;">Resources</a></div></div>
      


      

      
      
    </div>
    <br>
    <div class="homework">
      <h1>Homework</h1>
      <div class="lip">
        <br>
        <div class="d-flex mt-5">


        <input v-model="task" type="text" placeholder="enter assignment" class="w-100 form-control" @keyup.enter="addAssignment">
        
        
        </div>
        <div class="card">
          
          
          <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Table</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <table class="table">
    
    <thead>
      <tr>
        <th scope="col">Task</th>
        <th scope="col">Status</th>
        <th scope="col" class="text-center">#</th>
        <th scope="col" class="text-center"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(task,index) in tasks" :key="index">
        <th>{{ task.name }}</th>
        <td @click="changeStatus(index)" class="pointer">{{ task.status }}</td>
        <div class="text-center" @click="deleteAssignment">
        <td><i class="bi bi-trash-fill" style="color: black;"></i></td>
        </div>
        <td></td>
      </tr>
     </tbody>
  </table>
</body>
</html>

          
        
        </div>
        
        
                 

        
       
        

      </div>

      
    </div>
    <div class="code-snippets">
      <h1>code snippets</h1>
      <div class="card-flex-justify-content-center">
        <FloatLabel class="grid2">
            <Textarea class="snippet" v-model="value" rows="5" cols="30" />
          
            <Textarea class="snippet" v-model="value" rows="5" cols="30" />
            <Textarea class="snippet" v-model="value" rows="5" cols="30" />


            
        </FloatLabel>
    </div>
      
      
   
   

      



    </div>
    <br>

    


  </div>
  
  

  
 
  


  </div>
</template>

<script>

import Checkbox from 'primevue/checkbox';

import Textarea from 'primevue/textarea';


import Calendar from 'primevue/calendar';






export default {
  name: 'HomeView',
  components: 
  {
    Checkbox,
    Calendar,
    Textarea,
    
  
  
  

  
    
  },
  data(){
    return{
     
      ToDoList:'',
      skills: [],
      entry:'',
      task:'',
      tasks:[
        {
          name:"MP assignment",
          status:'todo'
        },
        {
          name:'DBMS exp12 upload',
          status:'in-progress'

        }
      ],
      availableStatus:['to-do','in progress','done'],
      date: null,
      

      

  
    }
    
  },
  methods:{
    addList(){
      
      

      if(this.skills.length<5){
        this.skills.push(this.entry)
      this.entry = ""
      }
      else
      alert('you can only enter 5 tasks for the day')
      

     
      
    },
    deleteList(index){
      this.skills.splice(index,1)

    },
    strikeList(index){
     
      this.skills[index].completed=!this.skills[index].completed

    },
    addAssignment(){
      if(this.task.length===0)return;
      this.tasks.push({
        name: this.task,
        status:'to-do'
      })

     

    },
    deleteAssignment(index){
      this.tasks.splice(index,1)

    },
    changeStatus(index){
      let newStatus = this.availableStatus.indexOf(this.tasks[index].status);
      if(++newStatus>2) newStatus =0;
      this.tasks[index].status= this.availableStatus[newStatus];

    }

    

  }
}

</script>


<style scoped>


*{
  
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.navbar{
  display:flex;
  background-color: #EED3D9;
  padding:10px;
  text-align: right;
}
.navbar-left{
  display:flex;
  margin:auto;
  justify-content: left ;
  align-items: left;
  cursor:pointer;
  
}
.navbar-right{
  display:flex;
  cursor:pointer;

  
  
}
img{
  display: block;
    object-fit: cover;
    border-radius: 0px;
    width: 100%;
    height: 30vh;
    opacity: 1;
    object-position: center;
    height: 250px;
}
.dashboard{
  border-radius:15px;
  background-color: #CCD3CA;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
margin:auto;
margin-left:20px;
margin-right:20px;
}
.grid1{
  display:flex;
  justify-content: space-evenly;
  height:370px;
  

  


}
.quick-access{
  border-radius: 15px;
  width: 300px;
  
  background-color:#CCD3CA

}
.habit-tracker{
  border-radius:15px;
  width:300px;
  
  background-color: #CCD3CA;

}
.clock{
  border-radius:15px;
  width:300px;
  
  
  background-color: #CCD3CA;
  cursor: pointer;

}
.internship{
  background-color: #CCD3CA;
  width:500px;
  border-radius:15px;
  margin:auto;
  height:150px;
  


  
}
.grid2{
  display:flex;
  justify-content: space-evenly;
  height:200px;
  
  
  

}
.maths4{
  border-radius: 15px;
  background-color: #CCD3CA;
  width: 200px;

}
.mp{
  border-radius: 15px;
  background-color: #CCD3CA;

  width:200px;
}
.os{
  border-radius: 15px;
  background-color: #CCD3CA;
  width:200px;

}
.dbms{
  border-radius: 15px;
  background-color: #CCD3CA;
  width:200px;

}
.aoa{
  border-radius: 15px;
  background-color: #CCD3CA;
  width: 220px;
  
}
router-link{
  color:black;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
img{
  height: 300px;

}
input[type='ToDoList']{
  background-color: #EED3D9;
  width: 200px;
height: 30px;

}
.login{
  width: 100px;
  color:white;
  justify-content: space-evenly;
  margin:5%;
  
    
   
    border-radius:20px;
    height:50px;
  
   
    padding:0;
    border:none;
    cursor:pointer;
    background-color: #2D3250;
    color:white;
    outline: 10cap;
    box-shadow: black;
  

}
.quick-access-pill{
  border-radius:15px;
  height: 70px;
  background-color: #2D3250;
  color: white;
  margin-left: 10%;
  text-align: center;
  justify-content: center;
  
  margin-right: 10%;
  

  
 

}
.moodle{
  border-radius: 15px;
  height: 45px;
  width: 180px;
  background-color: #2D3250;
  cursor: pointer;
  margin-left: 10%;
  margin-right: 10%;
  margin: auto;
  
}
.pill{
  list-style-type: none;
  
  width: 100px;
  border-radius: 15px;
  background-color: gray;
  height: auto;
  color: white;
  height: 30px;
  margin-bottom: 5%;
 


}
li{
 display: inline-block;
 margin-right: auto;
  
}
.completed{
  text-decoration: line-through;
}
.lip{
  border-radius: 20px;
  background-color: #CCD3CA;
  width: 1000px;
  height: 500px;
  margin:auto;
 
 
  


}
.snippet{
  border-radius: 10px;
  background-color: #F2F1EB;

}
.card-flex-justify-content-center{
  
  




}
.table {
  border-collapse: collapse;
  width: 100%;
  max-width: 600px;
}

.table th,
.table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.table th {
  background-color: #f2f2f2;
}

.table tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}
.card{
  justify-content: center;
  align-items: center;
  margin: auto;
  display: flex;
  margin-top: 2%;
}
.pointer{
  cursor: pointer;
}
.mwah{
  
  width: 210px;
  height:250px;
  border-radius: 20px;
  background-color: #F2F1EB;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto;
  
}
ul{
  list-style: none;
  padding: 0;
  margin: 0;
}



</style>
