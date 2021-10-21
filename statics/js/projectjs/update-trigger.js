

    $(function () {
        $("#select_trigger").change(function () {
            if ($(this).val() == "1") {
                $("#price-con").show();
                $("#price-am").show();
                $("#symbolcontainer").show();
            } else {
                $("#price-con").hide();
                 $("#price-am").hide();
            }
            
            if ($(this).val() == "2") {
                $("#moving_average").show();
                $("#moving_average_one").show();
                $("#moving_average_two").show();
                $("#moving_average_time_frame").show();
                $("#moving_average_type").show();
                $("#moving_average_period").show();
                $("#moving_average_field").show();
                $("#price-am-one").hide();
                $("#price-am-two").hide();
                $("#symbolcontainer").show();
                
            } else {
                $("#moving_average").hide();
                 $("#moving_average_one").hide();
                $("#moving_average_two").hide();
                $("#moving_average_time_frame").hide();
                $("#moving_average_type").hide();
                $("#moving_average_period").hide();
                $("#moving_average_field").hide();
                 
            }
            
            if ($(this).val() == "3") {
                $("#volume_con").show();
                $("#volume_con_time_frame").show();
                $("#symbolcontainer").show();
            } else {
                $("#volume_con").hide();
                 $("#volume_con_time_frame").hide();
            }
            
             if ($(this).val() == "6") {
                $("#rsi_con").show();
                $("#rsi_amount").show();
                $("#rsi_con_one").show();
                $("#rsi_time_frame").show();
                $("#rsi_period").show();
                $("#rsi_con_two").show();
                $("#symbolcontainer").show();
                
            } else {
               $("#rsi_con").hide();
                $("#rsi_amount").hide();
                $("#rsi_con_one").hide();
                $("#rsi_time_frame").hide();
                $("#rsi_period").hide();
                $("#rsi_con_two").hide();
            }
            
//            if ($(this).val() == "parabolic_sar") {
//                $("#parabolic_sar_con").show();
//                $("#parabolic_sar_con_one").show();
//                $("#parabolic_sar_con_two").show();
//                $("#parabolic_sar_time_frame").show();
//                $("#parabolic_sar_time_frame_one").show();
//                $("#parabolic_sar_time_frame_two").show();
//            } else {
//                $("#parabolic_sar_con").hide();
//                $("#parabolic_sar_con_one").hide();
//                $("#parabolic_sar_con_two").hide();
//                $("#parabolic_sar_time_frame").hide();
//                $("#parabolic_sar_time_frame_one").hide();
//                $("#parabolic_sar_time_frame_two").hide();
//            }
            
             if ($(this).val() == "4") {
                $("#p_con").show();
                $("#p_amount").show();
                $("#p_con_one").show();
                $("#p_con_two").show();
                $("#p_symbol_one").show();
                $("#p_symbol_two").show();
                $("#symbolcontainer").hide();
            } else {
                $("#p_con").hide();
                $("#p_amount").hide();
                $("#p_con_one").hide();
                $("#p_con_two").hide();
                $("#p_symbol_one").hide();
                $("#p_symbol_two").hide();
                // $("#symbolcontainer").show();
            }

            if($(this).val() == "7"){
                
                $("#p1minusp2_con").show();
                $("#p1minusp2_conone").show();
                $("#p1minusp2_confour").show();
                $("#p1minusp2_symbol_one").show();
                $("#p1minusp2_symbol_two").show();
                $("#symbolcontainer").hide();
            }else{
                $("#p1minusp2_con").hide();
                $("#p1minusp2_conone").hide();
                $("#p1minusp2_contwo").hide();
                $("#p1minusp2_conthree").hide();
                $("#p1minusp2_confour").hide();
                $("#p1minusp2_symbol_one").hide();
                $("#p1minusp2_symbol_two").hide();
                // $("#symbolcontainer").show();
                
            }
            
            if($(this).val() == "8"){
                
                $("#p1plusp2_con").show();
                $("#p1plusp2_conone").show();
                $("#p1plusp2_confour").show();
                $("#p1plusp2_symbol_one").show();
                $("#p1plusp2_symbol_two").show();
                $("#symbolcontainer").hide();
            }else{
                $("#p1plusp2_con").hide();
                $("#p1plusp2_conone").hide();
                $("#p1plusp2_confour").hide();
                $("#p1plusp2_contwo").hide();
                $("#p1plusp2_conthree").hide();
                $("#p1plusp2_symbol_one").hide();
                $("#p1plusp2_symbol_two").hide();
                // $("#symbolcontainer").show();
                
            }
            
            if ($(this).val() == "5") {
                $("#trigger_con").show();
                $("#trigger_con_one").show();
                $("#trigger_con_two").show();
                $("#symbolcontainer").show();
            } else {
                $("#trigger_con").hide();
                $("#trigger_con_one").hide();
                $("#trigger_con_two").hide();
            }
                   
            
        });
    });


  
