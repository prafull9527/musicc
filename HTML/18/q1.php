<?php
$associativeArray = array('name' => 'John','age' => 25,'city' => 'New York','country' => 'USA');

function reverseKeyValue($array) {
$reversedArray = array();
foreach ($array as $key => $value) {
$reversedArray[$value] = $key;
}
return $reversedArray;
}


function traverseRandomOrder($array) {
$keys = array_keys($array);
shuffle($keys);
$randomArray = array();
foreach ($keys as $key) {
$randomArray[$key] = $array[$key];
}
return $randomArray;
}


function convertToVariables($array) {
extract($array);

echo "Variables created: \$name = $name, \$age = $age, \$city = $city, \$country = $country<br>";
}

function displayWithKey($array) {
foreach ($array as $key => $value) {
echo "Key: $key, Value: $value<br>";
}
}


echo "Menu:\n";
echo "a. Reverse the order of each element’s key-value pair.\n";
echo "b. Traverse the element in an array in random order.\n";
echo "c. Convert the array elements into individual variables.\n";
echo "d. Display the elements of an array along with key.\n";

$choice = readline("Enter your choice (a/b/c/d): ");

switch ($choice) 
{
case 'a':
$reversedArray = reverseKeyValue($associativeArray);
displayWithKey($reversedArray);
break;

case 'b':
$randomArray = traverseRandomOrder($associativeArray);
displayWithKey($randomArray);
break;

case 'c':
convertToVariables($associativeArray);
break;

case 'd':
displayWithKey($associativeArray);
break;

default:
echo "Invalid choice. Please enter a valid option (a/b/c/d).\n";
break;
}

?>

