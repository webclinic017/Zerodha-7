$(document).ready(function(){
    
    var user_id= $('#user_id').val();
    
    $.ajax({
        
      url:'',
      type:'post',
      data:{user_id=user_id},
      dataType:'json',
      contentType: "application/json",
      success:function(response){
          
             var len= response.length;
              
               $("#trigger_name").empty();
                for( var i = 0; i<len; i++){
                    var triggername = response[i]['triggername'];
                    
                    $("#trigger_name").append("<option value='"+triggername+"'>"+triggername+"</option>");

                }

      }    
        
    });  
    
});