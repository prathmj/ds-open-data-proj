<?php
session_start();

$db_user = 'root';
$db_pass = '';
$db_name = 'SBCC';
$db_host = 'localhost';

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($mysqli->connect_errno) {
    die('Unable to connect to database [' . $db->connect_error . ']');
}

$email = $mysqli->real_escape_string($_SESSION['EMAIL']);

$message = $mysqli->real_escape_string($_POST['MESSAGE']);

$sql = <<<SQL
	UPDATE users
	SET MESSAGE = '$message' 
	WHERE EMAIL = '$email';
SQL;

if (!$result = $mysqli->query($sql)) {
	die('There was an error running the query [' . $mysqli->error . ']');
}

exec("../emails.py '$email'")
?>