<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Smart Invest</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

  <!-- Page level plugin CSS-->
  <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin.css" rel="stylesheet">
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
       <a href="http://etechdemo.com/trading/dashboard/trading.php" style="color:white;padding-left:12px;"><i class="fas fa-plus" >  </i> Add Trigger</a>
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
<div class="container">
    <center>
         <div class="me-heading2">
                <!--<h1 style="background-color:#FFA500;font-size:32px">Trigger and Condition Set</h1>-->
            </div>
    </center>
    <div class="row">
<div class="col-sm-8">
        <!--<div class="me-blog-two me-padder-top-less me-padder-bottom" style="padding-bottom:30px">-->
        <div class="container" style="padding-top:30px">
            <div class="me-heading2"style="padding-left:-42px;padding-right:350px" >
                 <!---->
                <h1 style="border-bottom: 2px solid #ffb628;font-size:30px!important;background-color:#FFA500;padding:8px;"><center><b>Create Trigger</b></center></h1>
            </div>
        <!--</div>-->
        </div>
    
    <section>
        <form action="">
        <div class="container-fluid">
            <div class="row">
                 <!--<div class="col-lg-4"></div>-->
            <div class="col-lg-6">
                <div class="form-group">
                    <label for="trigger_condition" style="font-weight:700;font-size:16px"onclick="myFunction()">Trigger Condition</label>
                   <select class="form-control"  style="background-color:#E9ECEF;font-size:16px"  id="select_trigger">
                        <option>Select Trigger Condition</option>
         <option value="price">Price</option>
        <option  value="movingaverage"></option>Moving Average</option>
       <option  value="volume">Volume</option>
        <option  value="rsi">RSI</option>
 <option  value="parabolic_sar">Parabolic SAR</option>
            <option  value="p2">(P2-P1)/P1</option>
            <option  value="Triggerif_order_is_placed">Triggerif order is placed</option>
    </select>
                </div></div>
                 <div class="col-lg-4"></div>
                  
      <div class="col-lg-2"></div>
      
                 
                 <div class="col-lg-6">
                 <div class="form-group" >
      <label for="symbol"style="font-weight:700;font-size:16px">Symbol</label>
      <input  style="background-color:#E9ECEF;font-size:16px" type="text" class="form-control" id="smbl" placeholder="Symbol" name="smbl;" >
    </div></div>
    
    <div class="col-lg-4"></div>
       <div class="col-lg-2"></div>
     
      
   
     <div class="col-lg-6">
     <div class="form-group">
                    <label for="exchange"style="font-weight:700;font-size:16px">Exchange</label>
                     <select class="form-control"  style="background-color:#E9ECEF;font-size:16px;">
                         <option>Select Condition</option>
          <option>NSE</option>
          <option>BSE</option>
          <option>NFO</option>
          <option>MCX</option>
          </select>
                </div>
            </div>  
            
               <div class="col-lg-4"></div>
     <div class="col-lg-2"></div>
      
     
            <div class="col-lg-4" id="price-con" style="display: none">
     <div class="form-group">
                    <label for="price" style="font-weight:700;font-size:16px;">Price</label>
                     <select class="form-control">
          <option>Select Price Operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div> 
             <div class="col-lg-4"  id="price-am" style="margin-top:10px; display: none;">
                 <div class="form-group">
      <label for="price"></label>
      <input style="font-size:16px" type="text" class="form-control" id="smbl" placeholder="Amount" name="price" >
    </div></div>
            
            
      <div class="col-lg-4"style="display: none;"></div>
        <div class="col-lg-4"  style="display: none" id="moving_average">
     <div class="form-group">
                    <label for="moving_avg" style="font-weight:700;font-size:16px">Moving Average</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select Moving average</option>
          <option>MA</option>
          <option>(P-MA)/MA</option>
          <option>MA avg</option>
          <option>(P-MA)/MA avg</option>
          </select>
                </div>
            </div>     
            
            
               <div class="col-lg-4" style="display: none" id="moving_average_two"></div>
               
               <div class="col-lg-4" style="display: none" id="moving_average_one"></div>
         
      <div class="col-lg-3" style="display: none" id="moving_average_time_frame" >
     <div class="form-group">
                    <label for="time_frame" style="font-weight:700;font-size:16px">Time Frame</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select Time Frame</option>
          <option>1min</option>
          <option>2min</option>
          <option>3min</option>
          <option>4min</option>
          <option>5min</option>
          <option>10min</option>
          <option>15min</option>
          <option>30min</option>
          <option>Hour</option>
          <option>1D</option>
          <option>1W</option>
          <option>1M</option>
          </select>
                </div>
            </div>  
             
           <div class="col-lg-3" style="display: none" id="moving_average_period">
                 <div class="form-group">
      <label for="time_frame" style="font-weight:700;font-size:16px">Period</label>
      <input style="font-size:16px" type="text" class="form-control" id="period" placeholder="Period" name="period" >
    </div></div>
    
         <div class="col-lg-3" style="display: none" id="moving_average_field">
     <div class="form-group">
                    <label for="field" style="font-weight:700;font-size:16px">Field</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select Field</option>
          <option>Open</option>
          <option>High</option>
          <option>Low</option>
          <option>Close</option>
          </select>
                </div>
            </div>     
            
         <div class="col-lg-3" style="display: none" id="moving_average_type">
     <div class="form-group">
                    <label for="type" style="font-weight:700;font-size:16px">Type</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select Type</option>
          <option>Simple</option>
          <option>Exponential</option></option>
         </select>
                </div>
            </div>       
         
         <div class="col-lg-4" style="display: none">
     <div class="form-group">
                    <label for="ma" style="font-weight:700;font-size:16px">MA</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select MA Operator </option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div> 
        <div class="col-lg-4"  style="margin-top:10px; display: none;">
                 <div class="form-group">
      <label for="ma" ></label></label>
      <input style="font-size:16px" type="text" class="form-control" id="ma" placeholder="Amount" name="ma" >
    </div></div>
            
            
               <div class="col-lg-4" ></div>
            
              <div class="col-lg-4" style="display: none">
     <div class="form-group" >
                    <label for="p-ma" style="font-weight:700;font-size:16px">(P-MA)/MA</label>
                     <select class="form-control" style="font-size:16px">
                          <option>Select (P-MA)/MA operator </option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div> 
        <div class="col-lg-4"style="margin-top:10px; display: none" >
                 <div class="form-group">
      <label for="p-ma"></label>
      <input style="font-size:16px" type="text" class="form-control" id="p-ma" placeholder="Amount" name="p-ma" >
    </div></div>
     <div class="col-lg-4"></div>
    
       <div class="col-lg-4" style="display: none" >
                 <div class="form-group">
      <label for="ma_avg" style="font-weight:700;font-size:16px">MA avg</label>
      <input style="font-size:16px" type="text" class="form-control" id="ma_avg" placeholder="No. of candels" name="ma_avg" >
    </div></div>
            
              <div class="col-lg-4"style="margin-top:10px; display: none;" >
     <div class="form-group" style="font-size:16px">
                    <label for="ma_avg"></label>
                     <select class="form-control">
                            <option>Select MA avg operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>       
            
       <div class="col-lg-4"style="margin-top:10px; display: none;">
                 <div class="form-group" >
      <label  style=" style="font-size:16px" "for="ma_avg"></label>
      <input type="text" class="form-control" id="ma_avg" placeholder="Amount" name="ma_avg" >
    </div></div>
            
            <div class="col-lg-4" style="display: none;">
                 <div class="form-group">
      <label for="(p-ma)/ma_avg" style="font-weight:700;font-size:16px">(P-MA)/MA avg</label>
      <input style=" style="font-size:16px"" type="text" class="form-control" id="(P-MA)/MA avg" placeholder="No. of candels" name="(P-MA)/MA avg" >
    </div></div>
            
              <div class="col-lg-4" style="margin-top:10px; display: none;">
     <div class="form-group">
                    <label for="(P-MA)/MA_avg" ></label>
                     <select class="form-control"  style="font-size:16px">
                    <option>Select (P-MA)/MA avg Operator</option>      
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>       
            
       <div class="col-lg-4"style="margin-top:10px; display: none;">
                 <div class="form-group">
      <label for="(p-ma)/ma_avg"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="(p-ma)/ma_avg" placeholder="Amount" name="(p-ma)/ma_avg" >
    </div></div>
           
       
              <div class="col-lg-6" style="display: none;" id="volume_con">
     <div class="form-group">
                    <label for="volume" style="font-weight:700;font-size:16px">Volume</label>
                     <select class="form-control"  style="font-size:16px">
          <option>Volume</option>
          <option>Volume avg</option>
          </select>
                </div>
            </div> 
            
               <div class="col-lg-4" ></div>
               <div class="col-lg-2"></div>
             
             <div class="col-lg-6" style="display: none;" id="volume_con_time_frame">
     <div class="form-group">
                    <label for="time_frame" style="font-weight:700;font-size:16px">Time Frame</label>
                     <select class="form-control"  style="font-size:16px">
                            <option>Select Time Frame</option>
          <option>1min</option>
          <option>2min</option>
          <option>3min</option>
          <option>4min</option>
          <option>5min</option>
          <option>10min</option>
          <option>15min</option>
          <option>30min</option>
          <option>Hour</option>
          <option>1D</option>
          <option>1W</option>
          <option>1M</option>
          </select>
                </div>
            </div> 
            
             <div class="col-lg-4"></div>
             
               <div class="col-lg-2"></div>
               
              <div class="col-lg-4" style="display: none;">
     <div class="form-group">
                    <label for="volume" style="font-weight:700;font-size:16px">Volume</label>
                     <select class="form-control"  style="font-size:16px">
                         <option> Select Volume Operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div> 
           
        <div class="col-lg-4"style="margin-top:10px;display: none;">
                 <div class="form-group"style="display:none">
      <label for="volume"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="vol" placeholder="Amount" name="vol" >
    </div></div>
     <div class="col-lg-4"></div>
    
    <div class="col-lg-4" style="display: none;">
                 <div class="form-group">
      <label for="vol_avg" style="font-weight:700;font-size:16px">Volume avg</label>
      <input  style="font-size:16px" type="text" class="form-control" id="vol_avg" placeholder="Volume avg" name="avg_vol" >
    </div></div>
            
              <div class="col-lg-4" style="display: none;">
     <div class="form-group">
                    <label for="vol_avg"></label>
                     <select class="form-control"  style="font-size:16px">
                             <option>Select Volume avg Operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>       
              <div class="col-lg-4" style="display: none;">
                 <div class="form-group">
      <label for="vol_avg"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="vol_avg" placeholder="Amount" name="vol_avg" >
    </div></div>
    
            
              <div class="col-lg-4" style="display: none;" id="rsi_con">
     <div class="form-group">
                    <label for="rsi" style="font-weight:700;font-size:16px">RSI</label>
                     <select class="form-control"  style="font-size:16px">
                             <option>Select RSI Operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>  
            
              <div class="col-lg-4"style="margin-top:10px;display: none;" id="rsi_amount">
                 <div class="form-group">
      <label for="rsi"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="rsi" placeholder="Amount" name="rsi" >
    </div></div>
            
               <div class="col-lg-4" style="display: none;" id="rsi_con_one"></div>
             <div class="col-lg-4" style="display: none;" id="rsi_time_frame">
     <div class="form-group">
                    <label for="time_frame" style="font-weight:700;font-size:16px">Time Frame</label>
                     <select class="form-control"  style="font-size:16px">
                     <option>Select Time Frame</option>
          <option>1min</option>
          <option>2min</option>
          <option>3min</option>
          <option>4min</option>
          <option>5min</option>
          <option>10min</option>
          <option>15min</option>
          <option>30min</option>
          <option>Hour</option>
          <option>1D</option>
          <option>1W</option>
          <option>1M</option>
          </select>
                </div>
            </div>  
             
           <div class="col-lg-4" style="display: none;" id="rsi_period">
                 <div class="form-group">
      <label for=" Period" style="font-weight:700;font-size:16px">Period</label>
      <input  style="font-size:16px;" type="text" class="form-control" id="period" placeholder="Period" name="period" >
    </div></div>
    
    
               <div class="col-lg-4" style="display: none;" id="rsi_con_two"></div>
    
       <div class="col-lg-6" style="display: none;" id="parabolic_sar_con">
     <div class="form-group">
                    <label for="parabolic" style="font-weight:700;font-size:16px">Parabolic SAR</label>
                     <select class="form-control"  style="font-size:16p ;diplay:none">
                             <option>Select Parabolic SAR</option>
          <option>Parabolic SAR</option>
          <option>(P-ParSar)/ParSAR</option>
          </select>
                </div>
            </div>  
            
               <div class="col-lg-4" style="display: none;" id="parabolic_sar_con_one"></div>
               
               <div class="col-lg-2" style="display: none;" id="parabolic_sar_con_two"></div>
            
             <div class="col-lg-6" style="display: none;" id="parabolic_sar_time_frame">
     <div class="form-group">
                    <label for="time_frame" style="font-weight:700;font-size:16px;">Time Frame</label>
                     <select class="form-control"  style="font-size:16px">
                             <option>Select Time Frame</option>
          <option>1min</option>
          <option>2min</option>
          <option>3min</option>
          <option>4min</option>
          <option>5min</option>
          <option>10min</option>
          <option>15min</option>
          <option>30min</option>
          <option>Hour</option>
          <option>1D</option>
          <option>1W</option>
          <option>1M</option>
          </select>
                </div>
            </div>  
            
               <div class="col-lg-4" style="display: none;" id="parabolic_sar_time_frame_one"></div>
               <div class="col-lg-2" style="display: none;" id="parabolic_sar_time_frame_two"></div>
             <div class="col-lg-4" style="display: none;">
     <div class="form-group">
                    <label for="parabolic_sar" style="font-weight:700;font-size:16px;display:none">Parabolic SAR</label>
                     <select class="form-control"  style="font-size:16px">
                               <option>Select Parabolic SAR Operator </option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>  
            
              <div class="col-lg-4"style="margin-top:10px; display: none;" >
                 <div class="form-group">
      <label for="parabolic_Sar"></label>
      <input   style="font-size:16px"type="text" class="form-control" id="parabolic_sar" placeholder="Amount" name="parabolic_sar" >
    </div></div>
    
               <div class="col-lg-4"></div>
    
             <div class="col-lg-4" style="display: none;">
     <div class="form-group">
                    <label for="(p=parsar)" style="font-weight:700;font-size:16px">(P-ParSAR)/ParSAR</label>
                     <select class="form-control"  style="font-size:16px">
                             <option>Select (P-ParSAR)/ParSAR Operator</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>  
            
              <div class="col-lg-4"style="margin-top:10px;display: none;">
                 <div class="form-group">
      <label for="parsar"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="parsar" placeholder="Amount" name="parsar" >
    </div></div>
    
    
             
    
      <div class="col-lg-4"></div>
     <div class="col-lg-4" style="display: none;" id="(P2-P1)/P1_con">
     <div class="form-group">
                    <label for="(p2-p1)" style="font-weight:700;font-size:16px">(P2-P1)/P1</label>
                     <select class="form-control"  style="font-size:16px">
                            <option>Select (P2-P1)/P1</option>
          <option>>=</option>
          <option><=</option>
          <option>></option>
          <option><</option>
          <option>=</option>
          <option>between</option>
          </select>
                </div>
            </div>  
            
              <div class="col-lg-4" style="margin-top:10px;display: none;" id="(P2-P1)/P1_amount">
                 <div class="form-group">
      <label for="(p2-p1)"></label>
      <input  style="font-size:16px" type="text" class="form-control" id="p2-p1" placeholder="Amount" name="p2-p1" >
    </div></div>
    
   
     <div class="col-lg-4" style="display: none;" id="(P2-P1)/P1_con_one"></div>
   
              <div class="col-lg-4" style="display: none;" id="(P2-P1)/P1_symbol_one">
                 <div class="form-group">
      <label for="symbol1" style="font-weight:700;font-size:16px">Symbol1</label>
      <input  style="font-size:16px" type="text" class="form-control" id="symbl" placeholder="NSE,BSE,NFO,MCX" name="symbl" >
    </div></div>
    
    
              <div class="col-lg-4" style="display: none;" id="(P2-P1)/P1_symbol_two">
                 <div class="form-group">
      <label for="symbol2" style="font-weight:700;font-size:16px">Symbol2</label>
      <input  style="font-size:16px" type="text" class="form-control" id="symbl2" placeholder="NSE,BSE,NFO,MCX" name="symbl2" >
    </div></div>
    
    
     
     <div class="col-lg-4" style="display: none;" id="(P2-P1)/P1_con_two"></div>
              <div class="col-lg-6" style="display: none;">
                 <div class="form-group">
      <label for="order" style="font-weight:700;font-size:16px">Trigger if order is Place</label>
      <input  style="font-size:16px"type="text" class="form-control" id="order" placeholder="Trigger if order is Place" name="order" >
    </div></div>
     <div class="col-lg-4"></div> <div class="col-lg-2"></div>
        
    <div class="col-lg-4"></div>
    <div class="col-lg-4" style="font-weight:700;font-size:16px"> <button type="submit" class="btn btn-default" style="background-color:#E9ECEF;font-weight:700">Submit</button></div>
    <div class="col-lg-4"></div>
   </div>
       <br>
            
        </div>
        </span>
        </form>
    </section>
   
        <!--order-->
 <div class="col-sm-4" style="padding-bottom:10px;height:1000px" >
