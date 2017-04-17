<?php

$db_user = 'root';
$db_pass = '';
$db_name = 'SBPROJECT';
$db_host = 'localhost';

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($mysqli->connect_errno) {
    die('Unable to connect to database [' . $db->connect_error . ']');
}

$first = $mysqli->real_escape_string($_POST['FIRSTNAME']);
$last = $mysqli->real_escape_string($_POST['LASTNAME']);
$email = $mysqli->real_escape_string($_POST['EMAIL']);
$pass = $mysqli->real_escape_string($_POST['PASSWRD']);

$sql = <<<SQL
	INSERT INTO test1 (FIRSTNAME, LASTNAME, EMAIL, PASSWRD) 
	VALUES ('$first','$last','$email','$pass')
SQL;

if (!$result = $mysqli->query($sql)) {
	die('There was an error running the query [' . $mysqli->error . ']');
}

?>