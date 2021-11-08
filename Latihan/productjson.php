<?php 


$user = "root";
$pass = "";
$server = "127.0.0.1";
$db = "northwind";

try {
	$conn = new PDO("mysql:host=$server;dbname=$db",$user,$pass);
	$conn->setAttribute(PDO::ATTR_ERRMODE,
						PDO::ERRMODE_EXCEPTION);
}catch(PDOException $e){
	echo "Connection Failed : ".$e->getMessage();
}

$sql = "SELECT * FROM customers";
$data = $conn->prepare($sql);
$data->execute();
$customers = [];
while ($row = $data->fetch(PDO::FETCH_OBJ)) {
	$customers[] = [
		"CustomerID"=>$row->CustomerID,
		"CompanyName"=>$row->CompanyName,
		"ContactName"=>$row->ContactName,
		"Address"=>$row->Address
	];
}

$abc = json_encode($customers);
print_r($abc);
?>