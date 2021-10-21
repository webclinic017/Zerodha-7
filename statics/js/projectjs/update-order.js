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
//                $("#symbolcontainer").show();
        }
        
          if($(this).val() == "7"){
            
            $("#p2minusp1_con").show();
            $("#p2minusp1_conone").show();
            $("#p2minusp1_confour").show();
            $("#p2minusp1_symbol_one").show();
            $("#p2minusp1_symbol_two").show();
            $("#symbolcontainer").hide();
        }else{
            $("#p2minusp1_con").hide();
            $("#p2minusp1_conone").hide();
            $("#p2minusp1_contwo").hide();
            $("#p2minusp1_conthree").hide();
            $("#p2minusp1_confour").hide();
            $("#p2minusp1_symbol_one").hide();
            $("#p2minusp1_symbol_two").hide();
//                $("#symbolcontainer").show();
            
        }
        
         if($(this).val() == "8"){
            
            $("#p2plusp1_con").show();
            $("#p2plusp1_conone").show();
            $("#p2plusp1_confour").show();
            $("#p2plusp1_symbol_one").show();
            $("#p2plusp1_symbol_two").show();
            $("#symbolcontainer").hide();
        }else{
            $("#p2plusp1_con").hide();
            $("#p2plusp1_conone").hide();
            $("#p2plusp1_confour").hide();
            $("#p2plusp1_contwo").hide();
            $("#p2plusp1_conthree").hide();
            $("#p2plusp1_symbol_one").hide();
            $("#p2plusp1_symbol_two").hide();
//                $("#symbolcontainer").show();
            
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



$(function () {
    $("#select_trigger").change(function () {
        
      
});
});



$(function () {
    $("#select_trigger").change(function () {
        
        
});
});



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
    $("#order_type").change(function () {
        
        if($(this).val()=="2"){
           
            $("#order-price-container").show();
            $("#trigger-price-container").hide();
        }else if($(this).val()=="3"){
            
           $("#order-price-container").show();
           $("#trigger-price-container").show();
        }
        // else if($(this).val()=="1"){
            
        //      $("#trigger-price-container").show();
        //       $("#order-price-container").hide();
             
        // }
         else if($(this).val()=="4"){
            
             $("#trigger-price-container").show(); 
             $("#order-price-container").hide();
             
        }
        else{
            
            $("#order-price-container").hide();
            $("#trigger-price-container").hide();
        }
        

    });
    });

  $(document).ready(function(){     
      /* Act on the event */
 
    
        
        if($("#order_type").val()=="2"){
           
            $("#order-price-container").show();
            $("#trigger-price-container").hide();
        }else if($("#order_type").val()=="3"){
            
           $("#order-price-container").show();
           $("#trigger-price-container").show();
        }
        // else if($("#order_type").val()=="1"){
            
        //      $("#trigger-price-container").show();
        //       $("#order-price-container").hide();
             
        // }
         else if($("#order_type").val()=="4"){
            
             $("#trigger-price-container").show(); 
             $("#order-price-container").hide();
             
        }
        else{
            
            $("#order-price-container").hide();
            $("#trigger-price-container").hide();
        }
        

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
    $("#trigger_p2minusp1_maOperator").change(function () {
        
        if($(this).val()=="6"){
           
            $("#p2minusp1_contwo").show();
            $("#p2minusp1_conthree").show();
           $("#p2minusp1_conone").hide();
            $("#p2minusp1_confour").hide();
            
        }else{
            
           $("#p2minusp1_contwo").hide();
           $("#p2minusp1_conthree").hide();
           $("#p2minusp1_conone").show();
            $("#p2minusp1_confour").show();
        }
        

    });
    });







$(function () {
    $("#trigger_p2plusp1_maOperator").change(function () {
        
         if($(this).val()=="6"){
           
            $("#p2plusp1_contwo").show();
            $("#p2plusp1_conthree").show();
           $("#p2plusp1_conone").hide();
            $("#p2plusp1_confour").hide();
            
        }else{
            
           $("#p2plusp1_contwo").hide();
           $("#p2plusp1_conthree").hide();
           $("#p2plusp1_conone").show();
            $("#p2plusp1_confour").show();
        }
        

    });
    });

$(document).ready(function(){
    var order_price, order_trigger_price;
             
             
             // Select order type start coding
             
                     function orderprice(){
                                 
                                  
                                 
                                 if($('#order_type').val()=='1'){
                                  
                                order_trigger_price="0";
                                order_price="0";
                                
                              }
                              else if($('#order_type').val()=='2'){
                                  
                                order_price=$('#order-price').val();  
                                order_trigger_price="0";
                                
                                
                              }
                              else if($('#order_type').val()=='3'){
                                  
                               order_price=$('#order-price').val();  
                               order_trigger_price=$('#order-trigger-price').val();
                                
                              }
                               else if($('#order_type').val()=='4'){
                                  
                               order_trigger_price=$('#order-trigger-price').val();  
                               order_price="0";
                                
                              }
                                 
                             }

       
        
         //      placeprice trigger function start
       
                   $('#update').on('click', function(){
 
 
                       var order_id=$('#order_id').val();
                       var trigger_name= $('#trigger_name').val();
                       
                       var order_buy_sell= $('#order_buy_sell').val();
                       var order_qty= $('#order_qty').val();
                       var order_product_type=$('#order_product_type').val();
                       var order_type=$('#order_type').val();
                       var order_symbol=$('#order_symbol').val();
                       var order_exchange=$('#order_exchange').val();
                       
                       orderprice();
                      
                       
                       debugger;
                    //    alert(trigger_name);
                       if(trigger_name!=""){
 
 
                               $.ajax({
 
                                   url:"http://127.0.0.1:8000/login_view/home/trigger_order_list/update/"+order_id,
                                   method:"POST",
                                   data:JSON.stringify({
                                   "trigger": {
                                   "trigger_name":trigger_name
                                   },
                                   "order":{
                                    
                                   "buy_sell":order_buy_sell,
                                   "quantity":order_qty,
                                   "product_type":order_product_type,
                                   "order_types":order_type,
                                   "symbol":order_symbol,
                                   "exchange_id":order_exchange,
                                   "price":order_price,
                                   "trigger_price":order_trigger_price
                                   
                                   }  
                                   }),
                                   dataType: "json",
                                   contentType: "application/json",
                                   success: function(result){
                                   if(result.status=="success")
                                   {
                                    alert('Order updated successfully');
                                    window.location.reload();
 
                                   }
                                   else{
                                    alert('Error occurred');
                                    window.location.reload();
                                   }
                               }
 
 
 
 
                               });
 
                       }
                       else{
                                           alert('Please fill all the field !');
                                   }
 
 
 
 
                       }); 
                                     
                    
                  //      placeprice trigger function end
   
 });