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

      function GetIndtrumentsp2p1()
    {
        var symbolp2p1 =$("#p2p1symbol_one").val();
       $('#p2p1resultsymbolone').html('');
       if(symbolp2p1.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p2p1symbol_one').val();
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
                       $('#p2p1resultsymbolone').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p2p1resultsymbolone').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p2p1symbol_one').val($.trim(click_text[0]));
        $('#instrument_token_p2p1').val($.trim(click_text[3]));
        $("#p2p1resultsymbolone").html('');
       });
    }

      function GetIndtrumentsp2p1_two()
    {
        var symbolp2p1_two =$("#p2p1symbol_two").val();
       $('#p2p1resultsymboltwo').html('');
       if(symbolp2p1_two.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p2p1symbol_two').val();
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
                       $('#p2p1resultsymboltwo').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p2p1resultsymboltwo').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p2p1symbol_two').val($.trim(click_text[0]));
        $('#instrument_token_p2p1_two').val($.trim(click_text[3]));
        $("#p2p1resultsymboltwo").html('');
       });
    }
       function GetIndtrumentsp2minusp1()
    {
        var symbolp2minusp1 =$("#p1minusp2symbol_one").val();
       $('#p1minusp2resultsymbolone').html('');
       if(symbolp2minusp1.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p1minusp2symbol_one').val();
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
                       $('#p1minusp2resultsymbolone').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p1minusp2resultsymbolone').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p1minusp2symbol_one').val($.trim(click_text[0]));
        $('#instrument_token_p2minusp1_one').val($.trim(click_text[3]));
        $("#p1minusp2resultsymbolone").html('');
       });
    }

          function GetIndtrumentsp2minusp1_two()
    {
        var symbolp2minusp1_two =$("#p1minusp2symbol_two").val();
       $('#p1minusp2resultsymboltwo').html('');
       if(symbolp2minusp1_two.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p1minusp2symbol_two').val();
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
                       $('#p1minusp2resultsymboltwo').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p1minusp2resultsymboltwo').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p1minusp2symbol_two').val($.trim(click_text[0]));
        $('#instrument_token_p2minusp1_two').val($.trim(click_text[3]));
        $("#p1minusp2resultsymboltwo").html('');
       });
    }



       function GetIndtrumentsp2plusp1()
    {
        var symbolp2twop1 =$("#p1plusp2symbol_one").val();
       $('#p1twop2resultsymbolone').html('');
       if(symbolp2twop1.length<3)
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
                       $('#p1twop2resultsymbolone').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p1twop2resultsymbolone').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p1plusp2symbol_one').val($.trim(click_text[0]));
        $('#instrument_token_p2twop1_one').val($.trim(click_text[3]));
        $("#p1twop2resultsymbolone").html('');
       });
    }


       function GetIndtrumentsp2plusp1_two()
    {
        var symbolp2plusp1_two =$("#p1plusp2symbol_two").val();
       $('#p1plusp2resultsymboltwo').html('');
       if(symbolp2plusp1_two.length<3)
       {
           return false;
       }
       
       var apiEndpoint="http://127.0.0.1:8000/instruments/?symbolName="+$('#p1plusp2symbol_two').val();
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
                       $('#p1plusp2resultsymboltwo').append('<li class="list-group-item link-class"> '+data[0].tradingsymbol+' | <span class="text-muted">'+data[0].exchange+'</span>  | <span class="text-muted">'+data[0].name+'</span> | <span style="display:none;">'+data[0].instrument_token+'</span></li>');   

                 });
                 
                 
                 
             } 
             else{
                 
                 alert('no data found');
             }
         }
           
           
       });
       
       $('#p1plusp2resultsymboltwo').on('click', 'li', function() {
        var click_text = $(this).text().split('|');
        $('#p1plusp2symbol_two').val($.trim(click_text[0]));
        $('#instrument_token_p2plusp1_two').val($.trim(click_text[3]));
        $("#p1plusp2resultsymboltwo").html('');
       });
    }



   $('#symbol').keyup(function(){
       GetIndtruments();
   }) ;
    
    $('#p2p1symbol_one').keyup(function(){
       GetIndtrumentsp2p1();
   }) ;

     $('#p2p1symbol_two').keyup(function(){
       GetIndtrumentsp2p1_two();
   }) ;
     $('#p1minusp2symbol_one').keyup(function(){
       GetIndtrumentsp2minusp1();
   }) ;

      $('#p1minusp2symbol_two').keyup(function(){
       GetIndtrumentsp2minusp1_two();
   }) ;

       $('#p1plusp2symbol_one').keyup(function(){
       GetIndtrumentsp2plusp1();
   }) ;

      $('#p1plusp2symbol_two').keyup(function(){
       GetIndtrumentsp2plusp1_two();
   }) ;
    
});