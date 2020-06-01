<?php
$N = (int)fgets(STDIN);
$dp = [];
$dp[0] = 1;
$dp[1] = 4;
$dp[2] = 16;
$dp[3] = 61;

for($i = 4; $i <= $N; $i++) {
    $dp[$i] = ($dp[$i - 1] * 4 - $dp[$i - 3] * 3 + $dp[$i - 4]) % 1000000007;
}

echo $dp[$N] . "\n";

