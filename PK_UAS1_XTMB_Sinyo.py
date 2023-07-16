#method 1
#input total harga
print('Program Kalkulator Diskon Belanja')
harga_belanja = int(input('Masukkan Total Belanja : Rp '))

#untuk menentukan nilai diskon
if (harga_belanja > 5000000):
    list_discount = ['7%', 0.07, 0.93]
elif (harga_belanja <= 5000000 and harga_belanja >= 2000000):
    list_discount = ['5%', 0.05, 0.95]
elif (harga_belanja <= 2000000 and harga_belanja >= 1000000):
    list_discount = ['3%', 0.03, 0.97]
elif (harga_belanja < 1000000):
    list_discount = ['1%', 0.01, 0.99]

#menampilkan hasil
print('Diskon                 : Rp', int(harga_belanja * list_discount[1]), f'(selamat, dapat diskon {list_discount[0]})')
print('Total Bayar            : Rp', int(harga_belanja * list_discount[2]))
