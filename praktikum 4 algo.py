print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

print('---- PROGRAM KONVERSI BILANGAN ----')

while True:
    print("Pilihan:")
    print("1. Angka ke Biner")
    print("2. Biner ke Angka")
    print("3. Exit")
    
    pilihan = input("Masukkan pilihan anda ->: ")
    
    if pilihan == '1':
        input_angka = int(input("Masukkan angka: "))
        binary_result = ""
        while input_angka > 0:
            remainder = input_angka % 2
            binary_result = str(remainder) + binary_result
            input_angka = input_angka // 2
        print(f"Hasil konversi ke biner: {binary_result}")
    elif pilihan == '2':
        binary_input = input("Masukkan bilangan biner: ")
        angka_result = 0
        for digit in binary_input:
            angka_result = angka_result * 2 + int(digit)
        print(f"Hasil konversi ke angka: {angka_result}")
    elif pilihan == '3':
        print("Terimakasih!!!!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')


input_angka = input("Masukkan List Angka (integer) ->  ")
angka = [int(x) for x in input_angka.split()]

terdapat_genap = False

for a in angka:
    if a % 2 == 0:
        terdapat_genap = True
        break

if terdapat_genap:
    print("List memiliki angka genap")
else:
    print("List tidak memiliki angka genap")

