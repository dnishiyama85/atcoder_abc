<?php
list($N, $Q) = array_map('intval', explode(' ', trim(fgets(STDIN))));
$S = trim(fgets(STDIN));
$queries = [];
for($i = 0; $i < $Q; $i++) {
    list($l, $r) = array_map('intval', explode(' ', trim(fgets(STDIN))));
    $queries[] = [$l, $r];
}

$qsum = [];
$count = 0;
$i = 0;
while ($i < $N) {
    $qsum[$i] = $count;
    if ($S[$i] == 'A' && $i < $N - 1) {
        $i++;
        if ($S[$i] == 'C') {
            $count++;
            $qsum[$i] = $count;
        }
    } else {
        $i++;
    }
}

//print_r($qsum);
foreach ($queries as $q) {
    list($l, $r) = $q;
    echo ($qsum[$r - 1] - $qsum[$l - 1]). "\n";
}

