"""
        NO 1
bilanganPertama = "5"
bilanganKedua = "14" 

hasil = bilanganPertama + bilanganKedua
print("hasil penjumlahan adalah", hasil)
"""
#komen no 1 : bisa terbaca, tetapi tidak bisa dijumlahkan karena hanya terbaca string bukan bilangan

"""
        NO 2
a=input("input bilangan 1=")
b=input("input bilangan 2=")
c=(a)+(b)
print("hasil jumlah", c)
"""
#komen no 2 : bisa terbaca, tetapi tidak bisa dijumlahkan karena hanya terbaca string bukan bilangan

#NO 4
bil1 = input("input bilangan 1 :")
bil2 = input("input bilangan 2 :")

jumlah = int(bil1) + int(bil2)
kurang = int(bil1) - int(bil2)
kali = int(bil1) * int(bil2)
bagi = int(bil1) / int(bil2)
pangkat = int(bil1) ** int(bil2)

print("hasil penjumlah", jumlah)
print("hasil pengurangan", kurang)
print("hasil perkalian", kali)
print("hasil pembagian", bagi)
print("hasil pemangkatan", pangkat)

#NO 5
print("Menghitung rata-rata 5 bilangan\n")
bil1 = input("Masukkan Bilangan 1: ")
bil2 = input("Masukkan Bilangan 2: ")
bil3 = input("Masukkan Bilangan 3: ")
bil4 = input("Masukkan Bilangan 4: ")
bil5 = input("Masukkan Bilangan 5: ")

jumlah = (int(bil1) + int(bil2) + int(bil3) + int(bil4) + int(bil5)) 
rata = int(jumlah) / 5

print("\nHasil Jumlah 5 bilangan: " ,jumlah)
print("rata-rata:", rata)