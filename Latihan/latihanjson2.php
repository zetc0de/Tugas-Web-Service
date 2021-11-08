<?php
$json = '{
	"domain":"stmikelrahma.ac.id",
	"core":"Web Service Using Restful",
	"address":{
		"street":"Sisingamangaraja Street Number 76",
		"city":"Yogyakarta",
		"zipcode":"554321"
	},
	"phone":"(0274)55124"
}';
echo "<pre>";
print_r(json_decode($json));

?>