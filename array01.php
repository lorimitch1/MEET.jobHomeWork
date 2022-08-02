<?php

/*






*/

$student = array("1","2","3","4","5");
echo $student[0];
echo "<br>";
echo $student[3] . "<br>";
echo "<hr>";

for($i=0 ; $i<5 ; $i++){
	echo $student[$i] . "<br>";
}


echo "<hr>";

foreach ($student as $value) {
	echo $value . "<br>";
}


?>