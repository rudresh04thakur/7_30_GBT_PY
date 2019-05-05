<?php

$con = mysql_connect("localhost","root","demo_db")
$fields="",
$values="";
//fname,lname,password,)values('')"
for each ($_POST as $ key => $value){
$fields = $key. "";
$values = "'" .$value . "; ";
}
$str = "insert into users (".substr($fields 0
str len ($fields)-i).")values (".substr($.substr($values,o, strlen ($values)-i).")";
//echo $str;
$result = mysql - query ($con, $str) or die/mysql.em(echo = $con)
?>
