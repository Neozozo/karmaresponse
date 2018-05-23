<?php

/**
 *
 * @author Doctor sender (Freemedia Internet SL)
 * @license This class is for the exclusive use of the client.
 */
class webserviceApi {

    // Private properties.
    private $proxy;

    public function __construct($user,$token) {
        $this->proxy = new SoapClient('http://soapwebservice.doctorsender.com/server.wsdl', array("trace"=>true,'cache_wsdl' => WSDL_CACHE_NONE));
        $header = new SoapHeader("ns1", "app_auth", array("user"=>$user, "pass"=>$token));
        $this->proxy->__setSoapHeaders($header);
    }

/**** CAMPAIGNS ****/

public function dsCampaignNew($name, $subject, $fromName, $fromEmail, $replyTo, $categoryId, $country, $languageId, $html, $text, $listUnsubscribe, $utmCampaign, $utmTerm, $utmContent, $footerDs = True, $mirrorDs = True, $idTemplate = 0){return self::checkResult($this->proxy->webservice('dsCampaignNew', array($name, $subject, $fromName, $fromEmail, $replyTo, $categoryId, $country, $languageId, $html, $text, $listUnsubscribe, $utmCampaign, $utmTerm, $utmContent, $footerDs, $mirrorDs, $idTemplate)));}

public function dsCampaignGet($idCampaign, $fields = array("name", "amount", "subject", "html", "text", "list_unsubscribe", "send_date", "status", "user_list", "country"), $extraInfo = 0){return self::checkResult($this->proxy->webservice('dsCampaignGet', array($idCampaign, $fields, $extraInfo )));}

public function dsCampaignGetAll($sqlWhere, $fields = array("name", "amount", "subject", "html", "text", "list_unsubscribe", "send_date", "status", "user_list", "country"), $extraInfo = 0, $limit = 0){return self::checkResult($this->proxy->webservice('dsCampaignGetAll', array($sqlWhere, $fields, $extraInfo, $limit)));}

public function dsCampaignUpdate($idCampaign, $data, $track = true, $returnHtml = false){return self::checkResult($this->proxy->webservice('dsCampaignUpdate', array($idCampaign, $data, $track, $returnHtml)));}

public function dsCampaignDelete($idCampaign){return self::checkResult($this->proxy->webservice('dsCampaignDelete', array($idCampaign)));}

public function dsCampaignDuplicate($idCampaign, $newName = ""){return self::checkResult($this->proxy->webservice('dsCampaignDuplicate', array($idCampaign,$newName)));}

public function dsCampaignUnschedule($idCampaign){return self::checkResult($this->proxy->webservice('dsCampaignUnschedule', array($idCampaign)));}

public function dsCampaignSendListTest($idCampaign, $listName){return self::checkResult($this->proxy->webservice('dsCampaignSendListTest', array($idCampaign, $listName)));}

public function dsCampaignSendEmailsTest($idCampaign, $contacts){return self::checkResult($this->proxy->webservice('dsCampaignSendEmailsTest', array($idCampaign, $contacts)));}

public function dsCampaignSendList($idCampaign, $listName, $ipGroupName, $speed = 1, $segmentId = 0, $partitionId = 0, $amount = 0, $autoDeleteList = False, $programmedDate = ""){return self::checkResult($this->proxy->webservice('dsCampaignSendList', array($idCampaign, $listName, $ipGroupName, $speed, $segmentId, $partitionId, $amount, $autoDeleteList, $programmedDate)));}

public function dsCampaignSendEmails($idCampaign, $contacts, $ipGroupName){return self::checkResult($this->proxy->webservice('dsCampaignSendEmails', array($idCampaign, $contacts, $ipGroupName)));}

public function dsCampaignGetUserStatistics($idCampaign, $type){return self::checkResult($this->proxy->webservice('dsCampaignGetUserStatistics', array($idCampaign, $type)));}


/**** SEGMENTS ****/

public function dsSegmentsGetByListName($listName){return self::checkResult($this->proxy->webservice('dsSegmentsGetByListName', array($listName)));}

public function dsSegmentsNew($listName, $segmentName){return self::checkResult($this->proxy->webservice('dsSegmentsNew', array($listName, $segmentName)));}

public function dsSegmentsAddCondition($segment_id, $field_name, $comparator, $value, $or=false, $is_date=false, $date_format="Y-m-d H:i:s"){return self::checkResult($this->proxy->webservice('dsSegmentsAddCondition', array($segment_id, $field_name, $comparator, $value, $or=false, $is_date=false, $date_format="Y-m-d H:i:s")));}

public function dsSegmentsDelCondition($segment_id, $field_name){return self::checkResult($this->proxy->webservice('dsSegmentsDelCondition', array($segment_id, $field_name)));}

public function dsSegmentsDel($segment_id){return self::checkResult($this->proxy->webservice('dsSegmentsDelCondition', array($segment_id)));}


/**** FUNCTIONALITY ****/

public function dsCategoryGetAll(){return self::checkResult($this->proxy->webservice('dsCategoryGetAll', array()));}

public function dsCountryGetAll(){return self::checkResult($this->proxy->webservice('dsCountryGetAll', array()));}

public function dsFtpGetAccess(){return self::checkResult($this->proxy->webservice('dsFtpGetAccess', array()));}

public function dsIpGroupGetByName($name){return self::checkResult($this->proxy->webservice('dsIpGroupGetByName', array($name)));}

public function dsIpGroupGetDefault(){return self::checkResult($this->proxy->webservice('dsIpGroupGetDefault', array()));}

public function dsIpGroupGetNames(){return self::checkResult($this->proxy->webservice('dsIpGroupGetNames', array()));}

public function dsLanguageGetAll(){return self::checkResult($this->proxy->webservice('dsLanguageGetAll', array()));}


/**** USERS ****/

public function dsUsersListAdd($listName, array $data, $isTestList){return self::checkResult($this->proxy->webservice('dsUsersListAdd', array($listName,$data, $isTestList)));}

public function dsUsersListNew($listName, $header, $isTestList, $deleteIfExist = false){return self::checkResult($this->proxy->webservice('dsUsersListNew', array($listName, $header, $isTestList, $deleteIfExist)));}

public function dsUsersListUnsubscribeMultiple($listArray, $emails){return self::checkResult($this->proxy->webservice('dsUsersListUnsubscribeMultiple', array($listArray, $emails)));}

public function dsUsersListGetUnsubscribes($iniDate, $endDate, $listName = "", $compress = false, $asString = true){return self::checkResult($this->proxy->webservice('dsUsersListGetUnsubscribes', array($iniDate, $endDate, $listName, $compress, $asString)));}

public function dsUsersListDelete($listName, $isTestList){return self::checkResult($this->proxy->webservice('dsUsersListDelete', array($listName, $isTestList)));}

public function dsUsersListReady($listName, $isTestList){return self::checkResult($this->proxy->webservice('dsUsersListReady', array($listName, $isTestList)));}

public function dsUsersListExists($listName, $isTestList){return self::checkResult($this->proxy->webservice('dsUsersListExists', array($listName, $isTestList)));}

public function dsUsersListUpdate ($listName, $fields, $newData, $isTestList, $data_type="array"){return self::checkResult($this->proxy->webservice('dsUsersListUpdate', array ($listName, $fields, $newData, $isTestList, $data_type)));}

public function dsUsersListImport($listName, $isTestList, $createTable = true){return self::checkResult($this->proxy->webservice('dsUsersListImport', array($listName, $isTestList, $createTable)));}

public function dsUsersListImportReactive($listName){return self::checkResult($this->proxy->webservice('dsUsersListImportReactive', array($listName)));}

public function dsUsersListUnsubscribe($email, $listName = ""){return self::checkResult($this->proxy->webservice('dsUsersListUnsubscribe', array($email, $listName )));}

public function dsUsersListGetUser($email){return self::checkResult($this->proxy->webservice('dsUsersListGetUser', array($email)));}

public function dsUsersListGetAll($isTestList=""){return self::checkResult($this->proxy->webservice('dsUsersListGetAll', array($isTestList)));}

public function dsUsersListNewExclusionFile($file_name, $type){return self::checkResult($this->proxy->webservice('dsUsersListNewExclusionFile', array($file_name, $type)));}

public function dsUsersListAddToExclusionFile($id, $type, $elements){return self::checkResult($this->proxy->webservice('dsUsersListAddToExclusionFile', array($id, $type, $elements)));}

public function dsUsersListGetFields ($listName, $isTestList, $getType=false){return self::checkResult($this->proxy->webservice('dsUsersListGetFields', array($listName, $isTestList, $getType)));}

public function dsUsersListAddField ($listName, $isTestList, $fieldName, $type){return self::checkResult($this->proxy->webservice('dsUsersListAddField', array($listName, $isTestList, $fieldName, $type)));}

public function dsUsersListDownload ($listName, $isTestList, $field="email"){return self::checkResult($this->proxy->webservice('dsUsersListDownload', array($listName, $isTestList, $field)));}