function submitbtn()
{
alert('Button Clcked');
}






    $(function () {
        $("#mv_option").change(function () {
            
            if ($(this).val() == "MA") {
                $("#ma_con").show();
                $("#ma_con_one").show();
//                $("#ma_con_two").show();
            } else {
               $("#ma_con").hide();
                $("#ma_con_one").hide();
                $("#ma_con_two").hide();
            }
            
            if ($(this).val() == "(P-MA/MA)") {
                $("#pa_ma_con").show();
                $("#pa_ma_con_one").show();
//                $("#pa_ma_con_two").show();
            } else {
               $("#pa_ma_con").hide();
                $("#pa_ma_con_one").hide();
//                $("#pa_ma_con_two").hide();
            }
            
            if ($(this).val() == "MA avg") {
                $("#ma_avg_con").show();
                $("#ma_avg_con_one").show();
                $("#ma_avg_con_two").show();
                $("#pa_ma_con_two").hide();
            } else {
                $("#ma_avg_con").hide();
                $("#ma_avg_con_one").hide();
                $("#ma_avg_con_two").hide();
            }
            
            if ($(this).val() == "P-MA/MA avg") {
                $("#p_ma_ma_con").show();
                $("#p_ma_ma_con_one").show();
                $("#p_ma_ma_con_two").show();
                $("#ma_avg_con_three").hide();
            } else {
              $("#p_ma_ma_con").hide();
                $("#p_ma_ma_con_one").hide();
                $("#p_ma_ma_con_two").hide();
            }
            
            
            
        });
        });

    $(function () {
        $("#selection_volume").change(function () {
        
           if ($(this).val() == "volume") {
                $("#volume_optioncon").show();
                $("#volume_optioncon_one").show();
                $("#volume_optioncon_two").show();
                $("#volume_avg_con_three").hide();
            } else {
              $("#volume_optioncon").hide();
                $("#volume_optioncon_one").hide();
                $("#volume_optioncon_two").hide();
            }
            
            if ($(this).val() == "volume_avg") {
                $("#volume_avg_con").show();
                $("#volume_avg_con_one").show();
                $("#volume_avg_con_two").show();
                $("#volume_optioncon_three").hide();
            } else {
              $("#volume_avg_con").hide();
                $("#volume_avg_con_one").hide();
                $("#volume_avg_con_two").hide();
            }
        });
        });

    $(function () {
        $("#select_parabolic").change(function () {
        
        if ($(this).val() == "parabolic_sar_sar") {
                $("#parabolic_saroption").show();
                $("#parabolic_saroption_one").show();
            } else {
              $("#parabolic_saroption").hide();
                $("#parabolic_saroption_one").hide();
            }
            
            if ($(this).val() == "parsar") {
                $("#parsar_con").show();
                $("#parsar_con_one").show();
            } else {
               $("#parsar_con").hide();
                $("#parsar_con_one").hide();
            }
        });
        });

 
  $(function () {
        $("#trigger_price_operator").change(function () {
            
            if($(this).val()=="6"){
                
                $("#price-am-one").show();
                $("#price-am-two").show();
                $("#price-am").hide();
                
            }
            else{
                
               $("#price-am-one").hide();
               $("#price-am-two").hide();
               $("#price-am").show();
                
            }
            
         });
        });
 

      $(function () {
        $("#trigger_ma_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#ma_con_two").show();
                $("#ma_con_three").show();
                $("#ma_con_one").hide();
               }else{
                
                $("#ma_con_two").hide();
                $("#ma_con_three").hide();
                $("#ma_con_one").show();
               }
            

        });
        });
 
      $(function () {
        $("#trigger_pma_pmaOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#pa_ma_con_one").hide();
                $("#pa_ma_con_two").show();
                $("#pa_ma_con_three").show();
            }else{
                
                $("#pa_ma_con_two").hide();
                $("#pa_ma_con_three").hide();
                $("#pa_ma_con_one").show();
            }
            

        });
        });
 


 
 
    $(function () {
        $("#trigger_maavg_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#ma_avg_con_three").show();
                $("#ma_avg_con_four").show();
                $("#ma_avg_con_two").hide();
                
            }else{
                
                $("#ma_avg_con_three").hide();
                $("#ma_avg_con_four").hide();
                $("#ma_avg_con_two").show();
                
                
            }
            

        });
        });
 
 
 
 
    $(function () {
        $("#p_ma_ma_avg_operator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#p_ma_ma_con_three").show();
                $("#p_ma_ma_con_four").show();
                $("#p_ma_ma_con_two").hide();
                
            }else{
                
                $("#p_ma_ma_con_three").hide();
                $("#p_ma_ma_con_four").hide();
                $("#p_ma_ma_con_two").show();
                
            }
            

        });
        });
 

 
 
    $(function () {
        $("#trigger_rsi_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#rsi_amount_two").show();
                $('#rsi_amount_three').show();
                $("#rsi_con_one").hide();
                
            }else{
                
                $("#rsi_amount_two").hide();
                $('#rsi_amount_three').hide();
                $('#rsi_amount_one').show();
                
            }
            

        });
        });
 

 
    $(function () {
        $("#trigger_p2p1_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#p_amount_two").show();
                $("#p_amount_three").show();
                $("#p_con_one").hide();
                
            }else{
                
                $("#p_amount_two").hide();
                $("#p_amount_three").hide();
                $("#p_con_one").show();
                
            }
            

        });
        });

 
 
    $(function () {
        $("#trigger_simplevolume_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
               $("#volume_optioncon_three").show();
               $("#volume_optioncon_four").show();
               $("#volume_optioncon_one").hide();
                
            }else{
                
                $("#volume_optioncon_three").hide();
                $("#volume_optioncon_four").hide();
                $("#volume_optioncon_one").show();
                
            }
            

        });
        });
 

 
 
    $(function () {
        $("#trigger_volumeavg_maOperator").change(function () {
            
            if($(this).val()=="6"){
               
                $("#volume_avg_con_three").show();
                $("#volume_avg_con_four").show();
               $("#volume_avg_con_two").hide();
                
            }else{
                
                $("#volume_avg_con_three").hide();
                $("#volume_avg_con_four").hide();
                $("#volume_avg_con_two").show();
            }
            

        });
        });
 
 
 
 
  $(function () {
      $("#trigger_p1minusp2_maOperator").change(function () {
          
          if($(this).val()=="6"){
             
              $("#p1minusp2_contwo").show();
              $("#p1minusp2_conthree").show();
             $("#p1minusp2_conone").hide();
              $("#p1minusp2_confour").hide();
              
          }else{
              
             $("#p1minusp2_contwo").hide();
             $("#p1minusp2_conthree").hide();
             $("#p1minusp2_conone").show();
              $("#p1minusp2_confour").show();
          }
          

      });
      });




  $(function () {
      $("#trigger_p1plusp2_maOperator").change(function () {
          
           if($(this).val()=="6"){
             
              $("#p1plusp2_contwo").show();
              $("#p1plusp2_conthree").show();
             $("#p1plusp2_conone").hide();
              $("#p1plusp2_confour").hide();
              
          }else{
              
             $("#p1plusp2_contwo").hide();
             $("#p1plusp2_conthree").hide();
             $("#p1plusp2_conone").show();
              $("#p1plusp2_confour").show();
          }
          

      });
      });



        
