$(document).ready(function(){
    
    $("#exchange").change(function(){
        GetIndtruments();        
    });
    
    function GetIndtruments()
    {
        var symbol =$("#symbol").val();
       $('#result').html('');
       if(symbol.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#symbol').val();
       if($("#exchange")[0].selectedIndex>0)
       {
           apiEndpoint=apiEndpoint+"&exchange="+$("#exchange").val();
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
        $('#symbol').val($.trim(click_text[0]));
        $('#instrument_token').val($.trim(click_text[3]));
        $("#result").html('');
       });
    }
    
   $('#symbol').keyup(function(){
       GetIndtruments();
   }) ;
    
    
});