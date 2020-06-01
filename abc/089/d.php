<?php
list($H, $W, $D) = array_map('intval', explode(' ', trim(fgets(STDIN))));

$table = [];
$map = [];
for ($i = 0; $i < $H; $i++) {
  $table[] = array_map('intval', explode(' ', trim(fgets(STDIN))));
}
for ($i = 0; $i < $H; $i++) {
  for ($j = 0; $j < $W; $j++) {
    $num = $table[$i][$j];
    $map[$num] = [$j, $i];
  }
}

// print_r($map);

$tests = [];
$Q = (int)trim(fgets(STDIN));
for ($i = 0; $i < $Q; $i++) {
  $tests[] = array_map('intval', explode(' ', trim(fgets(STDIN))));
}

$magicTable = [];
// 1 ~ D - 1までをスタート地点としたときに N まで行ったときの魔力消費量の早見表を作成
function calcTotalMagic($start) {
  global $H, $W, $D, $table, $map, $magicTable;
  list($x, $y) = $map[$start];
  $now = $start;
  // print_r($map);
  $magic = 0;
  // print_r($now);
  // echo "now = $now\n";
  while ($now <= $H * $W) {
    $magicTable[$now] = $magic;
    // echo ("x, y = ($x, $y)\n");
    if ($now + $D > $H * $W) {
        break;
    }
    list($newX, $newY) = $map[$now + $D];
    $magic += abs($x - $newX) + abs($y - $newY);
    $x = $newX;
    $y = $newY;
    $now = $table[$y][$x];
  }
}

for ($i = 1; $i <= $D; $i++) {
  calcTotalMagic($i);
}

// print_r($magicTable);

function solve($test) {
  global $magicTable;
  $L = $test[0];
  $R = $test[1];
  return $magicTable[$R] - $magicTable[$L];
}

// print_r($magicTable);
foreach ($tests as $test) {
  $magic = solve($test);
  echo "$magic\n";
}
