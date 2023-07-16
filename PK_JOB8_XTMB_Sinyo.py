kata1 = input("Masukkan kata pertama: ") #kata1 sebagai input kata pertama
kata2 = input("Masukkan kata kedua  : ") #kata2 sebagai input kata kedua

try:
    ulang = int(input("masukkan Perulangan :")) #ulang sebagai input jumlah perulangan
  
    if ulang % 2 == 0: #untuk deteksi bilangan ganjil/genap
        deteksi = 'genap'
    else:
        deteksi = 'ganjil'

    for i in range(ulang): #penggabungan dan perulangan kata
        print((kata1 + kata2), f"- {i+1}")
        
    print('({})'\
          .format(deteksi)) #output deteksi

except:
    print("Input anda salah, harap masukkan bilangan pada inputan ulang") #apabila input ulang bukan berupa angka/bilangan, maka alert ini akan muncul


