<?php
ini_set("error_reporting", E_ALL);
ini_set("display_errors", 1);
ini_set("display_startup_errors", 1);
ini_set('default_socket_timeout', 600);
ini_set('max_execution_time', 0);
chdir(dirname(__FILE__));
require_once(dirname(__FILE__) . "/webserviceApi.class.php");

echo getcwd() . "\n";
$str = file_get_contents('../params.json');
$json_data = json_decode($str, true);
$EStoken = $json_data['params']['EStoken'];
$ITtoken = $json_data['params']['ITtoken'];
$FRtoken = $json_data['params']['FRtoken'];
$AUtoken = $json_data['params']['AUtoken'];
$SGtoken = $json_data['params']['SGtoken'];
$IDtoken = $json_data['params']['IDtoken'];
$wsES = new webserviceApi("ES@karmaresponse.com",$EStoken);
$listsES = $json_data['params']['listsES'];
$wsIT = new webserviceApi("IT@karmaresponse.com",$ITtoken);
$listsIT = $json_data['params']['listsIT'];
$wsFR = new webserviceApi("FR@karmaresponse.com",$FRtoken);
$listsFR = $json_data['params']['listsFR'];
$wsAU = new webserviceApi("AU@karmaresponse.com",$AUtoken);
$listsAU = $json_data['params']['listsAU'];
$wsSG = new webserviceApi("SG@karmaresponse.com",$SGtoken);
$listsSG = $json_data['params']['listsSG'];
$wsID = new webserviceApi("ID@karmaresponse.com",$IDtoken);
$listsID = $json_data['params']['listsID'];
$iniDate = date('Y-m-d',strtotime("-1 days"));
$endDate = date("Y-m-d");
$today = date("Ymd");
$emails = [];

print_r('Unsub_DS_' . (string)$today . '.csv');

try {

	$csv = array_map('str_getcsv', file('../MergedFiles/Daily/ALL_Daily_Unsubs_' . (string)$today . '.csv'));
	print_r($csv);
	$sliced_array = array();  //setup the array you want with the sliced values.
	foreach ($csv as $sub_array) {
		$infos = array_slice($sub_array, 0, 1);
		foreach ($infos as $email) {
			array_push ($emails, $email);
		}
}


$halved = array_chunk($emails, 1000);
print_r($halved);

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsES as $DB){
		try {
			foreach ($halved as $half){
				$unsub_ES = array($wsES->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}


try {

	foreach ($listsFR as $DB){
		try {
			foreach ($halved as $half){
				$unsub_FR = array($wsFR->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsIT as $DB){
		try {
			foreach ($halved as $half){
				$unsub_IT = array($wsIT->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsAU as $DB){
		try {
			foreach ($halved as $half){
				$unsub_AU = array($wsAU->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsSG as $DB){
		try {
			foreach ($halved as $half){
				$unsub_SG = array($wsSG->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsID as $DB){
		try {
			foreach ($halved as $half){
				$unsub_ID = array($wsID->dsUsersListUnsubscribeMultiple(array($DB), $half));
				echo ' ... ' . "\xA";
		}

	echo (string)$DB . ' updated '  . "\xA";
	} catch (Exception $e) {
	    echo $msg = $e->getMessage();
			continue;
	}
}

} catch (Exception $e) {
    echo $msg = $e->getMessage();
}
?>
