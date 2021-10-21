<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>


    
$(document).ready( "load", function(){
    console.log( "window loaded" );
$.ajax({
    type: "GET",
    url: "https://kite.trade/connect/login?api_key=ib196gkbrmuqnoer&v=3",
    success: function(result){
        if(result.status=="success")
{
 window.location.replace(result.content)
}
    }
});
});