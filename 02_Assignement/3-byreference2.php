<?php
$a = 20;
$b = &$a;

echo "\$a = $a, \$b = $b";
echo "<br />";
// Hasil Proses $a = 20, $b = 20

$a = $a + 5;
echo "\$a = $a, \$b = $b";
echo "<br />";
// Hasil Proses $a = 25, $b = 25

$b = $b + 10;
echo "\$a = $a, \$b = $b";
// Hasil Proses: $a = 35, $b = 30