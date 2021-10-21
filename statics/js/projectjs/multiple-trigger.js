$(document).ready(function(){

        $('#placeorder').on('click', function(){
    
              
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
                                        
                                         
    
    
    
                          var trigger_name= $('#trigger_name').val();
                          var exchange= $('#exchange').val();
                          var symbol=$('#symbol').val();
                          var trigger_instrumenttoken=$('#instrument_token').val();
                          var trigger_condition=$('#select_trigger').val();
                          var trigger_price_operator=$('#trigger_price_operator').val();
                          var trigger_price_amount=$('#trigger_price_amount').val();

                          var operator = '';
                          if (trigger_price_operator == "1")
                          {
                                operator = ">=";
                          }
                          else if (trigger_price_operator == '2') 
                          {
                                operator = "<=";
                          }
                          else if (trigger_price_operator == '3') 
                          {
                                operator = ">";
                          }
                          else if (trigger_price_operator == '4') 
                          {
                                operator = "<";
                          }
                          else if (trigger_price_operator == '5') 
                          {
                                operator = "=";
                          }
                          else if (trigger_price_operator == '6') 
                          {
                                operator = "Between";
                          }
                        //    debugger;
                          if(trigger_name!=""){
    
    
                                  $.ajax({
    
                                      url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                      method:"POST",
                                      data:JSON.stringify({
                                      "trigger": {
                                      "trigger_name":trigger_name,
                                      "symbol":symbol,
                                      "trigger_condition_id": trigger_condition,
                                      "trigger_criteria":{"operator":trigger_price_operator, "amount":trigger_price_amount, "instrument_token":trigger_instrumenttoken},
                                      "criteria":{"Operator": operator, "Amount":trigger_price_amount},
                                      "exchange_id":exchange		
                              }}),
                                      dataType: "json",
                                      contentType: "application/json",
                                      success: function(result){
                                      if(result.status=="success")
                                      {
                                       alert(trigger_name + ' trigger created successfully');
                                       window.location.reload();
    
                                      }
                                  }
    
    
    
    
                                  });
    
                          }
                          else{
                                              alert('Please fill all the field !');
                                      }
    
    
    
    
                          
                                        
                                    }
                                    
                                    
                                    
                                    function betweenpriceoprtaormethod(){
                                        
                                         
    
    
    
                                       var trigger_name= $('#trigger_name').val();
                                       var exchange= $('#exchange').val();
                                       var symbol=$('#symbol').val();
                                       var trigger_instrumenttoken=$('#instrument_token').val();
                                       var trigger_condition=$('#select_trigger').val();
                                       var trigger_price_operator=$('#trigger_price_operator').val();
                                       var trigger_price_amount_one=$('#trigger_price_amount_one').val();
                                       var trigger_price_amount_two=$('#trigger_price_amount_two').val();
                         
                                       
                          var operator = '';
                          if (trigger_price_operator == "1")
                          {
                                operator = ">=";
                          }
                          else if (trigger_price_operator == '2') 
                          {
                                operator = "<=";
                          }
                          else if (trigger_price_operator == '3') 
                          {
                                operator = ">";
                          }
                          else if (trigger_price_operator == '4') 
                          {
                                operator = "<";
                          }
                          else if (trigger_price_operator == '5') 
                          {
                                operator = "=";
                          }
                          else if (trigger_price_operator == '6') 
                          {
                                operator = "Between";
                          }

                          
                        //   debugger;
                          if(trigger_name!=""){
    
    
                                  $.ajax({
    
                                      url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                      method:"POST",
                                      data:JSON.stringify({
                                        "trigger": {
                                      "trigger_name":trigger_name,
                                      "symbol":symbol,
                                      "trigger_condition_id": trigger_condition,

                                      "criteria":{"Operator":operator, "From Amount":trigger_price_amount_one, "To Amount":trigger_price_amount_two},

                                      "trigger_criteria":{"operator":trigger_price_operator, "from_amount":trigger_price_amount_one, "to_amount":trigger_price_amount_two, "instrument_token":trigger_instrumenttoken},
                                      "exchange_id":exchange		
                                  }}),

                                  dataType: "json",
                                      contentType: "application/json",
                                      success: function(result){
                                      if(result.status=="success")
                                      {
                                       alert(trigger_name + ' trigger created successfully');
                                       window.location.reload();
    
                                      }
                                  }
    
    
    
    
                                  });
    
                          }
                          else{
                                              alert('Please fill all the field !');
                                      }
    
    
    
    
                           
                                        
                                    }
                                    
                                    
                                
    
    
                            }
          
                     //      placeprice trigger function end
          
          
                    //      moving average function start
    
                    function movingAverage(){
    
                      
                         
    
    
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
                          

                                 var operator = '';
                                 if (trigger_ma_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_ma_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_ma_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_ma_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_ma_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_ma_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
       

                                 if(trigger_name!=""){
    
//     alert("callingg");
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Time Frame":trigger_ma_time_frame,"Period":trigger_ma_period,"Type":trigger_ma_type,"Operator":operator,"Amount":trigger_ma_amount},

                                  


                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"amount":trigger_ma_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                       
                                   }
                                   
                                   function betweenmaoperatormethod(){
                                       
                                       
                                       
    
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


                                 var operator = '';
                                 if (trigger_ma_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_ma_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_ma_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_ma_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_ma_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_ma_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           
                                 if(trigger_name!=""){
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Period":trigger_ma_period, "From Amount":trigger_ma_amount_two, "To Amount":trigger_ma_amount_three},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_ma_amount_two, "to_amount":trigger_ma_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   
                                        
                                    
                                }
     //                            function maplaceorder code end
     
     //                            function pmaplaceorder code start
                                
                                function pmaplaceorder(){
                                   
                                     
                                    
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
                           

                                 var operator = '';
                                 if (trigger_ma_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_ma_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_ma_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_ma_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_ma_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_ma_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Period":trigger_ma_period, "Amount":trigger_ma_amount},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "amount":trigger_ma_amount},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                         window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   function betweenpmaoperatormethod(){
                                       
                                       
    
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
                           

                                 var operator = '';
                                 if (trigger_ma_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_ma_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_ma_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_ma_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_ma_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_ma_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Period":trigger_ma_period, "From Amount":trigger_pma_amount_two, "To Amount":trigger_pma_amount_three},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_ma_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_pma_amount_two, "to_amount":trigger_pma_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                         window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                       
                                   }
                                   
                                   
                                   
                                      
                                    
                                }
     //                            function pmaplaceorder code end
                                
    //                            function maavgplaceorder() code start
                                
                                function maavgplaceorder(){
                                       
                                     
                                    
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
                                

                                 var operator = '';
                                 if (trigger_maavg_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_maavg_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_maavg_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_maavg_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_maavg_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_maavg_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Candles":maavg_noof_candles, "Time Frame":trigger_ma_time_frame,"Time Frame Duration":trigger_ma_time_frame_data_duration,"Type":trigger_ma_type,"Operator":operator,"amount":trigger_maavg_amount,"Period":trigger_ma_period},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"amount":trigger_maavg_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   function betweenmaavgoperatormethod(){
                                       
                                       
    
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


                                 var operator = '';
                                 if (trigger_maavg_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_maavg_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_maavg_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_maavg_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_maavg_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_maavg_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Candles":maavg_noof_candles, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Period":trigger_ma_period, "From Amount":trigger_maavg_amount_one, "To Amount":trigger_maavg_amount_two},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator, "instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_maavg_amount_one, "to_amount":trigger_maavg_amount_two},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                     
                                    
                                }
    //                            function maavgplaceorder() code end
    
    //                            function pmamaavgplaceorder() code start
    
                                function pmamaavgplaceorder(){
                                      
                                       
                                    
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
                                


                                 var operator = '';
                                 if (trigger_maavg_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_maavg_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_maavg_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_maavg_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_maavg_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_maavg_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Candles":maavg_noof_candles, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Amount":trigger_maavg_amount,"Period":trigger_ma_period},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"amount":trigger_maavg_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                                   function betweenpmamaavgoperatormethod(){
                                       
                                       
    
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
                                

                                 var operator = '';
                                 if (trigger_maavg_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_maavg_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_maavg_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_maavg_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_maavg_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_maavg_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Moving Average":trigger_ma_option, "Candles":maavg_noof_candles, "Time Frame":trigger_ma_time_frame,"Type":trigger_ma_type,"Operator":operator,"Period":trigger_ma_period, "From Amount":trigger_pmamaavg_amount_one, "To Amount":trigger_pmamaavg_amount_two},
                                             "trigger_criteria":{"moving_average":trigger_ma_option, "moving_average_candles":maavg_noof_candles, "time_frame":trigger_ma_time_frame,"time_frame_type":trigger_ma_time_frame_data_type,"time_frame_duration":trigger_ma_time_frame_data_duration,"type":trigger_ma_type,"operator":trigger_maavg_maOperator,"instrument_token":trigger_instrumenttoken,"period":trigger_ma_period, "from_amount":trigger_pmamaavg_amount_one, "to_amount":trigger_pmamaavg_amount_two},
                                             "exchange_id":exchange		
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   
                                      
                                    
                                }
                                
                             //   function pmamaavgplaceorder() code start
       
    
    
                            
                    }
    
    
                    //      moving average function end
                    
                    
                    
                    
                    
                    // Function volume code start
                    
                    function Volume(){
                        
                        
                            
                           if($('#selection_volume').val()== 'volume') {
                               
                               simplevolume();
                               
                           }
                           else if($('#selection_volume').val()== 'volume_avg'){
                               
                               volumeavg();
                               
                           }
                           
                           
    //                       simple volume function code start
    
                              function simplevolume(){

                                
                                    
                                    
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
                                      // alert("here all simplevolumeoperator");
                                       
    
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
                           

                                 var operator = '';
                                 if (trigger_volume_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_volume_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_volume_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_volume_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_volume_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_volume_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Type":trigger_volume_option, "Time Frame":trigger_volume_time_frame,"Operator":operator,"Amount":trigger_volume_amount},
                                             "trigger_criteria":{"type":trigger_volume_option, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"amount":trigger_volume_amount,"instrument_token":trigger_instrumenttoken},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    




























                                             
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                                   function betweensimplevolumeoperatormethod(){
                                       
                                      
    
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
                                 

                                 var operator = '';
                                 if (trigger_volume_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_volume_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_volume_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_volume_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_volume_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_volume_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                                 
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Type":trigger_volume_option, "Time Frame":trigger_volume_time_frame,"Operator":operator, "From Amount":trigger_simplevolume_amount_two, "TO Amount":trigger_simplevolume_amount_three},
                                             "trigger_criteria":{"type":trigger_volume_option, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_simplevolume_amount_two, "to_amount":trigger_simplevolume_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                    
                                }
                                
                                //  simple volume function code end
                            
                            
                            //  volume avg function code start
    
                              function volumeavg(){
                                 
                                    
                                    
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
                           
                                 

                                 var operator = '';
                                 if (trigger_volume_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_volume_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_volume_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_volume_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_volume_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_volume_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Type":trigger_volume_option,"Candles":trigger_volume_avg_no_candles, "Time Frame":trigger_volume_time_frame,"Operator":operator,"Amount":trigger_volume_amount},
                                             "trigger_criteria":{"type":trigger_volume_option,"volume_average_candles":trigger_volume_avg_no_candles, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"amount":trigger_volume_amount,"instrument_token":trigger_instrumenttoken},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                              window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   function betweenvolumeavgoperatormethod(){
                                       
                                       
    
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
                                

                                 var operator = '';
                                 if (trigger_volume_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_volume_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_volume_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_volume_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_volume_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_volume_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!=""){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Type":trigger_volume_option,"Candles":trigger_volume_avg_no_candles, "Time Frame":trigger_volume_time_frame,"Operator":operator, "From Amount":vol_avg_amount_two, "To Amount":vol_avg_amount_three},
                                             "trigger_criteria":{"type":trigger_volume_option,"volume_average_candles":trigger_volume_avg_no_candles, "time_frame":trigger_volume_time_frame,"time_frame_type":trigger_volume_time_frame_data_type,"time_frame_duration":trigger_volume_time_frame_data_duration,"operator":trigger_volume_maOperator,"instrument_token":trigger_instrumenttoken, "from_amount":vol_avg_amount_two, "to_amount":vol_avg_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                              window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                    
                                }
                                
                                //  volume avg function code end
                        
                        
                    }
                    
                     // Function volume code end
                     
                     
                     
                     // Function RSI code start
                     
                     function Rsi(){
                         
                         
                                    
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
                           

                                 var operator = '';
                                 if (trigger_rsi_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_rsi_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_rsi_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_rsi_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_rsi_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_rsi_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Time Frame":trigger_rsi_time_frame,"Operator":operator,"Amount":trigger_rsi_amount,"Period":trigger_rsi_period},
                                             "trigger_criteria":{"time_frame":trigger_rsi_time_frame,"time_frame_type":trigger_rsi_time_frame_data_type,"time_frame_duration":trigger_rsi_time_frame_data_duration,"operator":trigger_rsi_maOperator,"amount":trigger_rsi_amount,"instrument_token":trigger_instrumenttoken,"period":trigger_rsi_period},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                                   function betweenrsioperatormethod(){
                                       
                                        
    
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
                                

                                 var operator = '';
                                 if (trigger_rsi_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_rsi_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_rsi_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_rsi_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_rsi_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_rsi_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"Time Frame":trigger_rsi_time_frame,"Operator":operator,"Period":trigger_rsi_period, "From Amount":trigger_rsi_amount_two, "To Amount":trigger_rsi_amount_three},
                                             "trigger_criteria":{"time_frame":trigger_rsi_time_frame,"time_frame_type":trigger_rsi_time_frame_data_type,"time_frame_duration":trigger_rsi_time_frame_data_duration,"operator":trigger_rsi_maOperator, "instrument_token":trigger_instrumenttoken,"period":trigger_rsi_period, "from_amount":trigger_rsi_amount_two, "to_amount":trigger_rsi_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                             window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                       
                                   }
                                   
                                   
                                   
                                
                         
                     }
                     
                     // Function RSI code end
                     
                     
                      // Function p2p1 code start
                      
                       function p2p1(){
                            
                            
                            
                                    
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
                                       // alert("hello i am here in allp2p1operatormethod"); 
                                       
    
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
                                 

                                 var operator = '';
                                 if (trigger_p2p1_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p2p1_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p2p1_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p2p1_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p2p1_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p2p1_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p2p1_symbol_one, "Second Symbol":trigger_p2p1_symbol_two,"Operator":operator,"Amount":trigger_p2p1_amount}, 
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount},         
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                
                                   }
                                   
                                   
                                   function betweenp2p1operatormethod(){
                                       
                                       
    
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
                                 

                                 var operator = '';
                                 if (trigger_p2p1_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p2p1_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p2p1_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p2p1_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p2p1_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p2p1_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p2p1_symbol_one, "Second Symbol":trigger_p2p1_symbol_two,"Operator":operator, "From Amount":trigger_p2p1_amount_two, "To Amount":trigger_p2p1_amount_three},
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                            
                         
                     }
                      
                      // Function p2p1 code end
          
                   // Function  p1-p2 code start
                      
                         function p1minusp2(){
                          
                            
                                    
                                   var trigger_price_operator = $("#trigger_p1minusp2_maOperator").val();
                                   
                                   switch(trigger_price_operator){
                                       
                                       case "1":   
                                       // alert("first operator selected");    
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
                           

                                 var operator = '';
                                 if (trigger_p1minusp2_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }

                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p1minusp2_symbol_one, "Second Symbol":trigger_p1minusp2_symbol_two,"Operator":operator,"Amount":trigger_p1minusp2_amount},         
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1minusp2_symbol_one, "symbol2_exchange":trigger_p1minusp2_symbol_two,"operator":trigger_p1minusp2_maOperator,"amount":trigger_p1minusp2_amount},         
                                             "exchange_id":exchange		
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                                   
                                   function betweenp1minusp2operatormethod(){
                                       
                                       
    
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
                                 

                                 var operator = '';
                                 if (trigger_p1minusp2_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p1minusp2_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p1minusp2_symbol_one, "Second Symbol":trigger_p1minusp2_symbol_two,"Operator":operator, "From Amount":trigger_p1minusp2_amount_two, "To Amount":trigger_p1minusp2_amount_three},
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1minusp2_symbol_one, "symbol2_exchange":trigger_p1minusp2_symbol_two,"operator":trigger_p1minusp2_maOperator, "from_amount":trigger_p1minusp2_amount_two, "to_amount":trigger_p1minusp2_amount_three},
                                             "exchange_id":exchange		
                                     } }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                            
                         
                     }
          
                     // Function  p1-p2 code end
                     
                     // Function p1+p2 code start
                      function p1plusp2(){
                         
                            
                                    
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
                                       // alert("here allp1plusp2operatormethod");
                                       
    
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
                                 

                                 var operator = '';
                                 if (trigger_p1plusp2_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                           
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p1plusp2_symbol_one, "Second Symbol":trigger_p1plusp2_symbol_two,"Operator":operator,"Amount":trigger_p1plusp2_amount},         
                                       //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator,"amount":trigger_p2p1_amount,"instrument_token":trigger_instrumenttoken},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1plusp2_symbol_one, "symbol2_exchange":trigger_p1plusp2_symbol_two,"operator":trigger_p1plusp2_maOperator,"amount":trigger_p1plusp2_amount},         
                                             "exchange_id":exchange		
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                                   
                                   function betweenp1plusp2operatormethod(){
                                       
                                       
    
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
                                 

                                 var operator = '';
                                 if (trigger_p1plusp2_maOperator == "1")
                                 {
                                       operator = ">=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '2') 
                                 {
                                       operator = "<=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '3') 
                                 {
                                       operator = ">";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '4') 
                                 {
                                       operator = "<";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '5') 
                                 {
                                       operator = "=";
                                 }
                                 else if (trigger_p1plusp2_maOperator == '6') 
                                 {
                                       operator = "Between";
                                 }
                                
                                 if(trigger_name!="" ){
    
    
                                         $.ajax({
    
                                             url:"http://127.0.0.1:8000/save_multiple_trigger/",
                                             method:"POST",
                                             data:JSON.stringify({
                                               "trigger": {
                                             "trigger_name":trigger_name,
                                             "symbol":symbol,
                                             "trigger_condition_id": trigger_condition,
                                             "criteria":{"First Symbol":trigger_p1plusp2_symbol_one, "Second Symbol":trigger_p1plusp2_symbol_two,"Operator":operator, "from Amount":trigger_p1plusp2_amount_two, "To Amount":trigger_p1plusp2_amount_three},
                                             //       "trigger_criteria":{"symbol1_exchange":trigger_p2p1_symbol_one, "symbol2_exchange":trigger_p2p1_symbol_two,"operator":trigger_p2p1_maOperator, "instrument_token":trigger_instrumenttoken, "from_amount":trigger_p2p1_amount_two, "to_amount":trigger_p2p1_amount_three},
                                             "trigger_criteria":{"symbol1_exchange":trigger_p1plusp2_symbol_one, "symbol2_exchange":trigger_p1plusp2_symbol_two,"operator":trigger_p1plusp2_maOperator, "from_amount":trigger_p1plusp2_amount_two, "to_amount":trigger_p1plusp2_amount_three},
                                             "exchange_id":exchange		
                                     }  }),
                                             dataType: "json",
                                             contentType: "application/json",
                                             success: function(result){
                                             if(result.status=="success")
                                             {
                                              alert(trigger_name + ' trigger created successfully');
                                           window.location.reload();
    
    
                                             }
                                         }
    
    
    
    
                                         });
    
                                 }
                                 else{
                                                     alert('Please fill all the field !');
                                             }
    
    
    
    
                                 
                                   }
                                   
                            
                         
                     }
                     // Function p1+p2 code end
        
          
        
            
            
            
      
        });    
    });