    /**
     * Check the webservice response.
     * @param array $result
     * @throws Exception
     * @return string
     */
    private static function checkResult($result) {
        if (!is_array($result)) {
            Throw new Exception("Error occurred in webservice call");
        }
        if ($result["error"] === true) {
            Throw new Exception($result["msg"]);
        } else {
            return $result["msg"];
        }
    }

    /**
     * Upload import file to Doctor Sender.
     *
     * @param string $filename
     * @param string $listName
     * @throws Exception
     */
    public static function uploadFile($filename, $listName) {
        require_once(dirname(__FILE__) . "/ftpClient/ftp_class.php");
        $ftp = self::dsFtpGetAccess();
        $l = $ftp["user"];
        $p = $ftp["pass"];

        $ftp = new ftp(false);
        $ftp->Verbose = false;
        $ftp->LocalEcho = false;
        if (!$ftp->SetServer($ftp["server"])) {
            $ftp->quit();
            Throw new Exception("Error setting host server.");
        }

        if (!$ftp->connect()) {
            Throw new Exception("Error: FTP conection can't be established.");
        }
        if (!$ftp->login($l, $p)) {
            $ftp->quit();
            Throw new Exception("Error: FTP Access denied.");
        }
        $ftp->chdir("upload");
        if (false === $ftp->put($filename, $listName)){
            $ftp->quit();
            Throw new Exception("Error uploading file.");
        }
        $ftp->quit();
    }
}
