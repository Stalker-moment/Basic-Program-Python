
print('Kalkulator Sederhana\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Exit')
while(True): #program ini di dalam looping, agar program dapat digunakan berkali-kali, untuk keluar menggunakan query exit
    query = input("Pilih Operasi Yang Ingin Dilakukan: ") #query adalah input untuk memilih operasi, yang nantinya data diolah oleh kondisi (if/else)
    if (query == '1' or query == 'tambah' or query == 'Tambah' or query == '1.'): # Pertambahan
        bil1 = input('Bilangan Pertama : ') #bil1 adalah input untuk bilangan pertama
        bil2 = input('Bilangan Kedua : ')   #bil2 adalah input untuk bilangan kedua
        perhitungan = int(bil1) + int(bil2) #perhitungan digunakan sebagai konversi str le int yang nntinya akan dihitung
        print('Hasil Pertambahan dari '+bil1+' + '+bil2+' =', perhitungan)
    elif (query == '2' or query == 'kurang' or query == 'Kurang' or query == '2.'): # Pengurangan
        bil1 = input('Bilangan Pertama : ')
        bil2 = input('Bilangan Kedua : ')
        perhitungan = int(bil1) - int(bil2) 
        print('Hasil Pengurangan dari '+bil1+' - '+bil2+ ' =', perhitungan)
    elif (query == '3'  or query == 'kali' or query == 'Kali' or query == '3.'): # Perkalian
        bil1 = input('Bilangan Pertama : ')
        bil2 = input('Bilangan Kedua : ')
        perhitungan = int(bil1) * int(bil2)
        print('Hasil Perkalian dari '+bil1+' x '+bil2+ ' =', perhitungan)
    elif (query == '4' or query == 'bagi' or query == 'Bagi' or query == '4.'): # Pembagian
        bil1 = input('Bilangan Pertama : ')
        bil2 = input('Bilangan Kedua : ')
        perhitungan = int(bil1) / int(bil2)
        print('Hasil Pembagian dari '+bil1+' : '+bil2+' =', perhitungan)
    elif (query == '5' or query == 'exit' or query == 'Exit' or query == '5.'): # Keluar dari kalkulator
        print('Terimakasih telah menggunakan kalkulator sederhana ini\nby : @tierkunn_ (Tier Sinyo)')
        break #break untuk menghentikan fungsi looping,program kalkulator akan berhenti
    else :
        print('harap masukan option dengan benar') #apabila query tidak sesuai dengan program, maka akan diberikan peringatan dari else

    
    