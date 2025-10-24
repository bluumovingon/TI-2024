<?php
$saldoAwal = 1000000;
$bunga = 0.0025;
$bulan = 11;
$saldoAkhir = $saldoAwal - (($bunga * $bulan) * $saldoAwal) ;
echo "Saldo akhir setelah $bulan bulan adalah Rp. " . $saldoAkhir;
?>