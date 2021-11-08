<?php 
header('Content-Type: text/xml');

$val = [
	"domain"=>"stmikelrahma.ac.id",
	"core"=>"Web Service Using Restful",
	"address"=>"Sisingamangaraja Street Number 76,Yogyakarta,554321",
	"phone"=>"(0274)55124"
];


$xml = new SimpleXMLElement("<xml/>");

foreach ($val as $key => $val) {
	$track = $xml->addChild($key,$val);
	
}

print($xml->asXML());


?>