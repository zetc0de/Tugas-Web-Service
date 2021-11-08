<?php 

header('Content-Type: application/json; charset=utf-8');

$method = $_SERVER['REQUEST_METHOD'];

if ($method != 'GET') {
	http_response_code(405);
	$msg = ["Message"=>"You are using $method Method"];
	$msg = json_encode($msg);
	print_r($msg);
	die();
}



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
		"ContactTitle"=>$row->ContactTitle,
		"Address"=>$row->Address,
		"City"=>$row->City
	];
}


$data = ["took"=>$_SERVER["REQUEST_TIME_FLOAT"]];
$data += ["code"=>200];
$data += ["message"=>"Response successfully"];
$data += ["data"=>$customers];

$resp = json_encode($data);
print_r($resp);



?>