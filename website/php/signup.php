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

$_SESSION['EMAIL'] = $email;

switch($iccm) {
		case 1:
			header("Location: ../scott.html");
			break;
		case 2:
			header("Location: ../williams-preston.html");
			break;
		case 3:
			header("Location: ../kelly.html");
			break;
		case 4:
			header("Location: ../broden.html");
			break;
		case 5:
			header("Location: ../varner.html");
			break;
		case 6:
			header("Location: ../davis.html");
			break;
		default:
			header("Location: ../login.html");
			break;
	}

?>