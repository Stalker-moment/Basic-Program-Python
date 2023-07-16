import sys
line = '\n-----------------\n' #line digunakan untuk display menu
def main_menu(): #fungsi main menu, digunakan untuk menampilkan list menu tools
    print (f'{line}Menu Pada Tools Ini:\n1. mengeja kata\n2. exit{line}')
    pilih = input ('silahkan pilih: ')
    if (pilih == '1' or pilih == 'mengeja kata'):
        balikkata()
    elif (pilih == 'exit' or pilih == '2'):
        exit()
    else:
        force_exit()
        
     
def balikkata(): #fungsi untuk mengeja kata
    kata = input ("masukan kata : ")
    jumlah = len(kata) #menghitung total jumlah huruf
    print('jumlah karakter =', jumlah)
    #print(jumlah)
    kata = kata
    count1 = 1 #menghitung jumlah huruf yang ditampilkan 
    count2 = 1 #menghitung jumlah huruf yang ditampilkan(reverse)
    print ('\nEjaan : ', end='')
    for huruf in kata: #digunakan untuk mengeja kata
        #print(count)
        if count1 < jumlah: #apabila belum huruf terakhir maka akan terdapat akhiran '-'
            count1+=1
            print (huruf, end ='-')
        elif count1 == jumlah: #apabila belum huruf terakhir maka akan tidak terdapat akhiran '-'
            print (huruf, end ='')
    balik = reverse(kata) #reverse kata
    print ('\nBalik : ', end='')
    for huruf in balik:
        if count2 < jumlah:
            count2+=1
            print (huruf, end ='-')
        elif count2 == jumlah:
            print (huruf, end ='')
        #print (huruf, end ='-')
    if (kata == balik):
        print ('\nKata awal dan yang dibalik sama') #mendeteksi apakah dibalik akan sama
        kemanaaaaaaaaaaaaaaaaaa()
    else:
        print ('\nKata awal dan yang dibalik berbeda')
        kemanaaaaaaaaaaaaaaaaaa()
        
def reverse(kata): #fungsi membalik kata
        return kata[::-1]
    
def kemanaaaaaaaaaaaaaaaaaa(): #fungsi digunakan untuk menanyakan user, setelah selesai menghitung
    kemana = input('Mau Gunakan Tools ini lagi? (y/n): ')
    if (kemana == 'y' or kemana == 'Y'):
        balikkata()
    elif (kemana == 't' or kemana == 'n' or kemana == 'N' or kemana == 'T'):
        main_menu()
    else:
        force_exit()
        
def exit():
    sys.exit(f'{line}Bye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')
def force_exit():
    sys.exit(f'{line}Ente kadang-kadang ente, minimal jawab yang bener\nBye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')
 

if __name__== '__main__':
    main_menu() 