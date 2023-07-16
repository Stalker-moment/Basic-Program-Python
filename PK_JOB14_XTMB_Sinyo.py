import sys
line = '\n-----------------\n' #line digunakan untuk display menu
def main_menu():
    print (f'{line}Menu Tools:')
    print (f'1. Hitung vokal dan konsonan\n2. exit{line}')
    
    query = input('Pilihan anda: ')
    
    if (query == '1' or query == 'Hitung vokal dan konsonan : '):
        huruf()
    elif (query == '2' or query == 'exit'):
        exit()  
    else:
        force_exit()
        
#menghitung konsonan, vokal, dan spasi
def huruf():
    kataa = input('kata : ')
    count1 = 0 
    count2 = 0
    count3 = 0
    temp1=''
    temp2=''
    for vokal in kataa: #apabila konsonan,vokal,spasi terhitung, maka temp akan terisi jumlah perhitungan
        if vokal == 'a' or vokal == 'i' or vokal == 'u' or vokal == 'e' or vokal == 'o' or vokal == 'A' or vokal == 'I' or vokal == 'U' or vokal == 'E' or vokal == 'O':
            count1+=1
            temp1+=vokal+''
        elif vokal == ' ':
            count2+=1
        else:
            count3+=1
            temp2+=vokal+''
    print('huruf vokal: ',count1,'buah')
    print('huruf konsonan: ',count3,'buah')
    print('spasi: ',count2,'buah')
    again = input('Hitung lagi? (y/n) : ')
    if (again == 'y' or again == 'Y'):
        huruf()
    elif(again == 'n' or again == 'N' or again == 't' or again == 'T'):
        main_menu()
    else:
        force_exit()
        
def exit():
    sys.exit(f'{line}Bye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')
def force_exit():
    sys.exit(f'{line}Ente kadang-kadang ente, minimal jawab yang bener\nBye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')    

if __name__=='__main__':
    main_menu()