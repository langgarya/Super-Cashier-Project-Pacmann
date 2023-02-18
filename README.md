# Python Project Pacmann - Super Cashier
---
Ini merupakan project sistem kasir sederhana yang bernama **Super Cashier**
## Latar Belakang Masalah
---
Andi adalah seorang pemilik supermarket  besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah itemn yang dibeli, dan harga item yang dibeli dan fitur lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

## Requirements
---
- Membuat program untuk pembeli bisa menginput barang, jumlah barang, dan harga barang yang ingin dibeli
- Membuat program untuk pembeli bisa mengecek barang apa saja yang dibeli
- Membuat program untuk pembeli bisa merubah pesanan barang
- Membuat program untuk pembeli bisa mengetahui total pembelian beserta diskon yang didapat

## Flowchart dan Penjelasan Code
---
![Flowchart_Super_Cashier_Project_Pacmann](https://user-images.githubusercontent.com/67636190/219857262-b113f38f-eb0d-4a26-8d77-ac5bf814f529.png)

Flowchart untuk program ini cukup sederhana, yaitu pembeli memulai program, lalu memasukkan nama, jumlah, dan harga barang. Selanjutnya menambahkan barang jika mau, kalau tidak akan lanjut ke mengecek pesanan dan akan dicek apakah ada kesalahan seperti kesalahan input atau ada yang ingin diubah pesanannya. Selanjutnya ketika semua sudah benar maka akan lanjut ke bagian menghitung total belanja beserta diskon yang bisa didapatkan. Akhirnya akan muncul total yang harus dibayarkan beserta diskonnya.

Fungsi atribut:
- `add_item` berfungsi untuk menambahkan nama, jumlah, dan harga barang yang ingin dibeli
- `update_item_name` berfungsi untuk mengubah atau memperbaiki nama barang yang dibeli
- `update_item_qty` berfungsi untuk mengubah atau memperbaiki jumlah barang yang dibeli
- `update_item_price` berfungsi untuk mengubah atau memperbaiki harga barang yang dibeli
- `delete_item` berfungsi untuk menghapus barang yang tidak diinginkan
- `reset_transaction` berfungsi untuk menghapus semua barang yang dipesan
- `check_order` berfungsi untuk memeriksa benar atau salahnya pesanan yang sudah diinput dan menampilkan seluruh barang yang dipesan
- `total_price` berfungsi untuk mengetahui total dari belanja yang harus dibayar beserta diskon yang didapatkan

## Cara Menjalankan Program
---
1. Download semua file/module Python ke dalam satu direktori lokal
2. Buka terminal dan sesuaikan lokasi direktori lokal
3. Buka file main.py, silahkan untuk memasukkan fungsi di file ini
4. Jalankan module python main.py di terminal

## Hasil Test Case
---
1. Menginput barang yang ingin dibeli
![SS_Test_Case_1](https://user-images.githubusercontent.com/67636190/219864489-a3400666-df02-462e-8bd9-77366a09efac.png)
2. Menambah barang yang ingin dibeli
![SS_Test_Case_2](https://user-images.githubusercontent.com/67636190/219864713-77d693d2-b048-4416-9b84-eae9ad434018.png)
3. Mengupdate nama barang yang ingin dibeli
![SS_Test_Case_3](https://user-images.githubusercontent.com/67636190/219864836-d206a623-d509-487e-ba00-b4e9f9cf4443.png)
4. Mengupdate jumlah barang yang ingin dibeli
![SS_Test_Case_4](https://user-images.githubusercontent.com/67636190/219864912-ee2f3813-1c4b-4526-a634-84c5a41531c9.png)
5. Mengupdate harga barang yang ingin dibeli
![SS_Test_Case_5](https://user-images.githubusercontent.com/67636190/219865031-697d0088-62b0-4d84-a49a-570ead28c222.png)
6. Menghapus barang yang tidak ingin dibeli
![SS_Test_Case_6](https://user-images.githubusercontent.com/67636190/219865107-5cc65f4c-680d-477c-bd00-367dceb4b480.png)
7. Menghapus semua barang
![SS_Test_Case_7](https://user-images.githubusercontent.com/67636190/219865162-e22bb626-2900-42f9-b743-e4c53f8c9f6c.png)
8. Menghitung total belanjaan dan diskon
![SS_Test_Case_8](https://user-images.githubusercontent.com/67636190/219865392-8aa497aa-e73f-429e-b228-ff0642822bf4.png)

## Saran Perbaikan
- Diperlukan sebuah library agar pembeli tidak menginput banyak hal
- Memperbaiki interface agar lebih menarik dan mudah digunakan



