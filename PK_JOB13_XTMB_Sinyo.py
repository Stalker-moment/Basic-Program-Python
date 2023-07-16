import sys #alternatif exit, karena membuat fungsi exit
class colors: #digunakan untuk mewarnai teks
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

line = '\n---------------------------\n' #line digunakan untuk display menu
def main_menu():
    #print ('\n\nPilihan konversi : ')
    print(colors.OKBLUE + f'{line}Pilihan konversi : ' + colors.ENDC)
    print(colors.OKBLUE + f'1. Desimal ke biner\n2. Biner ke desimal\n3. exit{line}' + colors.ENDC)
    
    query = input(colors.OKBLUE + 'Pilih opsi : ' + colors.ENDC)
    
    if (query == '1' or query == 'Desimal ke biner'):
        desimal_biner()
    elif (query == '2' or query == 'Biner ke desimal'):
        biner_desimal()
    elif (query == '3' or query == 'exit'):
        exit()
    else:
        force_exit()
        
def desimal_biner(): #fungsi konversi desimal ke biner
    desimals = int(input(colors.OKBLUE + 'Bilangan positif desimal : ' + colors.ENDC))
    
    list_temp = []
    i = 0
    while desimals > 0:
        list_temp.append(desimals % 2) 
        desimals = desimals // 2
        i =i+1
        
    print (colors.OKGREEN + 'Hasil konversi (desimal) : ', end = '' + colors.ENDC)
    
    for i in range (i-1, -1, -1):
        print(list_temp[i], end = '')
        
    bro = input(colors.OKBLUE + '\nKonversi Lagi? (y/n): ' + colors.ENDC)
    if (bro == 'y' or bro == 'Y'):
        desimal_biner()
    elif (bro == 't' or bro == 'T' or bro == 'n' or bro == 'N'):    
        kemana()
    else:
        force_exit()
        
def biner_desimal(): #fungsi konversi biner ke desimal
    biner = int(input(colors.OKBLUE + 'Bilangan positif biner : ' + colors.ENDC))
    
    desimal = 0
    cnv = 1
    while (biner !=0):
        digit = biner % 10
        desimal = desimal + (digit*cnv)
        cnv = cnv*2;
        biner = biner // 10
        
    print (colors.OKGREEN + 'Hasil konversi (biner) : ' + colors.ENDC, desimal)
    
    bro = input(colors.OKBLUE + '\nKonversi Lagi? (y/n): ' + colors.ENDC)
    if (bro == 'y' or bro == 'Y'):
        desimal_biner()
    elif (bro == 't' or bro == 'T' or bro == 'n' or bro == 'N'):    
        kemana()
    else:
        force_exit()
    
def kemana(): #fungsi tanya apabila tidak menghitung kembali
    kemana = input(colors.OKBLUE + 'Mau balik ke main menu? (y/n): ' + colors.ENDC)
    if (kemana == 'y' or kemana == 'Y'):
        main_menu()
    elif (kemana == 't' or kemana == 'n' or kemana == 'N' or kemana == 'T'):
        exit()
    else:
        force_exit()
        
def exit(): #fungsi keluar program
    sys.exit(f'{line}Bye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')
def force_exit(): #fungsi keluar program paksa
    sys.exit(f'{line}Ente kadang-kadang ente, minimal jawab yang bener\nBye-Bye,Terimakasih telah menggunakan tools ini\nBy: @tierkunn_ (Tier Sinyo){line}')    

if __name__=='__main__':
    main_menu()
    
    
        

