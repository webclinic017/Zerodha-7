$(document).ready(function(){

  var group_name;
  var group_exchange_value;
  var group_exchange;
  var group_symbol;
  var output;
  var count = 0;
  
                               
  
  
  
  $('#addsymbol').click(function(){
  
    form_data();
  });
  
  function form_data(){
  
  group_name=$('#group_name').val();;
   
   group_exchange=$('#group_exchange').val();
   group_exchange_value=$('#group_exchange option:selected').data("trade");
   group_symbol=$('#group_symbol').val();
   
  
    if(group_name=="" || group_exchange=="Select Exchange" || group_symbol==""){
      alert("Please fill all the flied");
    }
    
    else{
     var count = count + 1;
      output = '<tr id="row_'+count+'" class="trade_data">';
  //    output += '<td>'+group_exchange+' <input type="hidden" name="group_exchange[]" id="group_exchange'+count+'" class="group_exchange" value="'+group_exchange_value+'" /></td>';
      output += '<td>'+group_symbol+' <input type="hidden" name="group_symbol[]" id="group_symbol'+count+'" class="group_symbol" value="'+group_symbol+'" /></td>';
      output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="'+count+'">Remove</button></td>';
      output += '</tr>';
      $('#group_data').append(output);
      $('#group_symbol').trigger("reset");
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
  
  
                                   $('#add_group_form').on('submit', function(event){
                                     
  
                                    event.preventDefault();  
                                    var group_name= $('#group_name').val();
                                    var count_data = 0;
                                    var jsonObj = [];
                                    $('.group_symbol').each(function(){
                                      count_data = count_data + 1;
                                      
                                      group_symbol=$(this).val();
                                      var instrument_token=$('#instrument_token').val();
                                    
                                      var item={};
                                    
                                      item["group_symbol"]= group_symbol;
                                       item["instrument_token"]= instrument_token ;
                                        item["group_exchange"]=group_exchange_value; 
                                      
                                      jsonObj.push(item);
                                      
                                     });
                                   debugger;
                                    if(count_data > 0){
                                     
  //                                   var form_data = $(this).serialize().replace(/%5B%5D/g, '').replace(/&/g, '","').replace(/%20/g, ' ').replace(/=/g, '":"').replace(/\\/g, "");
  //                                   form_data = '{"'+form_data+'"}';
                                     form_data= JSON.stringify(jsonObj); 
                                     console.log(form_data);
  
                                    
                                     debugger;
                                      
  
                                     
                                      alert('exchange :'+group_exchange_value)
                                     $.ajax({
       
                                         url:"http://127.0.0.1:8000/group_listing/company_add_update/"+group_name,
                                         method:"POST",
                                         data:JSON.stringify({
                                         "group": {
                                         "group_name":group_name, 
                                         "group_exchange":group_exchange_value         
                                         },
                                         "order":{
  //                                       "buy_sell":order_buy_sell,
  //                                       "quantity":order_qty,
  //                                       "product_type":order_product_type,
  //                                       "order_types":order_type,
  //                                       "symbol":order_symbol,
  //                                       "exchange_id":order_group_exchange,
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
                                          alert(' Order created successfully');
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