import sys
import base64

exitmsg = 'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KVGhhbmtzIEZvciBVc2UgVGhpcyBUb29scwpCeSA6IEB0aWVya3Vubl8gKFRpZXIgU2lueW8pCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0='

def main_menu():
    print('program menghitung Body Mass Index\n1. BMI\n2. Exit')
    best_choice = input('Pilih: ')
    if (best_choice == '1' or best_choice.lower() == 'bmi'):
        bmi_program()
    if (best_choice == '2' or best_choice.upper() == 'EXIT'):
        exit()
    else:
        print('Please Choice Menu...')
        main_menu()
        
def bmi_program():
    berat = int(input('Berat badan anda (kg) : '))
    tinggi = int(input('Tinggi badan anda (cm) : '))
    bmi_moment = berat / (tinggi ** 2) * 10000
    if (bmi_moment > 30):
        bmi_status = 'Obesitas'
    elif (bmi_moment <= 30 and bmi_moment >= 25):
        bmi_status = 'Overweight'
    elif (bmi_moment <= 25 and bmi_moment > 18.5):
        bmi_status = 'Optimal'
    if (bmi_moment <= 18.5):
        bmi_status = 'Underweight'
        
    print(f'Nilai BMI anda adalah {bmi_moment} masuk kategori {bmi_status}')
    tanyain()
    
def tanyain():
    question = input('\nMau Ngapain Lagi?\n1. Hitung Ulang\n2. Main Menu\n3. Exit\nChoice : ')
    if (question == '1' or question.lower() == 'hitung ulang'):
        bmi_program()
    if (question == '2' or question.upper() == 'MAIN MENU'):
        main_menu()
    if (question == '3' or question.upper() == 'EXIT'):
        exit()    
    else:
        print('Please Choice Menu...')
        tanyain()
        
def exit():
    base64_bytes = exitmsg.encode("ascii") #encode base64 (anti recode exit message:v)
    string_bytes = base64.b64decode(base64_bytes)
    encode_exit = string_bytes.decode("ascii")
    sys.exit(encode_exit)
    
if __name__=='__main__':
    main_menu()    