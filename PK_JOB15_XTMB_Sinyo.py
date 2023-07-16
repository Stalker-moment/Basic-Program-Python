import sys

line = '\n-----------------\n' #line digunakan untuk display menu
barang_wajib = ('sabun 2','masker 1','beras 5') #daftar barang wajib
barang_tambahan = [] #daftar barang tambahan menggunakan list agar dapat ditambahkan
#membuat menu
def main_menu():
    print ('Daftar Belanja Bulanan')
    print ('1. Daftar Belanja Bulanan\n2. exit') #pilihan menu
    
    pilih = input ('pilih menu yang kamu mau: ') #input pilihan menu
    if (pilih == 'exit' or pilih == '2'):
        exit()
    elif (pilih == '1'):
        barang()
    else:
        force_exit()
        
#input barang dan jumlah barang
def barang():
    jawab = 'y'
    nama = input ('Nama barang: ')
    jumlah = input ('Jumlah : ')
    barang_tambahan.append (nama + ' ' + jumlah)
    
    jawab = input ('Tambah lagi? (y/t)')
    if jawab == 't':
        daftar()
    elif jawab == 'y':
        barang()
    else:
        print('eitss... diisi dulu')
        barang()
        
#list daftar belanja
def daftar():
    print ('Daftar Belanja')
    
    for i in barang_wajib:
        print (i)
        
    for a in barang_tambahan:
        print (a)

def exit(): #fungsi keluar program
    sys.exit(f'{line}Bye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')
def force_exit(): #fungsi keluar program secara paksa (apabila user tidak merespon dengan benar)
    sys.exit(f'{line}Ente kadang-kadang ente, minimal jawab yang bener\nBye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')    
   
#main program        
if __name__== '__main__':
    main_menu()
