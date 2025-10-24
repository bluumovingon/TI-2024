<html>
    <head>
        <title>Menghitung Komisi Salesman</title>
    </head>
    <body>
        <h1>Menghitung Komisi Salesman</h1>
        <?php
        /*
        Script ini akan menghitung komisi salesman berdasarkan nilai penjualan
        yang dicapainnya yaitu Rp. 1.500.000,-
        Ketentuan Komisinya adalah 5% dari nilai penjualan yang tercapai.
        */  
        $nilaiJual = 1500000; // Nilai penjualan yang  didapat salesman
        $komisi = 0.05 * $nilaiJual; // Menghitung komisi 5% dari nilai penjualan
        echo "<p>Nilai Penjualan Salesman : Rp. ". $nilaiJual."<p/>"; // Menampilkan nilai penjualan salesman
        echo "<p>Komisi yang didapat Salesman : Rp. ". $komisi."<p/>"; // Menampilkan hasil perhitungan komisi
        ?>
    </body>
</html>