$(document).ready(function(){
        var order_price, order_trigger_price;
        var ordervalue= 0;
                 
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
           
     
                            
                          $('#placeorder').on('click', function(){
     
     
     
                           var group_name= $('#group_name').val();
                           var trigger_name= $('#trigger_name').val();
                           var order_buy_sell= $('#order_buy_sell').val();
                           var order_amount= $('#order_amount').val();
                           var order_product_type=$('#order_product_type').val();
                           var order_type=$('#order_type').val();
                           
                           orderprice();
                          
                           
                            debugger;
                           if(group_name!=""){
     
     
                                   $.ajax({
     
                                       url:"http://127.0.0.1:8000/insert_group_order/",
                                       method:"POST",
                                       data:JSON.stringify({
                                       "trigger": {
                                       "group_name":group_name,
                                       "trigger_name":trigger_name	
                               },
                               "order":{
                                       "buy_sell":order_buy_sell,
                                       "order_amount":order_amount,
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
                                        alert(group_name + ' Order created successfully');
                                        alert("Cronjob started");

                                        $.ajax({
                                       
                                       url:"http://127.0.0.1:8000/online_group_order/",

                                       success: function(result){
                                       if(result.status=="success")
                                       { 
                                        alert("Order executed successfully")
                                       }
                                       else
                                       {
                                        alert("Some error occured")
                                       }
                                     }

                                        });

                                        // window.location.reload();
     
                                       }
                                       else{
                                        alert('Error Occured');
                                        window.location.reload();
                                       }
                                   }
     
                                
     
       
                                   });
     
                           }
                           else{
                                   alert('Please fill all the field !');
                                       }
                                   });
});