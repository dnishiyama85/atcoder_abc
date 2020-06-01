<?php
$input = trim(fgets(STDIN));
$d = new DateTime($input);
$boundary = new DateTime('2019/04/30');

if ($d <= $boundary) {
    echo "Heisei\n";
} else {
    echo "TBD\n";
}

