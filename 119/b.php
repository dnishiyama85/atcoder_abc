<?php
$N = (int)fgets(STDIN);
$total = 0;
for ($i = 0; $i < $N; $i++) {
    list($x, $u) = explode(' ', trim(fgets(STDIN)));
    if ($u == 'BTC') {
        $total += 380000.0 * $x;
    } else {
        $total += $x;
    }
}

echo $total . "\n";

