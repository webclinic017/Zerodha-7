<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Smart Invest</title>
   {% load static %}
  <!-- Custom fonts for this template-->
  <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}" rel="stylesheet" type="text/css">

  <!-- Page level plugin CSS-->
  <link href="{% static 'vendor/datatables/dataTables.bootstrap4.css' %}" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="{% static 'css/sb-admin.css' %}" rel="stylesheet">
<!--<link href="css/login.css" rel="stylesheet">-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body id="page-top">

  <nav class="navbar navbar-expand navbar-dark bg-dark static-top">

    <a class="navbar-brand mr-1" href="dashboard.php">Smart Invest</a>

    <button class="btn btn-link btn-sm text-white order-1 order-sm-0" id="sidebarToggle" href="#">
      <i class="fas fa-bars"></i>
    </button>

    <!-- Navbar Search -->
    <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0">
      <div class="input-group">
        <!--<input type="text" class="form-control" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2">-->
        <div class="input-group-append">
          <!--<button class="btn btn-primary" type="button">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </form>

    <!-- Navbar -->
    <ul class="navbar-nav ml-auto ml-md-0">
<!--      <li class="nav-item dropdown no-arrow mx-1">
        <a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="fas fa-bell fa-fw"></i>
          <span class="badge badge-danger">9+</span>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="alertsDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>-->
      <li class="nav-item dropdown no-arrow mx-1">
        <a class="nav-link dropdown-toggle" href="#" id="messagesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <!--<i class="fas fa-envelope fa-fw"></i>-->
          <p style="font-size:20px">Krishnakant</p>
          <!--<span class="badge badge-danger"></span>-->
        </a>
<!--        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="messagesDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>-->
      <li class="nav-item dropdown no-arrow">
        <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="fas fa-user-circle fa-fw"></i>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
          <!--<a class="dropdown-item" href="#">Settings</a>-->
          <!--<a class="dropdown-item" href="#">Activity Log</a>-->
          <div class="dropdown-divider"></div>
          <!--<a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">Logout</a>-->
        </div>
      </li>
    </ul>

  </nav>

  <div id="wrapper">

    <!-- Sidebar -->
 <ul class="sidebar navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="dashboard.php">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>Dashboard</span>
    
   
    </a>
      </li>
      <!--<li class="nav-item dropdown">-->
        <!--<a class="nav-link dropdown-toggle" href="#" id="pagesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">-->
         
          <!--<span>Pages</span>-->
        </a>
        <!--<div class="dropdown-menu" aria-labelledby="pagesDropdown">-->
        <!--<h6 class="dropdown-header">Menu</h6>-->
        <a href="trading.php" style="color:white;padding-left:12px;"><i class="fas fa-plus" >  </i> Add Trigger</a>
   <!--<a class="dropdown-item" href="search.php">Search</a>-->
<!--          <a class="dropdown-item" href="forgot-password.html">Forgot Password</a>
          <div class="dropdown-divider"></div>
          <h6 class="dropdown-header">Other Pages:</h6>
          <a class="dropdown-item" href="404.html">404 Page</a>
          <a class="dropdown-item" href="blank.html">Blank Page</a>-->
        <!--</div>-->
<!--     </li>
     <li class="nav-item">
        <a class="nav-link" href="charts.html">
          <i class="fas fa-fw fa-chart-area"></i>
          <span>Charts</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
      </li>-->
    </ul>

    <div id="content-wrapper">
<!--table start-->
<div class="panel-wrap">
  <div class="panel">
<!--<div class="container">-->
<!--    <center>-->
         <!--<div class="me-heading2">-->
                <!--<h1 style="background-color:#FFA500;font-size:32px">Trigger and Condition Set</h1>-->
         <!--   </div>-->
<!--    </center>-->
<!--    <div class="row">-->
<!--<div class="col-sm-8">-->
        <!--<div class="me-blog-two me-padder-top-less me-padder-bottom" style="padding-bottom:30px">-->
<!--        <div class="container" style="padding-top:30px">-->
           
           
                 <!---->
<!--                  <div class="col-sm-6" style="margin-right:10px;padding-left:10px">-->
<!--                <h1 style="border-bottom: 2px solid #ffb628;font-size:30px!important;background-color:#FFA500;padding:8px;padding-right:30px"><center><b> Create Trigger</b></center></h1>-->
<!--            </div>-->
        <!--</div>-->
