<?php 

$array = array(
	"0" => array(
		"id" => "USR1",
		"name" => "Mukhammad",
		"company" => "Link"
	),
	"1" => array(
		"id" => "USR2",
		"name" => "Khabib",
		"company" => "Aja"
	),
	"2" => array(
		"id" => "USR3",
		"name" => "Risky",
		"company" => "UII"
	)	
);

$json = json_encode(array('data'=>$array));
// print_r($json);
if (file_put_contents('data.json', $json))
	echo "File Berhasil Dibuat!";
else
	echo "File Gagal Dibuat!";
?>