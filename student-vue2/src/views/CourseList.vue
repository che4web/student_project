<template lang="pug">
div
    h2 Список предметов  
        .row
            .col-6
                input(class="form-control my-class" v-model="search")
                input(v-model="num" placeholder="число студентов") 
            .col-6
                course-form(@input="course_list.push($event)")
        .article(  v-for="item in course_list" :key="item.id")
            .row
                .col-md-12
                    h2
                        a {{item.id}} 
                    course-form( :value="item")
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import CourseForm from "@/components/CourseForm"

export default {
    name: 'item-list',
    data(){
        return {
            course_list:[],
            search:'',
            num:''
        }
    },
    components:{CourseForm},
    watch:{
        search(){
            this.getList()
        },
        num(){
            this.getList()
        }
    },
    mounted(){
        this.getList()
    },
    methods:{
        getList(){
            axios.get('/api/course/',{params:{search:this.search,student_num:this.num}})
                .then(respose => this.course_list=respose.data)
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

.my-class.form-control{
    width:50%
}
</style>
