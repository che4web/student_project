  var updateList = function(query){
      $.get('/api/student/').done(function(data){
          console.log(data)
          $('my_div').empty('')
          for(let item of data){
              $('#my_div').append( `<div class="article" id="" >
                                        <div class="row ">
                                            <div class="col-md-12" >
                                                <h2> <a >${item.id} </a>
                                                <a href="">${item.name} </a></h2></div>
                                        </div>
                                        <hr>
                                    </div>
`)
          }
      })
    }
  $('#my_button').click(updateList)

