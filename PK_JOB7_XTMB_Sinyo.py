print('Gambar Pola Bintang, Query Yang Tersedia:\nA. Persegi\nB. Segitiga Siku-Siku\nC. Persegi Custom\nD. Exit')

while(True): 
    query = input('Masukkan Bentuk yang diinginkan:') #query sebagai inputan type bentuk
    if (query == 'A' or query == 'a' or query == 'persegi'): #Persegi
        tinggi = int(input('Masukkan tinggi bentuk: ')) #tinggi sebagai input tinggi bentuk
        persegi = tinggi + 1 #ditambah 1 karena mulai dari 1
        for i in range(1,persegi):
            print('*'*tinggi)
    elif (query == 'B' or query == 'b' or query == 'Segitiga Siku-Siku'): #Segitiga Siku-Siku
        tinggi = int(input('Masukkan tinggi bentuk: '))
        siku = tinggi + 1
        for i in range(1,siku):
            print('*'*i)
    elif (query == 'C' or query == 'c' or query == 'persegi custom'): #Persegi Custom (dapat menginput lebar dan tinggi bentuk persegi)
        tinggi = int(input('Masukkan tinggi bentuk: '))
        lebar = int(input('Masukkan lebar bentuk: '))
        persegi = tinggi + 1
        for i in range(1,persegi):
            print('*'*lebar)
    elif (query == 'D' or query == 'd' or query == 'exit'): #Exit keluar dari program
        print('terimakasi telah menggunakan program ini\nby : @tierkunn_ (Tier Sinyo)')
        break
    else :
        print('mohon masukkan query dengan benar')
