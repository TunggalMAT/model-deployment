# model-deployment
***
# Instruksi
>1. Download file `request.py`
>2. Pindahkan File `request.py` ke direktori local disk D
>3. Buka Anaconda Prompt
>4. Ketik `d:`
>5. Ketik `python request.py`
>6. Masukkan Jumlah User yang akan di prediksi
>7. Inputkan Fitur dari setiap user sesuai range angka yang ada pada keterangan di setiap fitur
>8. Klik Enter setiap selesai menginputkan nilai sebuah fitur
>9. Inputkan nilai pada semua fitur
>10. Tunggu selama beberapa detik, dan hasilpun akan muncul
***
### Program ini dapat digunakan untuk memprediksi 1 user maupun banyak user ***sekaligus***. Pada case ini maksimal user dibatasi dampai 10 user saja.
# Overview
***
Repository ini terdiri dari 2 Source Code dan 1 model. `request.py` adalah **user site**. pada folder`server_site` terdapat 2 file yakni `flask_app.py` dan `clf.pkl` yang merupakan **server site** yang ada pada *http://tunggalmat.pythonanywhere.com/api*.
<br> Secara umum, program ini adalah program untuk memprediksi user/customer akan *telat* atau *tidak telat* dalam membayar kredit. Inputnya berupa 6 fitur yakni EDUCATION, SEX, MARRIAGE, PAY_1, PAY_2, dan PAY_3. Model yang digunakan adalah Random Forest Classifier (`clf.pkl`). Pada user site dibuat simple agar mudah dicoba dan dimengerti oleh user.
<br>Selamat Menggunakan, **Semoga Bermanfaat**
# THANKS
