<?php

$db_user = 'root';
$db_pass = '';
$db_name = 'SBCC';
$db_host = 'localhost';

$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($mysqli->connect_errno) {
    die('Unable to connect to database [' . $db->connect_error . ']');
}

$email = $mysqli->real_escape_string($_POST['EMAIL']);
$pass = $mysqli->real_escape_string($_POST['PASSWRD']);

$sql = <<<SQL
	SELECT * FROM users
	WHERE EMAIL = '$email' and PASSWRD='$pass'
SQL;

if (!$result = $mysqli->query($sql)) {
	die('There was an error running the query [' . $mysqli->error . ']');
}

$count = $result->num_rows;

if ($count == 1){
	$_SESSION['EMAIL'] = $email;

	$sql2 = <<<SQL
		SELECT CCMEMB FROM users
		WHERE EMAIL = '$email' and PASSWRD='$pass'
SQL;

	if (!$result = $mysqli->query($sql2)) {
		die('There was an error running the query [' . $mysqli->error . ']');
	}

	$ccmemb = $result;

	switch($ccmemb) {
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
}
else {
	printf('Invalid Login Credentials');
}


?>