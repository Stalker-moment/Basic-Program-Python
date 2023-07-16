#input nilai
print('Program Penghitung Nilai Rapor')
harian = int(input('Nilai harian: '))
uas = int(input('Nilai UAS: '))

#menghitung nilai rapor
nilai_rapor= (3 * harian + 2 * uas) / 5

#untuk menentukan nilai huruf
if (nilai_rapor <= 100 and nilai_rapor >= 93):
    kategori = 'A'
elif (nilai_rapor <= 93 and nilai_rapor >= 86):
    kategori = 'B'
elif (nilai_rapor <= 86 and nilai_rapor >= 79):
    kategori = 'C'
elif (nilai_rapor <= 79 and nilai_rapor >= 72):
    kategori = 'D'
elif (nilai_rapor < 72):
    kategori = 'E (Tidak Lulus)'
else:
    kategori = '[NILAI DILUAR NALAR]'
    
print(f'\nNilai Rapor: {nilai_rapor} kategori {kategori}')    