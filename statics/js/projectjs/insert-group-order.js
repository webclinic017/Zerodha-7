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
 
 
 
                       var trigger_name= $('#trigger_name').val();
                       
                       var order_buy_sell= $('#order_buy_sell').val();
                       var order_product_type=$('#order_product_type').val();
                       var order_type=$('#order_type').val();
                       var group_name=$('#group_name').val();
                       var amount=$('#amount').val();
                       var order_exchange=$('#order_exchange').val();
                       
                       orderprice();

                      
                       
                       // debugger;
                       if(trigger_name!=""){
 
 
                               $.ajax({
 
                                   url:"http://127.0.0.1:8000/insert_group_order/",
                                   method:"POST",
                                   data:JSON.stringify({
                                   "trigger": {
                                   "trigger_name":trigger_name
                                   },
                                   "order":{
                                   "buy_sell":order_buy_sell,
                                   "exchange_id":order_exchange,
                                   "group_name":group_name,
                                   "amount":amount,
                                   "product_type":order_product_type,
                                   "order_types":order_type,
                                   "price":order_price,
                                   "trigger_price":order_trigger_price
                                   
                                   }  
                                   }),
                                   dataType: "json",
                                   contentType: "application/json",
                                   success: function(result){
                                   if(result.status=="success")
                                   {
                                    alert(trigger_name + ' Order created successfully');
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