<!--<div class="" style="background-color:#f2f2f2;padding-bottom:10px">-->
<!--   <div class="container">-->
<!--       <div class="row">-->
        
<!--     <div class="col-lg-4"></div>-->
     
     
     <!--order condition-->
     
   
          <!--<div class="col-lg-4">-->
          <div class="" style="padding-top:30px;padding-left:0px;padding-right:0px" >
               <div class="container-fluid" ></div>
            <div class="me-heading2" >
                <h1 style="border-bottom: 2px solid #ffb628;font-size:30px!important;background-color:#FFA500;padding:8px;font-weight:500"><center><b>Order Condition</b></center></h1>
            </div>
        <!--</div>-->
        </div>
  <form action="">
  
      <div class="form-group">
      <label for="symbol" style="font-weight:700">Symbol</label>
      <input  style="background-color:#E9ECEF" type="text" class="form-control" id="smbl" placeholder="Symbol" name="smbl" >
    </div>
   
    <div class="form-group">
      <label for="buy" style="font-weight:700">Buy/Sell</label>
      <select class="form-control"  style="background-color:#E9ECEF">
          <option>Buy</option>
          <option>Sell</option>
          </select>
    </div>
     <div class="form-group">
      <label for="exchange" style="font-weight:700">Exchange</label>
      <select class="form-control"  style="background-color:#E9ECEF">
          <option>NSE</option>
          <option>BSE</option>
          <option>NFO</option>
          <option>MCX</option>
          </select>
    </div>
    <div class="form-group">
      <label for="qty" style="font-weight:700">Quantity</label>
      <input  style="background-color:#E9ECEF" type="text" class="form-control" id="qty" placeholder="Quantity" name="qty">
    </div>
     <div class="form-group">
      <label for="product_type" style="font-weight:700">Product Type</label>
      <select class="form-control"  style="background-color:#E9ECEF">
          <option>NRML</option>
          <option>MIS</option>
          </select>
    </div>
    <div class="form-group">
      <label for="order" style="font-weight:700">Order</label>
      <select class="form-control"  style="background-color:#E9ECEF">
          <option>Market</option>
          <option>Limit</option>
          <option>SL</option>
          <option>SL-M</option>
          </select>
    </div>
      <div class="form-group">
      <label for="trigger" style="font-weight:700">Price</label>
      <input   style="background-color:#E9ECEF"type="text" class="form-control" id="trigger" placeholder="Price" name="trigger">
    </div>
      <div class="form-group">
      <label for="price" style="font-weight:700"> Trigger Price:</label>
      <input  style="background-color:#E9ECEF" type="text" class="form-control" id="price" placeholder=" Trigger Price" name="price">
    </div>
   <br/>
    <button type="submit" class="btn btn-default" style="font-weight:700;background-color:#E9ECEF">Submit</button>
  </form>
 
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
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Page level plugin JavaScript-->
  <script src="vendor/chart.js/Chart.min.js"></script>
  <script src="vendor/datatables/jquery.dataTables.js"></script>
  <script src="vendor/datatables/dataTables.bootstrap4.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin.min.js"></script>

  <!-- Demo scripts for this page-->
  <script src="js/demo/datatables-demo.js"></script>
  <!--<script src="js/demo/chart-area-demo.js"></script>-->
 <script src="dashboard/js/custom.js"></script>
 <script type="text/javascript">
    $(function () {
        $("#select_trigger").change(function () {
            if ($(this).val() == "price") {
                $("#price-con").show();
                $("#price-am").show();
            } else {
                $("#price-con").hide();
                 $("#price-am").hide();
            }
            
            if ($(this).val() == "movingaverage") {
                $("#moving_average").show();
                $("#moving_average_one").show();
                $("#moving_average_two").show();
                $("#moving_average_time_frame").show();
                $("#moving_average_type").show();
                $("#moving_average_period").show();
                $("#moving_average_field").show();
                
            } else {
                $("#moving_average").hide();
                 $("#moving_average_one").hide();
                $("#moving_average_two").hide();
                $("#moving_average_time_frame").hide();
                $("#moving_average_type").hide();
                $("#moving_average_period").hide();
                $("#moving_average_field").hide();
                 
            }
            
            if ($(this).val() == "volume") {
                $("#volume_con").show();
                $("#volume_con_time_frame").show();
            } else {
                $("#volume_con").hide();
                 $("#volume_con_time_frame").hide();
            }
            
             if ($(this).val() == "rsi") {
                $("#rsi_con").show();
                $("#rsi_amount").show();
                $("#rsi_con_one").show();
                $("#rsi_time_frame").show();
                $("#rsi_period").show();
                $("#rsi_con_two").show();
                
                
            } else {
               $("#rsi_con").hide();
                $("#rsi_amount").hide();
                $("#rsi_con_one").hide();
                $("#rsi_time_frame").hide();
                $("#rsi_period").hide();
                $("#rsi_con_two").hide();
            }
            
            if ($(this).val() == "parabolic_sar") {
                $("#parabolic_sar_con").show();
                $("#parabolic_sar_con_one").show();
                $("#parabolic_sar_con_two").show();
                $("#parabolic_sar_time_frame").show();
                $("#parabolic_sar_time_frame_one").show();
                $("#parabolic_sar_time_frame_two").show();
            } else {
                $("#parabolic_sar_con").hide();
                $("#parabolic_sar_con_one").hide();
                $("#parabolic_sar_con_two").hide();
                $("#parabolic_sar_time_frame").hide();
                $("#parabolic_sar_time_frame_one").hide();
                $("#parabolic_sar_time_frame_two").hide();
            }
            
             if ($(this).val() == "p2") {
                $("#(P2-P1)/P1_con").show();
                $("#(P2-P1)/P1_con_amount").show();
                $("#(P2-P1)/P1_con_one").show();
                $("#(P2-P1)/P1_con_two").show();
                $("#(P2-P1)/P1_symbol_one").show();
                $("#(P2-P1)/P1_con_symbol_two").show();
            } else {
                $("#(P2-P1)/P1_con").hide();
                $("#(P2-P1)/P1_con_amount").hide();
                $("#(P2-P1)/P1_con_one").hide();
                $("#(P2-P1)/P1_con_two").hide();
                $("#(P2-P1)/P1_symbol_one").hide();
                $("#(P2-P1)/P1_con_symbol_two").hide();
            }
           
            
            
        });
    });
</script>

 </script>
 

</body>

Success!
</html>
