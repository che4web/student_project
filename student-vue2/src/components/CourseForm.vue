<template >
<div>
    <input @input="save" class="form-controls" v-model="course.name">
    <button class="btn btn-primary" v-on:click="save">сохранить существуюй</button>
    <button class="btn btn-primary" v-on:click="saveNew">сохранить новый</button>
</div>

</template>
<script>
import axios from 'axios'
export default {
    name:'course-form',
    props:['value'],
    data(){
        return{
            course:{name:''}
        }
    },
    watch:{
        value(value){
            this.course=value
        }
    },
    mounted(){
        this.course = this.value
    },
    methods:{
        save(){
            let promis 
            if(this.course.id){
                promis = axios.patch('/api/course/'+this.course.id+'/',this.course)
            }else{
                promis =axios.post('/api/course/',this.course)
            }
            promis.then( response => {
                this.course=response.data
                this.$emit('input',this.course)
            })
        },
        saveNew(){
            let obj = this.course
            obj.id = undefined
            let promis =axios.post('/api/course/',obj)
            promis.then( response => this.course=response.data)

        }
    }
}
</script>
