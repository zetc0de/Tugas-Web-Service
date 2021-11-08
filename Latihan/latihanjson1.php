<?php

$val = [
	"domain"=>"stmikelrahma.ac.id",
	"core"=>"Web Service Using Restful",
	"address"=>[
		"street"=>"Sisingamangaraja Street Number 76",
		"city"=>"Yogyakarta",
		"zipcode"=>"554321"
	],
	"phone"=>"(0274)55124"
];

$out = json_encode($val);
echo $out;