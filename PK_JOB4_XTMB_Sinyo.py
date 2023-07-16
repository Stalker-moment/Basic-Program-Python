#Input jumlah hari
hari = input('Masukkan jumlah hari: ')

tahun = int(hari) // 365
sisa_tahun = int(hari) % 365 # % merupakan operator untuk menampilkan sisa dari pembagian
bulan = int(sisa_tahun) // 30 #pada int operasi pembagian tidak dapat menggunakan / jadi menggunakan //
sisa_bulan = int(sisa_tahun) % 30
minggu = int(sisa_bulan) // 7
sisa_hari = int(sisa_bulan) % 7

print("{} hari adalah, {} Tahun, {} Bulan, {} Minggu, {} Hari" \
    .format(hari, tahun, bulan, minggu, sisa_hari))

#print dengan {} yaitu print dengan teknik format
#yang nantinya {} akan digantikan variable yang di masukkan pada .format