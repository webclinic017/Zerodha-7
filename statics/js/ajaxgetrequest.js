<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

$(document).ready(function(){
  $("button").click(function(){
    $.get("127.0.0.1:8000/login/", function(status, content){
      alert("status: " + status + "\ncontent: " + content);
    });
  });
});
