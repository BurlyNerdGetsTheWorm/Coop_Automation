<html>
<head>
<link href="site.css" rel="stylesheet">
<div align="center">
<h1>Raspberry Pi Web Controls for 8 Outlet Relay</h1>
</div>
</head>
<?php
if (isset($_POST['GPIO02ON']))
{
exec("sudo python Pin02ON.py");
}
elseif (isset($_POST['GPIO02OFF']))
{
exec("sudo python Pin02OFF.py");
}
elseif (isset($_POST['GPIO03ON']))
{
exec("sudo python Pin03ON.py");
}
elseif (isset($_POST['GPIO03OFF']))
{
exec("sudo python Pin03OFF.py");
}
elseif (isset($_POST['GPIO04ON']))
{
exec("sudo python Pin04ON.py");
}
elseif (isset($_POST['GPIO04OFF']))
{
exec("sudo python Pin04OFF.py");
}
elseif (isset($_POST['GPIO17ON']))
{
exec("sudo python Pin17ON.py");
}
elseif (isset($_POST['GPIO17OFF']))
{
exec("sudo python Pin17OFF.py");
}
elseif (isset($_POST['GPIO27ON']))
{
exec("sudo python Pin27ON.py");
}
elseif (isset($_POST['GPIO27OFF']))
{
exec("sudo python Pin27OFF.py");
}
elseif (isset($_POST['GPIO22ON']))
{
exec("sudo python Pin22ON.py");
}
elseif (isset($_POST['GPIO22OFF']))
{
exec("sudo python Pin22OFF.py");
}
elseif (isset($_POST['GPIO10ON']))
{
exec("sudo python Pin10ON.py");
}
elseif (isset($_POST['GPIO10OFF']))
{
exec("sudo python Pin10OFF.py");
}
elseif (isset($_POST['GPIO09ON']))
{
exec("sudo python Pin09ON.py");
}
elseif (isset($_POST['GPIO09OFF']))
{
exec("sudo python Pin09OFF.py");
}
elseif (isset($_POST['DOOROPEN']))
{
exec("sudo python DoorOpen.py");
}
elseif (isset($_POST['DOORCLOSE']))
{
exec("sudo python DoorClose.py");
}
elseif (isset($_POST['AUTOMATIONENABLE']))
{
exec("sudo python AutomationOn.py");
}
elseif (isset($_POST['AUTOMATIONDISABLE']))
{
exec("sudo python AutomationOff.py");
}
?>
<br>
<body>

<div align="center">
<div id="SunTimesGroup">
<h3>Sunrise/Sunset Times</h3>
<p>
<?php
$url = "https://apps.tsa.dhs.gov/MyTSAWebService/GetEventInfo.ashx?eventtype=sunrise_sunset&airportcode=FNT&output=json";
$data = json_decode(file_get_contents($url),true);
echo "Sunrise - ",$data[Sunrise],"<br />";
echo "Sunset - ",$data[Sunset];
?>
</p>
</div>

<form method="post">

<div id="DoorGroup">
<h3>Door Status:</h3>
<p>
<button id="Door-Open" class="btn" name="DOOROPEN">Door Open</button>
<button id="Door-Close" class="btn" name="DOORCLOSE">Door Close</button><br>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[doorstatus] == "Open")
{
echo "<strong>" . $data[doorstatus] . "</strong>";
}
else {
echo $data[doorstatus];
}
?>
</p>
</div>

<div id="AutomationGroup">
  <h3>Automation Status:</h3>
<p>
  <button id="Automation-Enable" class="btn" name="AUTOMATIONENABLE">Enable</button>
  <button id="Automation-Disable" class="btn" name="AUTOMATIONDISABLE">Disable</button><br>
  <p>Status: <?php
  $data = json_decode(file_get_contents("values.json"),true);
  #echo $data[automationenabled];
  if ($data[automationenabled] == true) {
    echo "<strong>Enabled</strong><br />(The door will open/close automatically in addition to manual operation.)";
  } else {
    echo "<strong>Disabled</strong><br />(The door is set to manual operation only.)";
  }
  ?>
</p>
</div>

<div class="clear"></div>

<div id="Outlet2Group" class="toprow firstrow">
<h3>Outlet 2:</h3>
<button id="2-Outlet-On" class="btn" name="GPIO03ON">Light On</button>
<button id="2-Outlet-Off" class="btn" name="GPIO03OFF">Light Off</button><br>
<p>Connect led to Pin No :5/ GPIO 03</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug2] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug2];
}
?>
</div>

<div id="Outlet4Group" class="toprow secondrow">
<h3>Outlet 4:</h3>
<button id="4-Outlet-On" class="btn" name="GPIO17ON">Light On</button>
<button id="4-Outlet-Off" class="btn" name="GPIO17OFF">Light Off</button><br>
<p>Connect led to Pin No:11/ GPIO 17</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug4] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug4];
}
?>
</div>

<div id="Outlet8Group" class="toprow fourthrow">
<h3>Outlet 8:</h3>
<button id="8-Outlet-On" class="btn" name="GPIO09ON">Light On</button>
<button id="8-Outlet-Off" class="btn" name="GPIO09OFF">Light Off</button><br>
<p>Connect led to Pin No:9/ GPIO 09</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug8] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug8];
}
?>
</div>

<div id="Outlet6Group" class="toprow thirdrow">
<h3>Outlet 6:</h3>
<button id="6-Outlet-On" class="btn" name="GPIO22ON">Light On</button>
<button id="6-Outlet-Off" class="btn" name="GPIO22OFF">Light Off</button><br>
<p>Connect led to Pin No:15/ GPIO 22</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug6] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug6];
}
?>
</div>

<div id="Outlet1Group" class="bottomrow firstrow">
<h3>Outlet 1:</h3>
<button id="1-Outlet-On" class="btn" name="GPIO02ON">Light On</button>
<button id="1-Outlet-Off" class="btn" name="GPIO02OFF">Light Off</button><br>
<p>Connect led to Pin No: 3/ GPIO 02</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug1] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug1];
}
?>
</div>

<div id="Outlet3Group" class="bottomrow secondrow">
<h3>Outlet 3:</h3>
<button id="3-Outlet-On" class="btn" name="GPIO04ON">Light On</button>
<button id="3-Outlet-Off" class="btn" name="GPIO04OFF">Light Off</button><br>
<p>Connect led to Pin No:7/ GPIO 04</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug3] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug3];
}
?>
</div>

<div id="Outlet7Group" class="bottomrow thirdrow">
<h3>Outlet 7:</h3>
<button id="7-Outlet-On" class="btn" name="GPIO10ON">Light On</button>
<button id="7-Outlet-Off" class="btn" name="GPIO10OFF">Light Off</button><br>
<p>Connect led to Pin No:10/ GPIO 10</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug7] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug7];
}
?>
</div>

<div id="Outlet5Group" class="bottomrow fourthrow">
<h3>Outlet 5:</h3>
<button id="5-Outlet-On" class="btn" name="GPIO27ON">Light On</button>
<button id="5-Outlet-Off" class="btn" name="GPIO27OFF">Light Off</button><br>
<p>Connect led to Pin No:13/ GPIO 27</p>
<p>Status: <?php
$data = json_decode(file_get_contents("values.json"),true);
if ($data[plug5] == "On") {
  echo "<strong>On</strong>";
} else {
  echo $data[plug5];
}
?>
</div>

</form>
<div>
</body>
</html>
