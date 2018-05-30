<?php

class SoapClientMindbaz extends SoapClient
{
   const MBZ_WS_NAMESPACE = 'http://www.mindbaz.com/webservices/';
   function SoapClientMindbaz($IdSite, $Login, $Password, $wsdl, $options = array())
   {
       parent::__construct($wsdl, $options);
       $this->__setSoapHeaders($this->createHeader($IdSite, $Login, $Password));
   }
   private function createHeader($IdSite, $Login, $Password)
   {
       @$struct->Login = new SoapVar($Login, XSD_STRING, null, null, null, self::MBZ_WS_NAMESPACE);
       $struct->Password = new SoapVar($Password, XSD_STRING, null, null, null, self::MBZ_WS_NAMESPACE);
       $struct->IdSite = new SoapVar($IdSite, XSD_INTEGER, null, null, null, self::MBZ_WS_NAMESPACE);

       $header_values = new SoapVar($struct, SOAP_ENC_OBJECT, null, null,null, self::MBZ_WS_NAMESPACE);
       $header = new SoapHeader(self::MBZ_WS_NAMESPACE, "MindbazAuthHeader", $header_values);
       return $header;
   }
}

class Subscriber
   {
       public function getIdSubscriber()
       {
           if (array_key_exists(0, $this->fld))
               return $this->fld[0];
           else
               return -1;
       }
       public function setIdSubscriber($value)
       {
           $this->fld[0] = $value;
       }

       //tableau key = idField, value = fieldValue
       public $fld;

       //Constructeur à partir d'un objet SubscriberWS
       function __construct($subWS)
       {
           if( $subWS != null)
           {
               $this->setIdSubscriber( $subWS->idSubscriber);
               $this->fld = array();
               if( property_exists($subWS, 'fld') && $subWS->fld != null)
               {
                   if( count(array($subWS->fld)) > 1)
                   {
                       for($i = 0;$i<count(array($subWS->fld));$i++)
                       {
                           $tmpFld = $subWS->fld[$i];
                           $this->fld[$tmpFld->idField] = $tmpFld->value;
                       }
                   }
                   else
                       $this->fld[$subWS->fld->idField] = $subWS->fld->value;
               }
           }
       }

       function printSubscriber()
       {
           echo 'id : ' . $this->getIdSubscriber();
           echo '<br/>[' . count($this->fld ) . ' fields]';
           if( property_exists($this, 'fld') && $this->fld != null)
           {
               foreach ($this->fld as $key => $value)
               {
                   echo '<br/>fld' . $key  .' = ' . $value . ' (' . gettype($value) . ')';
               }
           }
       }
   }

//Webservice authentication
$str = file_get_contents('../params.json');
$json_data = json_decode($str, true);
$Logins = $json_data['params']['All_logins'];
$Passwords = $json_data['params']['All_passwords'];
$Ids = $json_data['params']['All_IDs'];
$today = date("Ymd");
$emails = [];
$IDofDB = $json_data['params']['nb_DB'];

foreach($IDofDB as $ID){
  $soapClient = new SoapClientMindbaz( $Ids[$ID], $Logins[$ID], $Passwords[$ID], "https://webservice.mindbaz.com/subscriberv2.asmx?WSDL", $Options = array());
  print_r(explode("_", $Logins[$ID])[2] . "\xA");
  print_r($Ids[$ID] . "\xA");
  print_r($Passwords[$ID] . "\xA");

  try {

  	$csv = array_map('str_getcsv', file('../MergedFiles/Daily/ALL_Daily_Unsubs_' . (string)$today . '.csv'));
  	$sliced_array = array();  //setup the array you want with the sliced values.
  	foreach ($csv as $sub_array) {
  		$infos = array_slice($sub_array, 0, 1);
  		foreach ($infos as $email) {
  			array_push ($emails, $email);
  		}
  }
  } catch (Exception $e) {
      echo $msg = $e->getMessage();
  }

  foreach ($emails as $unsub){
    try {
      $result = $soapClient -> GetSubscriberByEmail(array('email' => $unsub, 'idFields' => array(0)) );
      $sub = new Subscriber($result->GetSubscriberByEmailResult);
      if( $sub->getIdSubscriber()>0)
      {
      $result = $soapClient -> Unsubscribe(array('idSubscriber' => $sub->getIdSubscriber(),'idSent' => null, 'unsubOnlySubscribers' => True));
      print_r((string)$unsub . "\xA");
      if($result->UnsubscribeResult = false){
        echo var_dump($unsub);
        echo var_dump($result);
      }
      }
    }catch (Exception $e) {
    echo $msg = $e->getMessage();
    continue;
  }
  }
}
?>
