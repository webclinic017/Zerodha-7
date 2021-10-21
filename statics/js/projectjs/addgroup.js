$(document).ready(function(){

  var group_name;
  var group_exchange_value;
  var group_exchange;
  var group_symbol;
  var group_instrument_token;
  var output;
  var count = 0;
                               
  
  
  
  $('#addsymbol').click(function(){
  
    form_data();
  });
  
  function form_data(){
  
   group_name=$('#group_name').val();
   
   group_exchange=$('#group_exchange').val();
   group_exchange_value=$('#group_exchange option:selected').data("trade");
   group_symbol=$('#group_symbol').val();
   group_instrument_token=$('#group_instrument_token').val();
  
   
  
    if(group_name=="" || group_exchange=="Select Exchange" || group_symbol==""){
      alert("Please fill all the flied");
    }
    
    else{
  
      output = '<tr id="row_'+count+'" class="trade_data">';
      output += '<td>'+group_symbol+' <input type="hidden" name="group_symbol[]" id="group_symbol'+count+'" class="group_symbol" value="'+group_symbol+'" /></td>';
      output += '<td style="display: none;">'+group_instrument_token+' <input type="hidden" name="group_instrument_token[]" id="group_instrument_token'+count+'" class="group_instrument_token" value="'+group_instrument_token+'" /></td>';
      output += '<td><button type="button" name="remove_details" class="btn btn-danger btn-xs remove_details" id="'+count+'">Remove</button></td>';
      output += '</tr>';
      $('#group_data').append(output);
      $('#group_symbol').trigger("reset");
     
      count=count+1;
  
  }
  }
    
    
    $(document).on('click', '.remove_details', function(){
    var row_id = $(this).attr("id");


  if( confirm("Are you sure you want to remove this row data?"))
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
  //                                  var count_data = 0;
                                 
                                    //var rowctr = $('.trade_data').rowCount();
                                    var rowTradeDataLength = $('.trade_data').length;
                                    var rowCount = $('table#group_data tr:last').index();
                                    var i=0;
 
                                     var groupsymbol = [];
                                     var groupinstrument = [];
                                    
                                      $('.group_symbol').each(function(){
                                         groupsymbol.push($(this).val());
                                           });
                                             $('.group_instrument_token').each(function(){
                                                groupinstrument.push($(this).val());
                                                  });
                                           debugger;
  

  //                               
                                    if(rowTradeDataLength > 0){

                                     $.ajax({
       
                                         url:"http://127.0.0.1:8000/create_group/",
                                         method:"POST",
                                         data:JSON.stringify({
                                          "group": {"group_name":group_name, 
                                          "group_exchange":group_exchange_value,
                                           "group_symbol":groupsymbol,
                                           "group_instrument_token":groupinstrument
                                         }
                                       
                                         }),
  
  //                                       
                                         dataType: "json",
                                         contentType: "application/json",
  
                                         
                                         success: function(result){
                                         if(result.status=="success")
                                         {
                                          alert(group_name + ' group created successfully');
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