$(document).ready(function(){
    
    $("#order_exchange").change(function(){
        Getorderinstruments();        
    });
    
    function Getorderinstruments()
    {
        var symbol =$("#order_symbol").val();
       $('#resultorderinstrument').html('');
       if(symbol.length<3)
       {
           return false;
       }
       
       var apiEndpoint="https://thealgotrade.in:8000/instruments/?symbolName="+$('#order_symbol').val();
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
                       $('#resultorderinstrument').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#resultorderinstrument').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#order_symbol').val($.trim(click_text[0]));
        // $('#instrument_token').val($.trim(click_text[3]));
        $("#resultorderinstrument").html('');
       });
    }
    
   $('#order_symbol').keyup(function(){
       Getorderinstruments();
   }) ;
    
    
});