$(document).ready(function(){
    
    $("#group_exchange").change(function(){
        GetIndtruments();   
        alert("group exchange");     
    });
    
    function GetIndtruments()
    {
        var group_symbol =$("#group_symbol").val();
       $('#result').html('');
       if(group_symbol.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#group_symbol').val();
       if($("#group_exchange")[0].selectedIndex>0)
       {
           apiEndpoint=apiEndpoint+"&exchange="+$("#group_exchange").val();
       }
       
       $.ajax({
           
        url:apiEndpoint,
        method:"GET",
        dataType: 'json',
        contentType: "application/json",
         success:function(result){          
             
               if(result.status=="success"){
                  $.each(result.content, function (index,data) {   
                       $('#result').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span>'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#result').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#group_symbol').val($.trim(click_text[0]));
        $('#group_instrument_token').val($.trim(click_text[3]));
        $("#result").html('');
       });
    }
    
   $('#group_symbol').keyup(function(){
       GetIndtruments();
   }) ;
    
    
});