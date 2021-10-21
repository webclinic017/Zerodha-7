$(document).ready(function(){
    
    $("#order_exchange").change(function(){
        GetIndtruments();        
    });
    
    function GetIndtruments()
    {
        var symbol =$("#order_symbol").val();
       $('#result').html('');
       if(symbol.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#order_symbol').val();
       if($("#order_exchange")[0].selectedIndex>0)
       {
           apiEndpoint=apiEndpoint+"&exchange="+$("#order_exchange").val();
       }
       
       $.ajax({
           
        url:apiEndpoint,
        method:"GET",
        dataType: 'json', 
        contentType: "application/json",
         success:function(result){          
             
               if(result.status=="success"){
                  $.each(result.content, function (index,data) {   
                       $('#result').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       }); 
       
       $('#result').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#order_symbol').val($.trim(click_text[0]));
        $('#instrument_token').val($.trim(click_text[3]));
        $("#result").html('');
       });
    }




     $('#order_symbol').keyup(function(){
       GetIndtruments();
   }) ;

       });