// var b = localStorage.getItem("myValue");
// alert("The Value Received is " + b);
// document.getElementById("rec").value = b;
// var resetValue =0;
// localStorage.setItem("myValue", resetValue);
  

$(document).ready(function(){

        $("#select_trigger").change(function(){
    
              
            var triggerCondition=$("#select_trigger").val();
            
            switch(triggerCondition){
                
                  case "1":    
                  PlacePrice();
                  break;
                  
                  case "2":
                  movingAverage();
                  break;
                  
                  case "3":
                  Volume();
                  break;
                  
                  case "4":
                  p2p1();
                  break;
                  
                  case "5":
                  trigger_placed();
                  break;
                  
                  case "6":
                  Rsi();
                  break;

                  case "7":
                  p1minusp2();
                  break;

                  case "8":
                  p1plusp2();
                  break;
                
                
            }
          
          
           
            //      placeprice trigger function start
          
                            function PlacePrice(){
                                alert("hello price");
                                $("#trigger_price_operator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_price_operator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allpriceoprtaormethod();
                                       break;
                                       
                                       case "2":    
                                       allpriceoprtaormethod();
                                       break;
                                       
                                       case "3":    
                                       allpriceoprtaormethod();
                                       break;
                                       
                                       case "4":    
                                       allpriceoprtaormethod();
                                       break;
                                       
                                       case "5":    
                                       allpriceoprtaormethod();
                                       break;

                                       case "6":
                                       betweenpriceoprtaormethod();
                                       break;
                                       
                                   }
                                   
                                   
                                    function allpriceoprtaormethod(){
                                        
                                         $('#placeorder').on('click', function(){
    
    
    
                          var trigger_name= $('#trigger_name').val();
                          var exchange= $('#exchange').val();
                          var symbol=$('#symbol').val();
                          var trigger_instrumenttoken=$('#instrument_token').val();
                          var trigger_condition=$('#select_trigger').val();
                          var trigger_price_operator=$('#trigger_price_operator').val();
                          var trigger_price_amount=$('#trigger_price_amount').val();
                          var trigger_id=$('#trigger_id').val();
                          alert(trigger_id+": test ");
  
                          
                           debugger;
                          if(trigger_name!=""){
    
    
                                  $.ajax({
    //                                              trigger_list/update/
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                      method:"POST",
                                      data:JSON.stringify({
                                      "trigger": {
                                      "trigger_name":trigger_name,
                                      "symbol":symbol,
                                      "trigger_condition_id": trigger_condition,
                                      "trigger_criteria":{"operator":trigger_price_operator, "amount":trigger_price_amount, "instrument_token":trigger_instrumenttoken},
                                      "exchange_id":exchange        
                              }}),
                                      dataType: "json",
                                      contentType: "application/json",
                                      success: function(result){
                                      if(result.status=="success")
                                      {
                                       alert(trigger_name + ' trigger and order created successfully');
                                       window.location.reload();
    
                                      }
                                  }
    
    
    
    
                                  });
    
                          }
                          else{
                                              alert('Please fill all the field !');
                                      }
    
    
    
    
                          }); 
                                        
                                    }
                                    
                                    
                                    
                                    function betweenpriceoprtaormethod(){
                                        
                                          $('#placeorder').on('click', function(){
    
    
    
                                       var trigger_name= $('#trigger_name').val();
                                       var exchange= $('#exchange').val();
                                       var symbol=$('#symbol').val();
                                       var trigger_instrumenttoken=$('#instrument_token').val();
                                       var trigger_condition=$('#select_trigger').val();
                                       var trigger_price_operator=$('#trigger_price_operator').val();
                                       var trigger_price_amount_one=$('#trigger_price_amount_one').val();
                                       var trigger_price_amount_two=$('#trigger_price_amount_two').val();
                         
                          
                        //   debugger;
                          if(trigger_name!=""){
    
    
                                  $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                      method:"POST",
                                      data:JSON.stringify({
                                        "trigger": {
                                      "trigger_name":trigger_name,
                                      "symbol":symbol,
                                      "trigger_condition_id": trigger_condition,
                                      "trigger_criteria":{"operator":trigger_price_operator, "from_amount":trigger_price_amount_one, "to_amount":trigger_price_amount_two, "instrument_token":trigger_instrumenttoken},
                                      "exchange_id":exchange        
                                  }}),
                                      dataType: "json",
                                      contentType: "application/json",
                                      success: function(result){
                                      if(result.status=="success")
                                      {
                                       alert(trigger_name + ' trigger and order created successfully');
                                       window.location.reload();
    
                                      }
                                  }
    
    
    
    
                                  });
    
                          }
                          else{
                                              alert('Please fill all the field !');
                                      }
    
    
    
    
                          }); 
                                        
                                    }
                                    
                                    
                                });
    
    
                            }
          
                     //      placeprice trigger function end
          
          
                    //      moving average function start
    
                    function movingAverage(){
    
                      alert("here in moving average")
                         $('#mv_option').change(function(){
    
    
                                if($('#mv_option').val()=='MA'){
     
                                    maplaceorder();  
                                }
                                
                                else if($('#mv_option').val()=='MA avg'){
                                    
                                    maavgplaceorder(); 
                                                                }
                                else if($('#mv_option').val()=='(P-MA/MA)'){
                                    
                                    pmaplaceorder();
                                }
                                else if($('#mv_option').val()=='P-MA/MA avg'){
                                    
                                    pmamaavgplaceorder(); 
                                    
                                }
                                
                                   
    
    //                            function maplaceorder code start
                                
                                function maplaceorder(){
                                       alert("here in MA")
                                        $("#trigger_ma_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_ma_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allmaoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allmaoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allmaoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allmaoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allmaoperatormethod();
                                       break;

                                       case "6":
                                       betweenmaoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   
                                   function allmaoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                 var trigger_ma_maOperator=$('#trigger_ma_maOperator').val();
                                 var trigger_ma_amount=$('#trigger_ma_amount_one').val();
                          
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"amount":trigger_ma_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                       
                                   }
                                   
                                   function betweenmaoperatormethod(){
                                       
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                 var trigger_ma_maOperator=$('#trigger_ma_maOperator').val();
                                 var trigger_ma_amount=$('#trigger_ma_amount_one').val();
                                 var trigger_ma_amount_two=$('#trigger_ma_amount_two').val();
                                 var trigger_ma_amount_three=$('#trigger_ma_amount_three').val();
                           
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_ma_amount_two, "to_amount":trigger_ma_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   
                                        });
                                    
                                }
     //                            function maplaceorder code end
     
     //                            function pmaplaceorder code start
                                
                                function pmaplaceorder(){
                                   
                                      $("#trigger_pma_pmaOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_pma_pmaOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allpmaoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allpmaoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allpmaoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allpmaoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allpmaoperatormethod();
                                       break;

                                       case "6":
                                       betweenpmaoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   function allpmaoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                 var trigger_ma_maOperator=$('#trigger_pma_pmaOperator').val();
                                 var trigger_ma_amount=$('#trigger_pma_amount_one').val();
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "amount":trigger_ma_amount},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                         window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   function betweenpmaoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                 var trigger_ma_maOperator=$('#trigger_pma_pmaOperator').val();
                                 var trigger_ma_amount=$('#trigger_pma_amount_one').val();
                                 var trigger_pma_amount_two=$('#trigger_pma_amount_two').val();
                                 var trigger_pma_amount_three=$('#trigger_pma_amount_three').val();
                           
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_pma_amount_two, "to_amount":trigger_pma_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                         window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                       
                                   }
                                   
                                   
                                   
                                      });
                                    
                                }
     //                            function pmaplaceorder code end
                                
    //                            function maavgplaceorder() code start
                                
                                function maavgplaceorder(){
                                       
                                     $("#trigger_maavg_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_maavg_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allmaavgoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allmaavgoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allmaavgoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allmaavgoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allmaavgoperatormethod();
                                       break;

                                       case "6":
                                       betweenmaavgoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   function allmaavgoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                // MA_AVG data
                                 var maavg_noof_candles=$('#maavg_noof_candles').val();
                                 var trigger_maavg_maOperator=$('#trigger_maavg_maOperator').val();
                                 var trigger_maavg_amount=$('#trigger_maavg_amount').val();
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"amount":trigger_maavg_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   function betweenmaavgoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                // MA_AVG data
                                 var maavg_noof_candles=$('#maavg_noof_candles').val();
                                 var trigger_maavg_maOperator=$('#trigger_maavg_maOperator').val();
                                 var trigger_maavg_amount=$('#trigger_maavg_amount').val();
                                 var trigger_maavg_amount_one=$('#trigger_maavg_amount_one').val();
                                 var trigger_maavg_amount_two=$('#trigger_maavg_amount_two').val();
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator, "instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_maavg_amount_one, "to_amount":trigger_maavg_amount_two},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                     });
                                    
                                }
    //                            function maavgplaceorder() code end
    
    //                            function pmamaavgplaceorder() code start
    
                                function pmamaavgplaceorder(){
                                      
                                       $("#p_ma_ma_avg_operator").change(function(){
                                    
                                   var trigger_price_operator = $("#p_ma_ma_avg_operator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allpmamaavgoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allpmamaavgoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allpmamaavgoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allpmamaavgoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allpmamaavgoperatormethod();
                                       break;

                                       case "6":
                                       betweenpmamaavgoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   function allpmamaavgoperatormethod(){
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                // MA_AVG data
                                 var maavg_noof_candles=$('#pmamaavg_noof_candles').val();
                                 var trigger_maavg_maOperator=$('#p_ma_ma_avg_operator').val();
                                 var trigger_maavg_amount=$('#trigger_pmamaavg_amount').val();
                                
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"amount":trigger_maavg_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   function betweenpmamaavgoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_ma_option=$('#mv_option').val();
                                 var trigger_ma_time_frame=$('#trigger_ma_time_frame').val();
                                 var trigger_ma_time_frame_data_type=$('#trigger_ma_time_frame option:selected').data("type");
                                 var trigger_ma_time_frame_data_duration=$('#trigger_ma_time_frame option:selected').data("duration").toString();
                                 var trigger_ma_period=$('#trigger_ma_period').val();
                                 var trigger_ma_type=$('#trigger_ma_type').val();
                                // MA_AVG data
                                 var maavg_noof_candles=$('#pmamaavg_noof_candles').val();
                                 var trigger_maavg_maOperator=$('#p_ma_ma_avg_operator').val();
                                 var trigger_maavg_amount=$('#trigger_pmamaavg_amount').val();
                                 var trigger_pmamaavg_amount_one=$('#trigger_pmamaavg_amount_one').val();
                                 var trigger_pmamaavg_amount_two=$('#trigger_pmamaavg_amount_two').val();
                                
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_pmamaavg_amount_one, "to_amount":trigger_pmamaavg_amount_two},
                                             "exchange_id":exchange     
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   
                                      });
                                    
                                }
                                
                             //   function pmamaavgplaceorder() code start
       
    
    
                            });
                    }
    
    
                    //      moving average function end
                    
                    
                    
                    
                    
                    // Function volume code start
                    
                    function Volume(){
                        
                        $('#selection_volume').change(function(){
                            
                           if($('#selection_volume').val()== 'volume') {
                               
                               simplevolume();
                               
                           }
                           else if($('#selection_volume').val()== 'volume_avg'){
                               
                               volumeavg();
                               
                           }
                           
                           
    //                       simple volume function code start
    
                              function simplevolume(){

                               alert("here all simplevolume");  
                                    $("#trigger_simplevolume_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_simplevolume_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allsimplevolumeoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allsimplevolumeoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allsimplevolumeoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allsimplevolumeoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allsimplevolumeoperatormethod();
                                       break;

                                       case "6":
                                       betweensimplevolumeoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   function allsimplevolumeoperatormethod(){
                                      alert("here all simplevolumeoperator");
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_volume_option=$('#selection_volume').val();
                                 var trigger_volume_time_frame=$('#trigger_volume_time_frame').val();
                                 var trigger_volume_time_frame_data_type=$('#trigger_volume_time_frame option:selected').data('type');
                                 var trigger_volume_time_frame_data_duration=$('#trigger_volume_time_frame option:selected').data('duration').toString();
                                 var trigger_volume_maOperator=$('#trigger_simplevolume_maOperator').val();
                                 var trigger_volume_amount=$('#trigger_simplevolume_amount_one').val();
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"type":trigger_volume_option, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"amount":trigger_volume_amount,"instrument_token":trigger_instrumenttoken},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   function betweensimplevolumeoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_volume_option=$('#selection_volume').val();
                                 var trigger_volume_time_frame=$('#trigger_volume_time_frame').val();
                                 var trigger_volume_time_frame_data_type=$('#trigger_volume_time_frame option:selected').data('type');
                                 var trigger_volume_time_frame_data_duration=$('#trigger_volume_time_frame option:selected').data('duration').toString();
                                 var trigger_volume_maOperator=$('#trigger_simplevolume_maOperator').val();
                                 var trigger_volume_amount=$('#trigger_simplevolume_amount_one').val();
                                 var trigger_simplevolume_amount_two=$('#trigger_simplevolume_amount_two').val();
                                 var trigger_simplevolume_amount_three=$('#trigger_simplevolume_amount_three').val();
                                 
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"type":trigger_volume_option, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_simplevolume_amount_two, "to_amount":trigger_simplevolume_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                    });
                                }
                                
                                //  simple volume function code end
                            
                            
                            //  volume avg function code start
    
                              function volumeavg(){
                               alert("here in volumeavg")  
                                    $("#trigger_volumeavg_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_volumeavg_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allvolumeavgoperatormethod();
                                       break;
                                       
                                       case "2":    
                                       allvolumeavgoperatormethod();
                                       break;
                                       
                                       case "3":    
                                       allvolumeavgoperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allvolumeavgoperatormethod();
                                       break;
                                       
                                       case "5":    
                                       allvolumeavgoperatormethod();
                                       break;

                                       case "6":
                                       betweenvolumeavgoperatormethod();
                                       break;
                                       
                                   }
                                   
                                   
                                   function allvolumeavgoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_volume_option=$('#selection_volume').val();
                                 var trigger_volume_time_frame=$('#trigger_volume_time_frame').val();
                                 var trigger_volume_time_frame_data_type=$('#trigger_volume_time_frame option:selected').data('type');
                                 var trigger_volume_time_frame_data_duration=$('#trigger_volume_time_frame option:selected').data('duration').toString();
                                 var trigger_volume_avg_no_candles=$('#vol_avg_no_candles').val();
                                 var trigger_volume_maOperator=$('#trigger_volumeavg_maOperator').val();
                                 var trigger_volume_amount=$('#vol_avg_amount_one').val();
                           
                                 
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"type":trigger_volume_option,"volume_average_candles":trigger_volume_avg_no_candles, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"amount":trigger_volume_amount,"instrument_token":trigger_instrumenttoken},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                              window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   function betweenvolumeavgoperatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_volume_option=$('#selection_volume').val();
                                 var trigger_volume_time_frame=$('#trigger_volume_time_frame').val();
                                 var trigger_volume_time_frame_data_type=$('#trigger_volume_time_frame option:selected').data('type');
                                 var trigger_volume_time_frame_data_duration=$('#trigger_volume_time_frame option:selected').data('duration').toString();
                                 var trigger_volume_avg_no_candles=$('#vol_avg_no_candles').val();
                                 var trigger_volume_maOperator=$('#trigger_volumeavg_maOperator').val();
                                 var vol_avg_amount_two=$('#vol_avg_amount_two').val();
                                 var vol_avg_amount_three=$('#vol_avg_amount_three').val();
                                
                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"type":trigger_volume_option,"volume_average_candles":trigger_volume_avg_no_candles, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"instrument_token":trigger_instrumenttoken, "from_amount":vol_avg_amount_two, "to_amount":vol_avg_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                              window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                    });
                                }
                                
                                //  volume avg function code end
                        });
                        
                    }
                    
                     // Function volume code end
                     
                     
                     
                     // Function RSI code start
                     
                     function Rsi(){
                         
                         $("#trigger_rsi_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_rsi_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allrsioperatormethod();
                                       break;
                                       
                                       case "2":    
                                        allrsioperatormethod();
                                       break;
                                       
                                       case "3":    
                                        allrsioperatormethod();
                                       break;
                                       
                                       case "4":    
                                       allrsioperatormethod();
                                       break;
                                       
                                       case "5":    
                                        allrsioperatormethod();
                                       break;

                                       case "6":
                                       betweenrsioperatormethod();
                                       break;
                                       
                                   }
                                   
                                   function  allrsioperatormethod(){
                                       
                                        $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_rsi_time_frame=$('#trigger_rsi_time_frame').val();
                               //   var trigger_rsi_time_frame_data_type=$('#trigger_rsi_time_frame').val($(this).attr("type"));
                                 var trigger_rsi_time_frame_data_type=$('#trigger_rsi_time_frame option:selected').data('type');
                               //   var trigger_rsi_time_frame_data_duration=$('#trigger_rsi_time_frame').attr('duration');
                               var trigger_rsi_time_frame_data_duration=$('#trigger_rsi_time_frame option:selected').data('duration').toString();
                                 var trigger_rsi_period=$('#rsi_periods').val();
                                 var trigger_rsi_maOperator=$('#trigger_rsi_maOperator').val();
                                 var trigger_rsi_amount=$('#trigger_rsi_amount_one').val();
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"time_frame":trigger_rsi_time_frame,"time_frame_type":trigger_rsi_time_frame_data_type,"time_frame_duration":trigger_rsi_time_frame_data_duration,"operator":trigger_rsi_maOperator,"amount":trigger_rsi_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_rsi_period},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   function betweenrsioperatormethod(){
                                       
                                        $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_rsi_time_frame=$('#trigger_rsi_time_frame').val();
                                 var trigger_rsi_time_frame_data_type=$('#trigger_rsi_time_frame option:selected').data("type");
                                 var trigger_rsi_time_frame_data_duration=$('#trigger_rsi_time_frame option:selected').data("duration").toString();
                                 var trigger_rsi_period=$('#rsi_periods');
                                 var trigger_rsi_maOperator=$('#trigger_rsi_maOperator').val();
                                 var trigger_rsi_amount_two=$('#trigger_rsi_amount_two').val();
                                 var trigger_rsi_amount_three=$('#trigger_rsi_amount_three').val();
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "trigger_criteria":{"time_frame":trigger_rsi_time_frame,"time_frame_type":trigger_rsi_time_frame_data_type,"time_frame_duration":trigger_rsi_time_frame_data_duration,"operator":trigger_rsi_maOperator, "instrument_token":trigger_instrumenttoken,"period":trigger_rsi_period, "from_amount":trigger_rsi_amount_two, "to_amount":trigger_rsi_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                       
                                   }
                                   
                                   
                                   
                               });  
                         
                     }
                     
                     // Function RSI code end
                     
                     
                      // Function p2p1 code start
                      
                       function p2p1(){
                            
                            alert("hello i am here in p2p1");   
                            $("#trigger_p2p1_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_p2p1_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allp2p1operatormethod();
                                       break;
                                       
                                       case "2":    
                                        allp2p1operatormethod();
                                       break;
                                       
                                       case "3":    
                                         allp2p1operatormethod();
                                       break;
                                       
                                       case "4":    
                                        allp2p1operatormethod();
                                       break;
                                       
                                       case "5":    
                                        allp2p1operatormethod();
                                       break;

                                       case "6":
                                       betweenp2p1operatormethod();
                                       break;
                                       
                                   } 
                                   
                                   function allp2p1operatormethod(){
                                       alert("hello i am here in allp2p1operatormethod"); 
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                               //   var symbol=$('#symbol').val();
                               var symbol="N/A";
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p2p1_symbol_one=$('#p2p1symbol_one').val();
                                 var trigger_p2p1_symbol_two=$('#p2p1symbol_two').val();
                                 var trigger_p2p1_maOperator=$('#trigger_p2p1_maOperator').val();
                                 var trigger_p2p1_amount=$('#trigger_p2p1_amount_one').val();
                                 
                                 debugger;
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount},         
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   
                                   function betweenp2p1operatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p2p1_symbol_one=$('#p2p1symbol_one').val();
                                 var trigger_p2p1_symbol_two=$('#p2p1symbol_two').val();
                                 var trigger_p2p1_maOperator=$('#trigger_p2p1_maOperator').val();
                                 var trigger_p2p1_amount_two=$('#trigger_p2p1_amount_two').val();
                                 var trigger_p2p1_amount_three=$('#trigger_p2p1_amount_three').val();
                                 
                                 debugger;
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                            });
                         
                     }
                      
                      // Function p2p1 code end
          
                   // Function  p1-p2 code start
                      
                         function p1minusp2(){
                          alert("hello plmiunsp2");
                            $("#trigger_p1minusp2_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_p1minusp2_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":   
                                       alert("first operator selected");    
                                       allp1minusp2operatormethod();
                                       break;
                                       
                                       case "2":    
                                        allp1minusp2operatormethod();
                                       break;
                                       
                                       case "3":    
                                         allp1minusp2operatormethod();
                                       break;
                                       
                                       case "4":    
                                        allp1minusp2operatormethod();
                                       break;
                                       
                                       case "5":    
                                        allp1minusp2operatormethod();
                                       break;

                                       case "6":
                                       betweenp1minusp2operatormethod();
                                       break;
                                       
                                   } 
                                   
                                   function allp1minusp2operatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                               //   var symbol=$('#symbol').val();
                               var symbol="N/A";
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p1minusp2_symbol_one=$('#p1minusp2symbol_one').val();
                                 var trigger_p1minusp2_symbol_two=$('#p1minusp2symbol_two').val();
                                 var trigger_p1minusp2_maOperator=$('#trigger_p1minusp2_maOperator').val();
                                 var trigger_p1minusp2_amount=$('#trigger_p1minusp2_amount_one').val();
                           
                                debugger;
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1minusp2_symbol_one, "symbol2_exchange":trigger_p1minusp2_symbol_two,"operator":trigger_p1minusp2_maOperator,"amount":trigger_p1minusp2_amount},         
                                             "exchange_id":exchange     
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   
                                   function betweenp1minusp2operatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol="N/A";
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p1minusp2_symbol_one=$('#p1minusp2symbol_one').val();
                                 var trigger_p1minusp2_symbol_two=$('#p1minusp2symbol_two').val();
                                 var trigger_p1minusp2_maOperator=$('#trigger_p1minusp2_maOperator').val();
                                 var trigger_p1minusp2_amount_two=$('#trigger_p1minusp2_amount_two').val();
                                 var trigger_p1minusp2_amount_three=$('#trigger_p1minusp2_amount_three').val();
                                 
                                 debugger;
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1minusp2_symbol_one, "symbol2_exchange":trigger_p1minusp2_symbol_two,"operator":trigger_p1minusp2_maOperator, "from_amount":trigger_p1minusp2_amount_two, "to_amount":trigger_p1minusp2_amount_three},
                                             "exchange_id":exchange     
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                            });
                         
                     }
          
                     // Function  p1-p2 code end
                     
                     // Function p1+p2 code start
                      function p1plusp2(){
                         alert("here p1plusp2");
                            $("#trigger_p1plusp2_maOperator").change(function(){
                                    
                                   var trigger_price_operator = $("#trigger_p1plusp2_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":    
                                       allp1plusp2operatormethod();
                                       break;
                                       
                                       case "2":    
                                        allp1plusp2operatormethod();
                                       break;
                                       
                                       case "3":    
                                         allp1plusp2operatormethod();
                                       break;
                                       
                                       case "4":    
                                        allp1plusp2operatormethod();
                                       break;
                                       
                                       case "5":    
                                        allp1plusp2operatormethod();
                                       break;

                                       case "6":
                                       betweenp1plusp2operatormethod();
                                       break;
                                       
                                   } 
                                   
                                   function allp1plusp2operatormethod(){
                                       alert("here allp1plusp2operatormethod");
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                               //   var symbol=$('#symbol').val();
                                 var symbol="N/A";
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p1plusp2_symbol_one=$('#p1plusp2symbol_one').val();
                                 var trigger_p1plusp2_symbol_two=$('#p1plusp2symbol_two').val();
                                 var trigger_p1plusp2_maOperator=$('#trigger_p1plusp2_maOperator').val();
                                 var trigger_p1plusp2_amount=$('#trigger_p2plusp1_amount_one').val();
                                 
                                 debugger;
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1plusp2_symbol_one, "symbol2_exchange":trigger_p1plusp2_symbol_two,"operator":trigger_p1plusp2_maOperator,"amount":trigger_p1plusp2_amount},         
                                             "exchange_id":exchange     
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                                   
                                   function betweenp1plusp2operatormethod(){
                                       
                                       $('#placeorder').on('click', function(){
    
                                 var trigger_name= $('#trigger_name').val();
                                 var exchange= $('#exchange').val();
                                 var symbol=$('#symbol').val();
                                 var trigger_instrumenttoken=$('#instrument_token').val();
                                 var trigger_condition=$('#select_trigger').val();
                                 var trigger_p1plusp2_symbol_one=$('#p1plusp2symbol_one').val();
                                 var trigger_p1plusp2_symbol_two=$('#p1plusp2symbol_two').val();
                                 var trigger_p1plusp2_maOperator=$('#trigger_p1plusp2_maOperator').val();
                                 var trigger_p1plusp2_amount_two=$('#trigger_p1plusp2_amount_two').val();
                                 var trigger_p1plusp2_amount_three=$('#trigger_p1plusp2_amount_three').val();
                                 
                                 debugger;
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                      url:"http://127.0.0.1:8000/trigger_list/update/"+2226,
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1plusp2_symbol_one, "symbol2_exchange":trigger_p1plusp2_symbol_two,"operator":trigger_p1plusp2_maOperator, "from_amount":trigger_p1plusp2_amount_two, "to_amount":trigger_p1plusp2_amount_three},
                                             "exchange_id":exchange     
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger and order created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 });
                                   }
                                   
                            });
                         
                     }
                     // Function p1+p2 code end
        
          
        
            
            
            
      
        });    
    });


  