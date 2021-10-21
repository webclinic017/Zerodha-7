 <?php

	session_start();
	include_once 'connection.php';

        $username= $_POST['username'];
        $password = $_POST['password'];

		$query = "SELECT * FROM registration WHERE username='".$username."' and password='".$password."'";
		
	$result=mysqli_query($conn, $query);
	
	// if (!$result) {   printf("Error: %s\n", mysqli_error($conn));   exit();}
	
	$row=mysqli_fetch_array($result);
	

        if ($row['username']==$username && $row['password']== $password){
        	
			echo "<script type='text/javascript'>alert('You successfully logged In'),location.href='dashboard.php';</script>".$_SESSION['username']=$username;
	
	}
		else{
			
			echo "<script type='text/javascript'>alert('Invalid Login'),location.href='index.php';</script>".mysqli_error($conn);
			
			
			
		}

?>			
	
