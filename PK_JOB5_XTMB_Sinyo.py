#Program 1
"""
jawab = 'y'
hitung = 0

while(jawab == 'y'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    
print ("Total perulangan: " + str(hitung))
"""

#Program 2
"""
jawab = 'y'
hitung = 0

while(True):
    hitung += 1
    jawab = input("ulang lagi tidak? ")
    if jawab == 't':
        break
    
print ("Total perulangan: " + str(hitung))
"""

# No 1 : Perbedaan Program 1 dengan Program 2 adalah pada program 1 hanya memiliki 1 input yaitu "y" apabila input tidak sesuai
# maka program akan berhenti dan akan menghitung perulangan, dan pada program 2 memiliki 2 input yaitu "y" dan "t", y digunakan
# untuk perulangan dan apabila inputan berupa t program akan berhenti dan menghitung perulangan, apabila input selain 2 input tadi
# maka program tetap menghitung perulangan berbeda dengan program 1 yang langsung menghentikan perulangan

#No 2 method 1:

jawab = ''
jawaban_benar = 'ayam'
hitung = 0
print("kuis buat kamu, jawab yaaa....\n")

while(True):
    hitung += 1
    jawab = input("Hewan berkaki 2 dapat berkokok? ")
    if jawab == jawaban_benar:
        break
    
print ("jawaban benar!\nkamu berusaha menjawab selama: " + str(hitung) + " Percobaan")

#No 2 method 2:
jawab = ''
jawaban_benar = 'ayam'
hitung = 0
print("kuis buat kamu, jawab yaaa....\n")

while(True):
    hitung += 1
    jawab = input("Hewan berkaki 2 dapat berkokok?\n\nketik 'help' untuk bantuan, 'nyerah' untuk menyerah\n  Jawab :")
    if jawab == jawaban_benar:
        print ("jawaban benar!\nkamu berusaha menjawab selama: " + str(hitung) + " Percobaan")
        break
    elif jawab == 'help':
        print("bantuan : A _ Y _ M")
    elif jawab == 'nyerah': 
        print("Yah... menyerah, jawabannya {}" \
              .input(jawaban_benar))
        break
    elif jawab == jawab:
        print("Salah cuy, coba lagi")
    
    