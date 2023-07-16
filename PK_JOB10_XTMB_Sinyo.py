#PROGRAM JOB 10 (sebelum modifikasi)
'''
try:
    print('Mengitung Luas Bangun Datar------\nQuery Yang Tersedia:\n1. Persegi\n2. Persegi Panjang\n3. Jajar Genjang\n4. Segitiga Siku\n5. Belah Ketupat\n6. Lingkaran\n7. Trapesium\n8. Exit')
    line = '\n----------------------------------------------------------\n'
    kuadrat = '²'
    while(True):
        query = input('Masukkan Bentuk yang diinginkan:')
        if query == '1': #Persegi
            sisi = int(input('Masukkan sisi persegi: '))
            satuan = input('Masukan Satuan: ')
            luas = str(sisi * sisi)
            print('{}➤Rumus Luas Persegi = Sisi x Sisi\n➤Luas Persegi {}{} x {}{} = {}{}{} {}'\
                  .format(line, sisi, satuan, sisi, satuan, luas, satuan, kuadrat, line))
        elif query == '2': #Persegi Panjang
            panjang = int(input('Masukkan panjang persegi: '))
            lebar = int(input('Masukkan lebar persegi: '))
            satuan = input('Masukan Satuan: ')
            luas = str(panjang * lebar)
            print('{}➤Rumus Luas Persegi Panjang = panjang x lebar\n➤Luas Persegi Panjang {}{} x {}{} = {}{}{} {}'\
                  .format(line, panjang, satuan, lebar, satuan, luas, satuan, kuadrat, line))
        elif query == '3': #Jajar Genjang
            alas = int(input('Masukkan alas jajar genjang: '))
            tinggi = int(input('Masukkan tinggi jajar genjang: '))
            satuan = input('Masukan Satuan: ')
            luas = str(1 / 2 * alas * tinggi)
            print('{}➤Rumus Luas Jajar Genjang = ½ x alas x tinggi\n➤Luas Jajar Genjang ½ x {}{} x {}{} = {}{}{} {}'\
                  .format(line, alas, satuan, tinggi, satuan, luas, satuan, kuadrat, line))
        elif query == '4': #Segitiga Siku
            alas = int(input('Masukkan alas segitiga: '))
            tinggi = int(input('Masukkan tinggi segitiga: '))
            satuan = input('Masukan Satuan: ')
            luas = str(1 / 2 * alas * tinggi)
            print('{}➤Rumus Luas Segitiga Siku-Siku = ½ x alas x tinggi\n➤Luas Segitiga Siku-Siku ½ x {}{} x {}{} = {}{}{} {}'\
                  .format(line, alas, satuan, tinggi, satuan, luas, satuan, kuadrat, line))
        elif query == '5': #Belah Ketupat
            d1 = int(input('Masukkan d1 belah ketupat: '))
            d2 = int(input('Masukkan d2 belah ketupat: '))
            satuan = input('Masukan Satuan: ')
            luas = str(1 / 2 * d1 * d2)
            print('{}➤Rumus Luas Segitiga Siku-Siku = ½ × d1 × d2\n➤Luas belah ketupat ½ x {}{} x {}{} = {}{}{} {}'\
                  .format(line, d1, satuan, d2, satuan, luas, satuan, kuadrat, line))
        elif query == '6': #Lingkaran
            lingkaran = input('Menghitung lingkaran dengan apa?\nA. Jari-jari\nB. Diameter\nPilihanmu: ')
            if (lingkaran == 'A' or lingkaran == 'a' or lingkaran == 'jari-jari' or lingkaran == 'jari'):
                jari = int(input('Masukkan Jari-Jari lingkaran: '))
                satuan = input('Masukan Satuan: ')
                luas1 = str(22/7 * jari * jari)
                luas2 = str(3.14 * jari * jari)
                print('{}➤Rumus Luas Lingkaran (dengan jari-jari) = π × r × r\n➤Luas lingkaran (cara 1) 22/7 x {}{} x {}{} = {}{}{}\n➤Luas lingkaran (cara 2) 3,14 x {}{} x {}{} = {}{}{} {}'\
                      .format(line, jari, satuan, jari, satuan, luas1, satuan, kuadrat, jari, satuan, jari, satuan, luas2, satuan, kuadrat, line))
            elif (lingkaran =='B' or lingkaran == 'b' or lingkaran == 'diameter'):
                diameter = int(input('Masukkan diameter lingkaran: '))
                satuan = input('Masukan Satuan: ')
                luas1 = str(22/7 * (diameter/2) * (diameter/2))
                luas2 = str(3.14 * (diameter/2) * (diameter/2))
                print('{}➤Rumus Luas Lingkaran (dengan diameter) = π × (diameter / 2x 2)\n➤Luas lingkaran (cara 1) 22/7 x ({}{}/2x2) = {}{}{}\n➤Luas lingkaran (cara 2) 3,14 x ({}{}/2x2) = {}{}{} {}'\
                      .format(line, diameter, satuan, luas1, satuan, kuadrat, diameter, satuan, luas2, satuan, kuadrat, line))
            else:
                print('Input kamu salah, harap isi dengan benar')
        elif query == '7': #Trapesium
            atas = int(input('Masukkan panjang sisi sejajar atas: '))
            bawah = int(input('Masukkan panjang sisi sejajar bawah: '))
            tinggi = int(input('Masukkan tinggi trapesium: '))
            satuan = input('Masukan Satuan: ')
            luas = str(1 / 2 * (atas + bawah) * tinggi)
            print('{}➤Rumus Luas Trapesium = ½ × (sisi atas x sisi bawah) x tinggi\n➤Luas Trapesium ½ x ({}{} + {}{}) x {}{} = {}{}{} {}'\
                  .format(line, atas, satuan, bawah, satuan, tinggi, satuan, luas, satuan, kuadrat, line))

        elif query == '8': #Exit
            print('Terimakasih telah menggunakan program ini\nby : @tierkunn_ (Tier Sinyo)')
            break
        else :
            print('mohon masukkan query dengan benar')
except:
    print('Error\nMungkin Kesalah input')
'''

