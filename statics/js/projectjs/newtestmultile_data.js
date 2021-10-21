$(document).ready(function(){

  var trigger_name;
  var order_buy_sell;
  var order_buy_sell_value;
  var order_exchange;
  var order_exchange_value;
  var order_symbol;
  var order_qty='';
  var order_product_type;
  var order_product_type_value;
  var order_type;
  var order_type_value;
  
  var order_price;
  var order_trigger_price;
  var output;
  var count = 0;
                                function orderprice(){
                                       
                                        
                                       
                                       if($('#order_type').val()=='Market'){
                                        
                                      order_trigger_price="0";
                                      order_price="0";
                                      
                                    }
                                    else if($('#order_type').val()=='Limit'){
                                        
                                      order_price=$('#order_price').val();  
                                      order_trigger_price="0";
                                      
                                      
                                    }
                                    else if($('#order_type').val()=='SL'){
                                        
                                     order_price=$('#order_price').val();  
                                     order_trigger_price=$('#order_trigger_price').val();
                                       
                                    }
                                     else if($('#order_type').val()=='SL-M'){
                                        
                                     order_trigger_price=$('#order_trigger_price').val();  
                                     order_price="0";
                                      
                                    }
                                       
                                   }
  
  
  
  $('#placeorder').click(function(){
  
    form_data();
  });
  
  function form_data(){
   trigger_name=$('#trigger_name').val();
   order_buy_sell=$('#order_buy_sell').val();
   order_exchange=$('#order_exchange').val();
   order_buy_sell_value=$('#order_buy_sell option:selected').data("trade");
   order_exchange_value=$('#order_exchange option:selected').data("trade");
   order_symbol=$('#order_symbol').val();
   order_qty=$('#order_qty').val();
   order_product_type=$('#order_product_type').val();
   order_type=$('#order_type').val();
   order_product_type_value=$('#order_product_type option:selected').data("trade");
   order_type_value=$('#order_type option:selected').data("trade");
   
   order_price=$('#order_price').val();
   order_trigger_price=$('#order_trigger_price').val();
   orderprice();

  if (order_buy_sell=="Select buy/sell") {

    alert("Please Select Buy/Sell")

  }

  else if (order_exchange=="Select Exchange") {

    alert("Please Select Exchange");
    
  }

  else if (order_product_type=="Select product type") {

    alert("Please Select Product Type")
    
  }

  else if (order_type=="Select order type") {

    alert("Please Select Order Type")
    
  }

   else{
    
      
     
      output = '<tr id="row_'+count+'" class="trade_data">';
      output += '<td>'+order_buy_sell+' <input type="hidden" name="order_buy_sell[]" id="order_buy_sell'+count+'" class="order_buy_sell" value="'+order_buy_sell_value+'" /></td>';
      output += '<td>'+order_exchange_value+' <input type="hidden" name="order_exchange[]" id="order_exchange'+count+'" value="'+order_exchange+'" /></td>';
      output += '<td>'+order_symbol+' <input type="hidden" name="order_symbol[]" id="order_symbol'+count+'" class="" value="'+order_symbol+'" /></td>';
      output += '<td>'+order_qty+' <input type="hidden" name="order_qty[]" id="order_qty'+count+'" class="order_qty" value="'+order_qty+'" /></td>';
      output += '<td>'+order_product_type+' <input type="hidden" name="order_product_type[]" id="order_product_type'+count+'" class="" value="'+order_product_type_value+'" /></td>';
      output += '<td>'+order_type+' <input type="hidden" name="order_type[]" id="order_type'+count+'" value="'+order_type_value+'" /></td>';
    //   output += '<td>'+order_price+' <input type="hidden" name="order_price[]" id="order_price'+count+'" class="" value="'+order_price+'" /></td>';
      output += '<td>'+order_trigger_price+' <input type="hidden" name="trigger_price[]" id="order_trigger_price'+count+'" value="'+order_trigger_price+'" /></td>';
      output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="'+count+'">Remove</button></td>';
      output += '</tr>';
      $('#user_data').append(output);
      $('#orderform').trigger("reset");
      count=count+1;
  
  }
}
  
  
    $(document).on('click', '.remove_details', function(){
    var row_id = $(this).attr("id");
    if(confirm("Are you sure you want to remove this row data?"))
    {
     $('#row_'+row_id+'').remove();
     }
    else
    {
     return false;
    }
   });
  
  
                                   $('#user_form').on('submit', function(event){
                                     
  
                                    event.preventDefault();  
  //                                  var count_data = 0;
                                    var jsonObj = [];
                                    //var rowctr = $('.trade_data').rowCount();
                                    var rowTradeDataLength = $('.trade_data').length;
                                    var i=0;
                                    for(i=0; i<rowTradeDataLength; i++){
                                        
                                       order_buy_sell=$('#order_buy_sell'+i).val(); 
                                       order_qty=$('#order_qty'+i).val();
                                       order_product_type=$('#order_product_type'+i).val();
                                       order_type=$('#order_type'+i).val();
                                       order_exchange=$('#order_exchange'+i).val();
                                       order_symbol=$('#order_symbol'+i).val();
                                       order_price=$('#order_price'+i).val();
                                       order_trigger_price=$('#order_trigger_price'+i).val();
                                       
                                    //   debugger;
                                       
                                        var item={};
                                    
                                    item["buy_sell"]= order_buy_sell;
                                    item["quantity"]= order_qty;
                                    item["product_type"]= order_product_type;http://127.0.0.1:8000/
                                    item["order_types"]= order_type;
                                    item["exchange_id"]= order_exchange;
                                    item["symbol"]= order_symbol;
                                    item["price"]=order_price;
                                    item["trigger_price"]=order_trigger_price;
  //                                     console.log("**" + order_buy_sell + " order_qty" + order_qty);
                                       jsonObj.push(item); 
                                    }
  //                                  $('tr').each(function(){
  //                                    count_data = count_data + 1;
  //                                    
  //                                    
  //                                    order_buy_sell=$(this).val();
  //                                    order_qty=$(this).val();
  //                                    
  //                                   
  //                                  
  //                                  
  //                                  
  //                                   jsonObj.push(item);
  //                                   });
 
                                    if(rowTradeDataLength > 0){
                                    
                                     
                                     var form_data;
  //                                   form_data = $(this).serialize().replace(/%5B%5D/g, '').replace(/&/g, '","').replace(/%20/g, ' ').replace(/=/g, '":"');
  //                                   form_data = '{"'+form_data+'"}';
                                     form_data= JSON.stringify(jsonObj); 
                                     console.log(form_data);
                                     

       
                                     $.ajax({ 
       
                                         url:"http://127.0.0.1:8000/save_multiple_order/",
                                         method:"POST",
                                         data:JSON.stringify({
                                         "trigger": {
                                         "trigger_name":trigger_name
                                         },
                                         "order":{
  //                                       "buy_sell":order_buy_sell,
  //                                       "quantity":order_qty,
  //                                       "product_type":order_product_type,
  //                                       "order_types":order_type,
  //                                       "symbol":order_symbol,
  //                                       "exchange_id":order_exchange,
  //                                       "price":order_price,
  //                                       "trigger_price":order_trigger_price
                                          form_data
                                         
                                         } 
                                         }),
  //                                       data:JSON.stringify({form_data}),
                                         dataType: "json",
                                         contentType: "application/json",
 
                                         success: function(result){
                                         if(result.status=="success")
                                         {
                                          alert(trigger_name + ' order created successfully');
                                          //alert("Cronjob started");

                                          $.ajax({
                                         
                                        url:"http://127.0.0.1:8000/onlinetrigger/",

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