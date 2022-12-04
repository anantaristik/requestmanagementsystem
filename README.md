![plot](requestmanagementsystem/static/base/img/rms-logo-white-bg.png)
<h1 align="center">Request Management System</h1>
<h3 align="center">Aki Runcoko</h3>

## About The Project
Sebagaimana yang kita ketahui, organisasi kemahasiswaan memiliki suatu birokrasi dalam melakukan korespondensi, pengelolaan keuangan, publikasi, dan administrasi internal lainnya untuk mendukung berjalannya organisasi. Sejauh ini, kami merasa organisasi di Fasilkom masih belum memanfaatkan digitalisasi dalam pelaksanaan berbagai birokrasi yang ada. Sebagai contoh, proses permintaan surat menyurat yang masih melalui email atau Google Form sehingga pemohon tidak bisa melakukan tracking terhadap surat yang diminta. Hal yang sama juga terjadi pada birokrasi yang lainnya seperti birokrasi publikasi dan birokrasi permohonan dana.
<br> <br>
Berangkat dari permasalahan tersebut, kami merasa diperlukannya suatu sistem informasi yang dapat mengoptimalisasi berbagai birokrasi yang ada melalui sistem yang terintegrasi. Harapannya, dengan adanya sistem informasi terintegrasi bisa menciptakan sistem kerja yang efisien. Oleh karena itu, kami menginisiasi sebuah sistem informasi terintegrasi yang terdiri atas beberapa sistem informasi dari berbagai birokrasi yang ada dalam satu aplikasi. Sistem ini mencakup sistem informasi publikasi, surat menyurat, keuangan, permintaan survei, dan lain lain. Sistem ini lebih efektif dari sistem sebelumnya karena hanya membutuhkan satu platform  saja untuk dapat menjalankan berbagai sistem lainnya.

## Developers:
1. 2006482640 - Rizky Ananta (Dana)
2. 2006536486 - Ferdinand Amos Papilaya (Surat)
3. 2006596251 - Mika Suryofakhri Rahwono (Feedback)
4. 2006473863 - Sulthan Afif Althaf (User)
5. 2006486115 - Takayuki Muhamad Rabbani (Publikasi)


## System Requirements
### Fitur:
### Permohonan Surat menyurat ✉️
Permohonan surat merupakan fitur yang disediakan oleh RSM untuk mempermudah pemohon dalam melakukan permohonan surat menyurat, serta mempermudah bagi para pengurus surat dalam melakukan tracking terhadap permintaan-permintaan yang ada.

### Permohonan Dana 💵
Permohonan dana merupakan fitur yang disediakan oleh RSM untuk mempermudah pemohon dalam melakukan permohonan dana, serta mempermudah bagi para pengurus dana dalam melakukan tracking terhadap permintaan-permintaan yang ada. Fitur ini tidak mendukung penarikan dana via sistem. Fitur ini hanya untuk pelaporan dan permohonan dana, sementara penarikan dana dilakukan secara manual diluar sistem.

### Permohonan Publikasi 📢
Permohonan publikasi merupakan fitur yang disediakan oleh RSM untuk mempermudah pemohon dalam melakukan permohonan publikasi di kanal media organisasi yang ada, serta mempermudah bagi para pengurus publikasi dalam melakukan tracking terhadap permintaan-permintaan yang ada.

### Dashboard Pemohon 👥
Pada dashboard pemohon berisi daftar permintaan yang dilakukan oleh pemohon, sehingga pemohon dapat melakukan tracking terhadap progress dari permintaan yang sudah diajukan.

### Dashboard Pengurus 👷🏻‍♀️
Pada dashboard pengurus berisi daftar permintaan dari seluruh permintaan yang masuk. Sehingga pengurus dari masing-masing permintaan bisa melakukan tracking terhadap seluruh permintaan yang ada.

### Autentikasi 👤
Untuk melakukan permohonan dan juga pengelolaan alur permohonan, user harus login dan ter-autentikasi oleh sistem. Jika tidak terautentikasi, maka user tidak bisa menggunakan keseluruhan fitur yang ada pada sistem (semua fitur hanya bisa digunakan oleh user yang terautentikasi).

## Role 🎭
### Super Admin
Super admin merupakan user super dimana user ini memiliki kuasa atas seluruh data dan alur yang ada pada sistem.

### User Pengurus
User pengurus merupakan user dimana user ini memiliki akses terhadap setiap tahapan progress permintaan dan seluruh permintaan yang masuk. User pengurus dapat mengakses halaman berikut :
### Dashboard pengurus

### Detail page dan alur permohonan :
1. Surat menyurat
2. Dana
3. Publikasi

### User Pemohon
User pemohon merupakan user dimana user ini bisa melakukan permohonan terhadap permintaan yang dibutuhkan oleh pemohon, baik surat menyurat, dana, maupun publikasi. User pemohon dapat mengakses halaman berikut :
Dashboard pemohon

### Form permohonan :
1. Surat menyurat
2. Dana
3. Publikasi
