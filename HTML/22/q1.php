<?php

class Queue
{
private $queue;
public function __construct()
{
$this->queue = array();
}
public function enqueue($element)
{
array_push($this->queue, $element);
echo "Element '$element' inserted into the queue.\n";
}
public function dequeue()
{
if (empty($this->queue)) {
echo "Queue is empty. Cannot dequeue.\n";
} else {
$element = array_shift($this->queue);
echo "Element '$element' deleted from the queue.\n";
}
}
public function displayQueue()
{
if (empty($this->queue)) {
echo "Queue is empty.\n";
} else {
echo "Contents of the queue: " . implode(', ', $this->queue) . "\n";
}
}
}

$queue = new Queue();

while (true) {
echo "Menu:\n";
echo "a. Insert an element in the queue.\n";
echo "b. Delete an element from the queue.\n";
echo "c. Display the contents of the queue.\n";
echo "d. Exit.\n";

$choice = readline("Enter your choice (a/b/c/d): ");
switch ($choice) {

case 'a':
$element = readline("Enter the element to insert: ");
$queue->enqueue($element);
break;

case 'b':
$queue->dequeue();
break;

case 'c':
$queue->displayQueue();
break;

case 'd':
exit("Exiting the program.\n");

default:
echo "Invalid choice. Please enter a valid option (a/b/c/d).\n";
break;
}
}
?>