#PROGRAM JOB 10 (setelah dimodifikasi)

import sys #library digunakan untuk fungsi exit (warna merah pada tampilan exit)

username = 'kalkulator' #variable untuk menyimpan username
password = 'kalkal'     #variable untuk menyimpan password 
kuadrat = '²'           #digunakan untuk melengkapi kuadrat satuan
line = '------------'   #digunakan sebagai tampilan garis

def main_menu(): #tampilan utama (main menu)
    print(f'{line}Mengitung Luas Bangun Datar{line}\nQuery Yang Tersedia:')
    print('1. Persegi')
    print('2. Persegi Panjang')
    print('3. Jajar Genjang')
    print('4. Segitiga Siku')
    print('5. Belah Ketupat')
    print('6. Lingkaran')
    print('7. Trapesium')
    print('8. Exit')
    print('9. Logout')
    print(f'{line}{line}{line}')
    choice = input('Masukkan Pilihan anda: ')
    if(choice == '1' or choice == 'persegi'):
        persegi()
    elif(choice == '2' or choice == 'persegi panjang'):
        persegi_panjang()
    elif(choice == '3' or choice == 'jajar genjang'):
        jajar_genjang()
    elif(choice == '4' or choice == 'segitiga siku'):
        segitiga_siku()
    elif(choice == '5' or choice == 'belah ketupat'):
        belah_ketupat()
    elif(choice == '6' or choice == 'lingkaran'):
        lingkaran_luas()
    elif(choice == '7' or choice == 'trapesium'):
        trapesium()
    elif(choice == '8' or choice == 'exit'):
        exit()
    elif(choice == '9' or choice == 'logout'):
        logout()
    else:
        print(f'\n{line}⚠️Input salah   ⚠{line}\nHarap masukkan input sesuai pilihan diatas :)') #apabila pilihan tidak dipilih, maka akann menampilkan peringatan
        bingung_moment() #dan akan callback ke fungsi kebingungan 

def bingung_moment(): #fungsi ini digunakan untuk menanyakan seseorang saat kebingungan
    print('Kamu mau ngapain?')
    bingung = input(f'A. Kembali ke Main Menu\nB. Exit\n{line}{line}\nPilih : ')
    if(bingung == 'a' or bingung == 'A' or bingung == 'menu'):
        main_menu()
    if(bingung == 'b' or bingung == 'B' or bingung == 'exit'):
        exit()
    else:
        print(f'gabisa pake?\n{line}Program Exit Otomatis{line}')
        exit()
        
