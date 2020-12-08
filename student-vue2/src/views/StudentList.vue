<template>
    <div >
        <input v-model="search"> 
        <div class="article"  v-for="student in student_list" :key="student.id"> 
            <div class="row">
                <div class="col-md-12">
                    <h2> <a>{{student.id}} </a></h2>
                    <a href="">{{student.name}}</a> </div>
            <hr>
        </div>
    </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
    name: 'student-list',
    data(){
        return {
            student_list:[],
            search:''
        }
    },
    watch:{
        search(){
            this.getList()
        }
    },
    mounted(){
        this.getList()
    },
    methods:{
        getList(){
            axios.get('/api/student/',{params:{search:this.search}}).then(respose => this.student_list=respose.data)
        }
    }
}
</script>

<style scoped>
.article{
    border: 1px solid rgba(0,0,0,.125);
    margin-top:20px;
    padding: 10px;
        
}
.article__title{
    margin:20px
}
.article__footter{
    margin:20px
}
.article__img{
    width:100%
}
</style>