<!--        </div>-->
    <!--table-->
     <div class="card mb-3">
          <div class="card-header">
           
           <h2>OPEN ORDERS(x)</h2></div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-bordered" id="tableOpenOrders" width="100%" cellspacing="0">
                <thead>
                  <tr>
                       <th style="background-color:#FFA500">S.no</th>
        <th  style="background-color:#FFA500">Date and Time</th>
        <th  style="background-color:#FFA500">Trigger</th>
         <th  style="background-color:#FFA500">Trigger Instrument</th>
          <th  style="background-color:#FFA500">Trigger Condition</th>
           <th  style="background-color:#FFA500"787>Order Instrument</th>
            <th  style="background-color:#FFA500">BUY/SELL</th>
             <th  style="background-color:#FFA500">Qty.</th>
              <th  style="background-color:#FFA500">Product type</th>
               <th  style="background-color:#FFA500;"></th>
                 </tr>
                </thead>
                <tbody>
     </tbody>
              </table>
            </div>
          </div>
          <!--<div class="card-footer small text-muted"></div>-->
        </div>
<!--end table1-->
<!--table2-->
  <div class="card mb-3">
          <div class="card-header">
           
           <h2>EXECUTED ORDERS(X)</h2></div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-bordered" id="tableExecutedOrders" width="100%" cellspacing="0">
                <thead>
                  <tr>
        <th style="background-color:#FFA500">S.no</th>
        <th  style="background-color:#FFA500">Date and Time</th>
        <th  style="background-color:#FFA500">Trigger</th>
         <th  style="background-color:#FFA500">Trigger Instrument</th>
          <th  style="background-color:#FFA500">Trigger Condition</th>
           <th  style="background-color:#FFA500">Order Instrument</th>
            <th  style="background-color:#FFA500">BUY/SELL</th>
             <th  style="background-color:#FFA500">Qty.</th>
              <th  style="background-color:#FFA500">Product type</th>
               <th  style="background-color:#FFA500"></th>
      </tr>
        </thead>
        <tbody>
        </tbody>
              </table>
            </div>
          </div>
          <!--<div class="card-footer small text-muted"></div>-->
        </div>
<!--end table2-->
     
      <!-- Sticky Footer -->
      <footer class="sticky-footer">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright ©Smart Invest 2020</span>
          </div>
        </div>
      </footer>

    </div>
    <!-- /.content-wrapper -->

  </div>
  <!-- /#wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Logout Modal-->
  <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
          </button>
        </div>
        <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
          <a class="btn btn-primary" href="login.html">Logout</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript-->
  <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>
  <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>

  <!-- Core plugin JavaScript-->
  <script src="{% static 'vendor/jquery-easing/jquery.easing.min.js' %}"></script>

  <!-- Page level plugin JavaScript-->
  <script src="{% static 'vendor/chart.js/Chart.min.js' %}"></script>
  <script src="{% static 'vendor/datatables/jquery.dataTables.js' %}"></script>
  <script src="{% static 'vendor/datatables/dataTables.bootstrap4.js' %}"></script>

  <!-- Custom scripts for all pages-->
  <script src="{% static 'js/sb-admin.min.js' %}"></script>

  <!-- Demo scripts for this page-->
  <script src="{% static 'js/demo/datatables-demo.js' %}"></script>
  <!--<script src="js/demo/chart-area-demo.js"></script>-->
 <script src="dashboard/js/custom.js"></script>
 <script>
 $(document).ready(function(){
           $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/getdashboardorders",
            success: function(result){
                if(result.status=="success")
                {
                    
                var openOrders = $.grep(result.content, function(v) {
              return v.is_active==true
            });
                 
                $.each(openOrders, function(index, value){
            $("#tableOpenOrders").append('<tr><tr> <td>'+(index+1)+'</td><td>'+value.created_on+'</td> <td>'+value.trigger_name+'</td><td>'+value.symbol+'</td><td>'+value.trigger_condition+'</td><td>'+value.symbol+'</td> <td>'+value.buy_sell+'</td> <td>'+value.quantity+'</td> <td>'+value.product_type+'</td> <td><button type="button" class="btn" style="background-color:#E9ECEF;padding-left:35px;padding-right:36px">Open</button></td></tr>');
             });
             
             
             var executedOrders = $.grep(result.content, function(v) {
              return v.is_executed==true || v.is_cancelled==true
            });
                 var status='';
                $.each(executedOrders, function(index, value){
                    if(value.is_executed==false && value.is_cancelled==true)
                    {
                        status='<button type="button" class="btn" style="background-color:red;padding-left:35px;padding-right:36px">Cancelled</button>';
                    }
                    else
                    {
                         status='<button type="button" class="btn" style="background-color:green;padding-left:35px;padding-right:36px">Completed</button>';
                    }
            $("#tableExecutedOrders").append('<tr><tr> <td>'+(index+1)+'</td><td>'+value.executed_on+'</td> <td>'+value.trigger_name+'</td><td>'+value.symbol+'</td><td>'+value.trigger_condition+'</td><td>'+value.symbol+'</td> <td>'+value.buy_sell+'</td> <td>'+value.quantity+'</td> <td>'+value.product_type+'</td> <td>'+status+'</td></tr>');
             });
                 
                }
            }
        });
        });
 </script>

</body>

</html>
