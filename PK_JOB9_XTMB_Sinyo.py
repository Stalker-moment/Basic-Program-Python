#Method 1 (manual)
try:
    print('Konversi Satuan Panjang (mm, cm, dm, m, dam, hm, km)')
    awal = input('satuan Awal: ')
    akhir = input('Satuan Akhir: ')
    query = awal+'-'+akhir
    print(query)

    if query == 'mm-km':
        koreksi = 0.000001
    elif query == 'mm-hm':
        koreksi = 0.00001
    elif query == 'mm-dam':
        koreksi = 0.0001
    elif query == 'mm-m':
        koreksi = 0.001
    elif query == 'mm-dm':
        koreksi = 0.01
    elif query == 'mm-cm':
        koreksi = 0.1
    elif query == 'mm-mm':
        koreksi = 1
    elif query == 'cm-mm':
        koreksi = 10
    elif query == 'cm-cm':
        koreksi = 1
    elif query == 'cm-dm':
        koreksi = 0.1
    elif query == 'cm-m':
        koreksi = 0.01
    elif query == 'cm-dam':
        koreksi = 0.001
    elif query == 'cm-hm':
        koreksi = 0.0001
    elif query == 'cm-km':
        koreksi = 0.00001
    elif query == 'dm-cm':
        koreksi = 10
    elif query == 'dm-mm':
        koreksi = 100
    elif query == 'dm-dm':
        koreksi = 1
    elif query == 'dm-m':
        koreksi = 0.1
    elif query == 'dm-dam':
        koreksi = 0.01
    elif query == 'dm-hm':
        koreksi = 0.001
    elif query == 'dm-km':
        koreksi = 0.0001
    elif query == 'm-dm':
        koreksi = 10
    elif query == 'm-cm':
        koreksi = 100
    elif query == 'm-mm':
        koreksi = 1000
    elif query == 'm-m':
        koreksi = 1
    elif query == 'm-dam':
        koreksi = 0.1
    elif query == 'm-hm':
        koreksi = 0.01
    elif query == 'm-km':
        koreksi = 0.001
    elif query == 'dam-dam':
        koreksi = 1
    elif query == 'dam-m':
        koreksi = 10
    elif query == 'dam-dm':
        koreksi = 100
    elif query == 'dam-cm':
        koreksi = 1000
    elif query == 'dam-mm':
        koreksi = 10000
    elif query == 'dam-hm':
        koreksi = 0.1
    elif query == 'dam-km':
        koreksi = 0.01
    elif query == 'hm-mm':
        koreksi = 100000
    elif query == 'hm-cm':
        koreksi = 10000
    elif query == 'hm-dm':
        koreksi = 1000
    elif query == 'hm-m':
        koreksi = 100
    elif query == 'hm-dam':
        koreksi = 10
    elif query == 'hm-hm':
        koreksi = 1
    elif query == 'hm-km':
        koreksi = 0.1
    elif query == 'km-mm':
        koreksi = 1000000
    elif query == 'km-cm':
        koreksi = 100000
    elif query == 'km-dm':
        koreksi = 10000
    elif query == 'km-m':
        koreksi = 1000
    elif query == 'km-dam':
        koreksi = 100
    elif query == 'km-hm':
        koreksi = 10
    elif query == 'km-km':
        koreksi = 1
    else:
        print('query '+query+' tidak ditemukan')
        
    nilai = input('Nilai yang ingin dikonversi ({}) :'\
                  .format(awal))
    konversi = int(nilai) * koreksi
    print('Hasil : {} {} = {} {}'\
        .format(nilai, awal, konversi, akhir))

except:
    print("Error!\nMungkin Input anda salah, harap masukkan input dengan benar:)")
    
#Method 2 (Mathematics)
try:    
    print('Konversi Satuan Panjang (mm, cm, dm, m, dam, hm, km)')
    awal = input ('satuan awal : ')
    akhir = input ('satuan akhir : ')
    nilai = int(input ('Nilai yang dokonversikan : '))

    if  (awal == 'km' ):
        a = 1000000
    elif  (awal == 'hm' ):
        a = 100000
    elif  (awal == 'dam' ):
        a = 10000
    elif  (awal == 'm' ):
        a = 1000
    elif  (awal == 'dm' ):
        a = 100
    elif  (awal == 'cm' ):
        a = 10
    elif  (awal == 'mm' ):
        a = 1
        
    if  (akhir == 'km' ):
        b = 1000000
    elif  (akhir == 'hm' ):
        b = 100000
    elif  (akhir == 'dam' ):
        b = 10000
    elif  (akhir == 'm' ):
        b = 1000
    elif  (akhir == 'dm' ):
        b = 100
    elif  (akhir == 'cm' ):
        b = 10
    elif  (akhir == 'mm' ):
        b = 1
        
    hasil = a/b*nilai
    print(nilai,awal,'=',hasil,akhir)
except:
    print('error\nmungkin input anda salah')