def login_kalkulator(): #fungsi login, sebelum masuk ke main menu
    print(f'{line}{line}{line}')
    print('login dulu sebelum menggunakan kalkulator')
    usernamei = input('masukkan username: ')
    passwordi = input('masukkan password: ')
    print(f'{line}{line}{line}')
    
    if usernamei == username and passwordi == password: #kondisi untuk username dan password
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi...')
        login_kalkulator()
        
def logout(): #fungsi untuk logout
    print('\nkamu telah logout...')
    again = input('login lagi? (y/n)') #input login lagi/tidak (bila iya akan masuk ke halaman login, jika tidak akan keluar dari program)
    if(again == 'y'):
        login_kalkulator() #callback fungsi login
    elif(again == 'n' or again == 't' or again == 'N' or again == 'T'):
        exit() #callback fungsi exit
    else:
        print(f'gabisa pake?\n{line}Program Exit Otomatis{line}')
        exit() #callback fungsi exit
        
def persegi(): #fungsi luas persegi
    sisi = int(input('Masukkan sisi persegi: '))
    satuan = input('Masukan Satuan: ')
    luas = str(sisi * sisi)
    print('{}{}\n➤Rumus Luas Persegi = Sisi x Sisi\n➤Luas Persegi {}{} x {}{} = {}{}{}\n{}{}'\
          .format(line, line, sisi, satuan, sisi, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ') #input saat program selesai menghitung, untuk memastikan apakah ingin menghitung lagi(berlaku untuk semua fungsi perhitungan luas)
    
    if(tanyain == 'y' or tanyain == 'Y'):
        persegi() #callback fungsi luas persegi saat user ingin menghitung ulang
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi() #callback fungsi tanya lagi saat user tidak menghitung ulang
    else:
        main_menu() #callback fungsi main menu saat user tidak memilih apapun
       
def persegi_panjang(): #fungsi luas persegi panjang
    panjang = int(input('Masukkan panjang persegi: '))
    lebar = int(input('Masukkan lebar persegi: '))
    satuan = input('Masukan Satuan: ')
    luas = str(panjang * lebar)
    print('{}{}\n➤Rumus Luas Persegi Panjang = panjang x lebar\n➤Luas Persegi Panjang {}{} x {}{} = {}{}{}\n{}{}'\
          .format(line, line, panjang, satuan, lebar, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ')
    
    if(tanyain == 'y' or tanyain == 'Y'):
        persegi_panjang()
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi()
    else:
        main_menu()
       
def jajar_genjang(): #fungsi luas jajar genjang
    alas = int(input('Masukkan alas jajar genjang: '))
    tinggi = int(input('Masukkan tinggi jajar genjang: '))
    satuan = input('Masukan Satuan: ')
    luas = str(1 / 2 * alas * tinggi)
    print('{}{}\n➤Rumus Luas Jajar Genjang = ½ x alas x tinggi\n➤Luas Jajar Genjang ½ x {}{} x {}{} = {}{}{}\n{}{}'\
          .format(line, line, alas, satuan, tinggi, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ')
    
    if(tanyain == 'y' or tanyain == 'Y'):
        jajar_genjang()
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi()
    else:
        main_menu()
       
def segitiga_siku(): #fungsi luas segitiga siku-siku
    alas = int(input('Masukkan alas segitiga: '))
    tinggi = int(input('Masukkan tinggi segitiga: '))
    satuan = input('Masukan Satuan: ')
    luas = str(1 / 2 * alas * tinggi)
    print('{}{}\n➤Rumus Luas Segitiga Siku-Siku = ½ x alas x tinggi\n➤Luas Segitiga Siku-Siku ½ x {}{} x {}{} = {}{}{}\n{}{}'\
          .format(line, line, alas, satuan, tinggi, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ')

    if(tanyain == 'y' or tanyain == 'Y'):
        segitiga_siku()
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi()
    else:
        main_menu()    
       
def belah_ketupat(): #fungsi luas belah ketupat
    d1 = int(input('Masukkan d1 belah ketupat: '))
    d2 = int(input('Masukkan d2 belah ketupat: '))
    satuan = input('Masukan Satuan: ')
    luas = str(1 / 2 * d1 * d2)
    print('{}{}\n➤Rumus Luas Segitiga Siku-Siku = ½ × d1 × d2\n➤Luas belah ketupat ½ x {}{} x {}{} = {}{}{}\n{}{}'\
          .format(line, line, d1, satuan, d2, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ')

    if(tanyain == 'y' or tanyain == 'Y'):
        belah_ketupat()
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi()
    else:
        main_menu()    
       
def lingkaran_luas(): #fungsi luas lingkaran
    lingkaran = input('Menghitung lingkaran dengan apa?\nA. Jari-jari\nB. Diameter\nPilihanmu: ')
    if (lingkaran == 'A' or lingkaran == 'a' or lingkaran == 'jari-jari' or lingkaran == 'jari'): #menghitung luas berdasarkan jari-jari
        jari = int(input('Masukkan Jari-Jari lingkaran: '))
        satuan = input('Masukan Satuan: ')
        luas1 = str(22/7 * jari * jari)
        luas2 = str(3.14 * jari * jari)
        print('{}{}\n➤Rumus Luas Lingkaran (dengan jari-jari) = π × r × r\n➤Luas lingkaran (cara 1) 22/7 x {}{} x {}{} = {}{}{}\n➤Luas lingkaran (cara 2) 3,14 x {}{} x {}{} = {}{}{}\n{}{}'\
              .format(line, line, jari, satuan, jari, satuan, luas1, satuan, kuadrat, jari, satuan, jari, satuan, luas2, satuan, kuadrat, line, line))
        tanyain = input('hitung lagi? (y/n): ')

        if(tanyain == 'y' or tanyain == 'Y'):
            lingkaran_luas()
        elif(tanyain == 't' or tanyain == 'T'):
            tanya_lagi()
        else:
            main_menu()    
            
    elif (lingkaran =='B' or lingkaran == 'b' or lingkaran == 'diameter'): #menghitung luas berdasarkan diameter
        diameter = int(input('Masukkan diameter lingkaran: '))
        satuan = input('Masukan Satuan: ')
        luas1 = str(22/7 * (diameter/2) * (diameter/2))
        luas2 = str(3.14 * (diameter/2) * (diameter/2))
        print('{}➤Rumus Luas Lingkaran (dengan diameter) = π × (diameter / 2x 2)\n➤Luas lingkaran (cara 1) 22/7 x ({}{}/2x2) = {}{}{}\n➤Luas lingkaran (cara 2) 3,14 x ({}{}/2x2) = {}{}{}\n{}{}'\
              .format(line, diameter, satuan, luas1, satuan, kuadrat, diameter, satuan, luas2, satuan, kuadrat, line, line))
        tanyain = input('hitung lagi? (y/n): ')

        if(tanyain == 'y' or tanyain == 'Y'):
            lingkaran_luas()
        elif(tanyain == 't' or tanyain == 'T'):
            tanya_lagi()
        else:
            main_menu()    
    else:
        print('Input kamu salah, harap isi dengan benar')
        lingkaran_luas()
       
def trapesium(): #fungsi luas trapesium
    atas = int(input('Masukkan panjang sisi sejajar atas: '))
    bawah = int(input('Masukkan panjang sisi sejajar bawah: '))
    tinggi = int(input('Masukkan tinggi trapesium: '))
    satuan = input('Masukan Satuan: ')
    luas = str(1 / 2 * (atas + bawah) * tinggi)
    print('{}{}\n➤Rumus Luas Trapesium = ½ × (sisi atas x sisi bawah) x tinggi\n➤Luas Trapesium ½ x ({}{} + {}{}) x {}{} = {}{}{}\n{}{}'\
          .format(line, line, atas, satuan, bawah, satuan, tinggi, satuan, luas, satuan, kuadrat, line, line))
    tanyain = input('hitung lagi? (y/n): ')

    if(tanyain == 'y' or tanyain == 'Y'):
        trapesium()
    elif(tanyain == 't' or tanyain == 'T'):
        tanya_lagi()
    else:
        main_menu()    

def tanya_lagi(): #fungsi tanya lagi, saat seseorang tidak menghitung lagi
    tanyalagi = input('Mau kemana?\n1. Menu\n2. Exit\n---> ')
    if (tanyalagi == '1' or tanyalagi == 'menu'):
        main_menu()
    elif (tanyalagi == '2' or tanyalagi == 'exit'):
        exit()
    else:
        print('eits.... isi dulu boss....')
        tanya_lagi()

def exit(): #fungsi exit (keluar dari program)
    sys.exit(f'{line}{line}{line}\nTerimakasih telah menggunakan tools ini\nby : @tierkunn_ (Tier Sinyo)\n{line}{line}{line}')

#main program
if __name__ == '__main__': #kondisi saat program dijalankan pada terminal, maka akan menjalankan code yang didalam kondisi ini 
    login_kalkulator()
