  var updateList = function(query){
      let q = $('#id_search').val()
      let offset = $('#my_div').children().length

      $.get('/api/student/',{search:q,offset}).done(function(data){
          console.log(data)
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
  $(document).on('scroll',updateList)

