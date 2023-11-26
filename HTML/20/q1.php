<?php
$associativeArray = array('a' => 5,'b' => 2,'c' => 8,'d' => 3,'e' => 7,'f' => 6);


function splitIntoChunks($array, $chunkSize) {
$result = array_chunk($array, $chunkSize, true);
return $result;
}


function sortByValues($array) {
asort($array);
return $array;
}


function filterEvenElements($array) {
$result = array_filter($array, function ($value){return $value % 2 == 0;});
return $result;
}


echo "Menu:\n";
echo "a. Split an array into chunks.\n";
echo "b. Sort the array by values without changing keys.\n";
echo "c. Filter the even elements from an array.\n";

$choice = readline("Enter your choice (a/b/c): ");

switch ($choice)
 {
case 'a':
$chunkSize = readline("Enter the chunk size: ");
$result = splitIntoChunks($associativeArray, $chunkSize);
print_r($result);
break;

case 'b':
$result = sortByValues($associativeArray);
print_r($result);
break;

case 'c':
$result = filterEvenElements($associativeArray);
print_r($result);
break;

default:
echo "Invalid choice. Please enter a valid option (a/b/c).\n";
break;
}

?>

