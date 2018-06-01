<?php
ini_set("error_reporting", E_ALL);
ini_set("display_errors", 1);
ini_set("display_startup_errors", 1);
chdir(dirname(__FILE__));
require_once(dirname(__FILE__) . "/webserviceApi.class.php");

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

try {

	foreach ($listsES as $DB) {
		$unsub_ES = array($wsES->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpES = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_ES as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpES, $fields);
}

    	fclose($fpES);

		echo "\xA" . 'Finished Downloading ' . (string)$DB  . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsFR as $DB) {
		$unsub_FR = array($wsFR->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpFR = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_FR as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpFR, $fields);
}

    	fclose($fpFR);

		echo "\xA" . 'Finished Downloading ' . (string)$DB . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsIT as $DB) {
		$unsub_IT = array($wsIT->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpIT = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_IT as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpIT, $fields);
}

    	fclose($fpIT);

		echo "\xA" . 'Finished Downloading ' . (string)$DB . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsAU as $DB) {
		$unsub_AU = array($wsAU->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpAU = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_AU as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpAU, $fields);
}

    	fclose($fpAU);

		echo "\xA" . 'Finished Downloading ' . (string)$DB . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsSG as $DB) {
		$unsub_SG = array($wsES->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpSG = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_SG as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpSG, $fields);
}

    	fclose($fpSG);

		echo "\xA" . 'Finished Downloading ' . (string)$DB . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}

try {

	foreach ($listsID as $DB) {
		$unsub_ID = array($wsID->dsUsersListGetUnsubscribes($iniDate, $endDate, $DB, $compress = false, $asString = true));
		$fpID = fopen('csv/' . (string)$DB . '/' . 'unsubs_' . (string)$today . '.csv', 'w');

    	foreach ($unsub_ID as $fields) {
    		if (!file_exists('csv/' . (string)$DB . '/')) {
                mkdir('csv/' . (string)$DB . '/', 0777, true);
}
        	fputcsv($fpID, $fields);
}

    	fclose($fpID);

		echo "\xA" . 'Finished Downloading ' . (string)$DB . "\xA" . "\xA";
}


} catch (Exception $e) {
    echo $msg = $e->getMessage();
}
?>
