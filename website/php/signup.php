<?php

$db_user = 'root';
$db_pass = '';
$db_name = 'SBCC';
$db_host = 'localhost';

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($mysqli->connect_errno) {
    die('Unable to connect to database [' . $db->connect_error . ']');
}

$first = $mysqli->real_escape_string($_POST['FIRSTNAME']);
$last = $mysqli->real_escape_string($_POST['LASTNAME']);
$email = $mysqli->real_escape_string($_POST['EMAIL']);
$pass = $mysqli->real_escape_string($_POST['PASSWRD']);
$ccm = $mysqli->real_escape_string($_POST['CCMEMB']);
$iccm = (int)$ccm;

$sql = <<<SQL
	INSERT INTO users (FIRSTNAME, LASTNAME, EMAIL, CCMEMB, PASSWRD) 
	VALUES ('$first','$last','$email',$iccm,'$pass')
SQL;

if (!$result = $mysqli->query($sql)) {
	die('There was an error running the query [' . $mysqli->error . ']');
}

?>