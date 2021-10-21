$(document).ready(function(){
    
    $("#exchange").change(function(){
        Getp2p1oneIndtruments();        
    });
    
    function Getp2p1oneIndtruments()
    {
        var symbol =$("#p1plusp2symbol_one").val();
       $('#p1plusp2resultsymbolone').html('');
       if(symbol.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p1plusp2symbol_one').val();
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
                       $('#p1plusp2resultsymbolone').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p1plusp2resultsymbolone').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p1plusp2symbol_one').val($.trim(click_text[0]));
//        $('#p2p1instrument_token').val($.trim(click_text[3]));
        $("#p1plusp2resultsymbolone").html('');
       });
    }
    
   $('#p1plusp2symbol_one').keyup(function(){
       Getp2p1oneIndtruments();
   }) ;
    
    
});