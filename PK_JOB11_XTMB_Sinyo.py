# membuat program kasir resto sederhana
#fungsi untuk tanya hitung kembali                      __________________________________________________________________________________________________________________________
def counter_kasir():                               #   |--> cara kerja program ini :                                                                                              |
    counter = input('hitung lagi: (y/n)')          #   |  + program ini menggunakan sistem login sederhana(menggunakan logika and)                                                |
    if counter == 'y':                             #   |  + program ini menggunakan fungsi (def), fungsi ini memudahkan saat callback (memanggil fungsi untuk di eksekusi)        |
        kasir()                                    #   |--> runtut proses :                                                                                                       |
    elif counter == 'n':                           #   |  + program dimulai -> callback halaman login -> memasukkan username & password -> login berhasil : masuk halaman utama   |
        print('ingin hitung lagi..?')              #   |                                                 login gagal : memasukkan username & passsword ulang                      |
        tanya()                                    #   |  + halaman utama -> cetak menu -> masukkan pilihan : callback fungsi pilihan                                             |
    else:                                          #   |                                   tidak memasukkan pilihan : callback exit                                               |
        print('input program salah harap ulangi')  #   |__________________________________________________________________________________________________________________________|
 
def kasir(): #fungsi perhitungan kasir
    #masukkan input dari user
    nama_barang = input('masukan pesanan anda: ') #input barang
    harga = int(input('masukan harga barang: ')) #input harga
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: ')) #input jumlah barang
    
    #menghitung jumlah harga
    total = harga * jumlah_beli
    
    #cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
    
    #input pembayaran dari user
    bayar = int (input('masukkan pembayaran: '))
    
    #mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
    
    if bayar > total: #apabila bayar lebih dari total = kembalian
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
    elif bayar == total: #apabila bayar sama dengan total = uang pas
        print('uang anda pas, terimakasih telah berbelanja')
    else: #apabila bayar kurang dari total = uang kurang
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir #callback ke 

def main_menu():
    #membuat daftar menu pada kasir
    print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukkan input aplikasi', '=' * 20)
    print('1. Program Kasir')
    print('2. Program Kalkulator')
    print('3. Exit Program')
    
    #input pilihan
    pilihan = input('pilih menu: ')
    
    #pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('Program Exit')
        exit()

def get_login(): #fungsi halaman login
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukkan username kasir anda: ') #input username
    password = input('masukkan password: ') #input password
    
    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu() #apabila login berhasil, callback main menu
    else:
        print('login gagal coba lagi...')
        get_login() #apabila login gagal, callback login (mengisi ulang)
        
def tanya(): #fungsi tanya kemmbali
    tanya = input('kembali ke menu..? (y/n)')  #input tanya
    if tanya == 'y':
        main_menu()
    elif tanya == 'n':
        exit()
    else:
        print('input salah')
        print('masukkan input dengan benar')
        
    #membuat kalkulator
def kalkulator(): #fungsi kalkulator
    print('=' * 10)
    print('Program Kalkulator')
    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')
    
    a = int(input('masukkan bilangan pertama: ')) #input bilangan pertama
    b = int(input('masukkan bilangan ke-dua: ')) #input bilangan kedua
    operator = input('masukkan operator: ') #input jenis operator
    
    if operator == '1': #pertambahan
        print('hasil dari {} + {} = {}'.format (a, b, a + b)) 
    elif operator == '2': #pengurangan
        print('hasil dari {} - {} = {}'.format (a, b, a - b))
    elif operator == '3': #pembagian
        print('hasil dari {} / {} = {}'.format (a, b, a / b))
    elif operator == '4': #perkalian
        print('hasil dari {} * {} = {}'.format (a, b, a * b))
    elif operator == '5': #modulus
        print('hasil dari {} % {} = {}'.format (a, b, a % b))
    else:
        print('masukkan input yang benar sesuai menu diatas')
    
#main program
if __name__ == '__main__': #kondisi saat program dijalankan pada terminal, maka akan menjalankan code yang didalam kondisi ini 
    get_login()
    