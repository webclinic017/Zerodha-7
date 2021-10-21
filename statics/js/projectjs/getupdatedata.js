$(document).ready(function() {
        
//        var triggerCondition=$("#select_trigger").val();
        if ($("#select_trigger").val() == "1") {
                $("#price-con").show();
                $("#price-am").show();
                $("#symbolcontainer").show();
            } else {
                $("#price-con").hide();
                 $("#price-am").hide();
            }
            
            
         if($("#select_trigger").val() == "7"){
                
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
            
            if($("#select_trigger").val() == "8"){
                
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
            
               if ($("#select_trigger").val() == "6") {
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
            
             if ($("#select_trigger").val() == "5") {
                $("#trigger_con").show();
                $("#trigger_con_one").show();
                $("#trigger_con_two").show();
                $("#symbolcontainer").show();
            } else {
                $("#trigger_con").hide();
                $("#trigger_con_one").hide();
                $("#trigger_con_two").hide();
            }
            
            if ($("#select_trigger").val() == "4") {
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
            
             if ($("#select_trigger").val() == "2") {
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
            
            if ($("#select_trigger").val() == "3") {
                $("#volume_con").show();
                $("#volume_con_time_frame").show();
                $("#symbolcontainer").show();
            } else {
                $("#volume_con").hide();
                 $("#volume_con_time_frame").hide();
            }
            
            
            
            /*/////////////////volume code start///////////////////////////////////*/
            
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