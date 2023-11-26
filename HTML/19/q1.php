<?php
function deleteSubstring($sentence, $position, $numChars) {
$deletedPart = substr($sentence, $position, $numChars);
$result = str_replace($deletedPart, '', $sentence);
return $result;
}
function insertSubstring($bigString, $smallString, $position) {
$result = substr_replace($bigString, $smallString, $position, 0);
return $result;
}

function replaceSubstring($bigString, $smallString, $position) {
$result = substr_replace($bigString, $smallString, $position,strlen($smallString));
return $result;
}


$sentence = readline("Enter a sentence: ");
$word = readline("Enter a word: ");


echo "Menu:\n";
echo "a. Delete a small part from the first string.\n";
echo "b. Insert the given small string in the given big string at a specified position.\n";
echo "c. Replace some characters/words from the given big string with the given small string at a specified position.\n";

$choice = readline("Enter your choice (a/b/c): ");

switch ($choice) 
{
case 'a':
$position = readline("Enter the position to start deletion: ");
$numChars = readline("Enter the number of characters to delete: ");
$result = deleteSubstring($sentence, $position, $numChars);
echo "Result after deletion: $result\n";
break;

case 'b':
$position = readline("Enter the position to insert the word: ");
$result = insertSubstring($sentence, $word, $position);
echo "Result after insertion: $result\n";
break;

case 'c':
$position = readline("Enter the position to replace characters/words: ");
$result = replaceSubstring($sentence, $word, $position);
echo "Result after replacement: $result\n";
break;

default:
echo "Invalid choice. Please enter a valid option (a/b/c).\n";
break;
}

?>

