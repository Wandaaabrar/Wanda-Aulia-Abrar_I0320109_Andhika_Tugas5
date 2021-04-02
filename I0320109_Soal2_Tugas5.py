nama = input("Inputkan Nama :")
skor = float(input("Input Nilai Akhir : "))
variabel = 'Hallo', nama, '!Nilai anda setelah dikonversikan adalah'

if skor >= 85:
    print(variabel,'A')
elif skor >= 80:
    print(variabel,'A-')
elif skor >= 75:
    print(variabel,'B+')
elif skor >= 70:
    print(variabel,'B')
elif skor >= 65:
    print(variabel,'C+')
elif skor >= 60:
    print(variabel,'C')
else:
    print(variabel,'E')