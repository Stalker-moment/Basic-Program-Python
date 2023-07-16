print('Program Menghitung Volume\n1. Kubus\n2. Balok\n3. Tabung')
choice = str(input('Pilih Bentuk: '))

if (choice == '1' or choice.lower() == 'kubus'):
    sisi = int(input('Masukkan panjang sisi kubus (cm): '))
    volume = sisi ** 3
    print(f'Volume Kubus dengan sisi {sisi} cm adalah {volume} cm^3')
elif (choice == '2' or choice.lower() == 'balok'):
    panjang = int(input('Masukkan Panjang: '))
    lebar = int(input('Masukkan lebar: '))
    tinggi = int(input('Masukkan tinggi: '))
    volume = panjang * lebar * tinggi
    print(f'Volume Balok dengan ukuran {panjang} x {lebar} x {tinggi} cm adalah {volume} cm^3')
elif (choice == '3' or choice.lower() == 'tabung'):
    jari = int(input('Masukkan Jari-jari: '))
    tinggi = int(input('Masukkan tinggi: '))
    volume = 3.14 * jari * jari * tinggi
    volume_reborn = 22/7 * jari * jari * tinggi
    print(f'Volume Tabung dengan jari-jari {jari} cm dan {tinggi} cm adalah\n[Phi 3.14] = {volume} cm^3\n[Phi 22/7] = {volume_reborn} cm^3')
else:
    print('Pilihan Diluar Nalar...')
