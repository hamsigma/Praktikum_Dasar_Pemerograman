#hitung volume Balok Kubus Dan Tabung
import hitungvolume

print("1. Hitung Volume Balok: ")
print("2. Hitung Volume Kubus: ")
print("3. Hitung Volume Tabung: ")
pilihan = int(input("Masukan Pilihan: "))

if pilihan == 1:
    panjang = int(input("Panjang: "))
    lebar = int(input("Lebar: "))
    tinggi = int(input("Tinggi: "))
    print(f"Volume Balok : {hitungvolume.volumebalok(panjang,lebar,tinggi)}")
elif pilihan == 2:
    sisi = int(input("Sisi: "))
    print(f"Volume Kubus: {hitungvolume.volumekubus(sisi)}")
elif pilihan == 3:
    jari = int(input("jari - jari: "))
    tinggi = int(input("Tinggi: "))
    print(f"volume tabung: {int(hitungvolume.volumetabung(jari,tinggi))}")
else:
    print("Tidak ada pilihan")
    
    
cekatribut = dir(hitungvolume)
print(cekatribut)
#dir di gunakan untuk mengecek atribut dan berbagai fungsi di dalam codingan
    