<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="utf-8">
    <title>Tark Maja</title>
    <link rel="icon" type="image/png" href="M.png">
    <link rel="stylesheet" type="text/css" href="design/style.css">
</head>
<body>     
    <nav>
        <ul>
            <li><a href="koduleht.php">Avaleht</a></li>
            <li><a href="paketiinfo.html">Paketi informatsioon</a></li>
            <li><a href="seadmed.php">Seadmed</a></li>
            <li><a href="tingimused.html">Seadme tingimused</a></li>
        </ul>
    </nav>
    
    <div class="banner">
        <img class="banner-image" src="4.png">
     </div><hr>

    <h1>Tingimuste sisestamine</h1>
        <br>  
        <div class="container">   
            <form method="POST">
                <legend>Mitu minutit peab elektriseade ööpäevas olema sisse lülitatud?</legend>
                    <input type="number" name="am_worktime_min"><br>
                <br>
                <legend>Mitu minutit peab elektriseade ööpäevas olema välja lülitatud?</legend>
                    <input type="number" name="pm_worktime_min"><br>
                <br>
                <legend>Mitu minutit peab elektriseade ööpäevas korraga töötama?</legend>
                    <input type="number" name="alltime_worktime"><br>
                <br>
                <legend>Mitu minutit peab elektriseade ööpäevas korraga kinni olema?</legend>
                    <input type="number" name="notworktime"><br>
                <br>
                <legend>Maksimumvõimsus</legend>
                    <input type="number" name="maxpower"><br>
                <br>
                <legend>Miinimumvõimsus</legend>
                    <input type="number" name="minpower"><br> 
				<br>
                <legend>Seade sisse lülitatud:</legend>
                <input type="time" name="tooaeg1"> 
                <input type="time" name="tooaeg2"><br>
                <input type="time" name="tooaeg3">
                <input type="time" name="tooaeg4"><br>
                <input type="time" name="tooaeg5">
                <input type="time" name="tooaeg6"><br>
                <input type="time" name="tooaeg7">
                <input type="time" name="tooaeg8"><br>
                <br>
                <legend>Seade välja lülitatud:</legend>
                <input type="time" name="mittetooaeg1">
                <input type="time" name="mittetooaeg2"><br>
                <input type="time" name="mittetooaeg3">
                <input type="time" name="mittetooaeg4"><br>
                <input type="time" name="mittetooaeg5">
                <input type="time" name="mittetooaeg6"><br>
                <input type="time" name="mittetooaeg7">
                <input type="time" name="mittetooaeg8"><br>
				<input type="submit" name="submit" value="Salvesta">
            </form>
        </div>
</body>
</html>

<?php

if(isset($_POST["am_worktime_min"]) && isset($_POST["pm_worktime_min"]) && isset($_POST["alltime_worktime"]) && isset($_POST["notworktime"]) && isset($_POST["maxpower"]) && isset($_POST["minpower"]) && isset($_POST["tooaeg1"]) && isset($_POST["tooaeg2"]) && isset($_POST["tooaeg3"]) && isset($_POST["tooaeg4"]) && isset($_POST["tooaeg5"]) && isset($_POST["tooaeg6"]) && isset($_POST["tooaeg7"]) && isset($_POST["tooaeg8"]) && isset($_POST["mittetooaeg1"]) && isset($_POST["mittetooaeg2"]) && isset($_POST["mittetooaeg3"]) && isset($_POST["mittetooaeg4"]) && isset($_POST["mittetooaeg5"]) && isset($_POST["mittetooaeg6"]) && isset($_POST["mittetooaeg6"]) && isset($_POST["mittetooaeg7"]) && isset($_POST["mittetooaeg8"])) {

    $data = $_POST['am_worktime_min'] . "\n" . $_POST['pm_worktime_min'] . "\n" . $_POST['alltime_worktime'] . "\n" . $_POST['notworktime'] . "\n" . $_POST['maxpower'] . "\n" . $_POST['minpower'] . "\n" . $_POST['tooaeg1'] . "\n" . $_POST['tooaeg2'] . "\n" . $_POST['tooaeg3'] . "\n" . $_POST['tooaeg4'] . "\n" . $_POST['tooaeg5'] . "\n" . $_POST['tooaeg6'] . "\n" . $_POST['tooaeg7'] . "\n" . $_POST['tooaeg8'] . "\n" . $_POST['mittetooaeg1'] . "\n" . $_POST['mittetooaeg2'] . "\n" . $_POST['mittetooaeg3'] . "\n" . $_POST['mittetooaeg4'] . "\n" . $_POST['mittetooaeg5'] . "\n" . $_POST['mittetooaeg6'] . "\n" . $_POST['mittetooaeg7'] . "\n" . $_POST['mittetooaeg8'] . "\n";
	
	 $getData = file_put_contents('userconditions.txt', $data, LOCK_EX);
    if($getData === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$getData bytes written to file";
    }
	}
	else {
	   die(' ');
	}
?>