import konversi

suhu = float(input("Masukan Suhu Yang Ingin Dikonversikan: "))
print("Pilih Konversi Suhu")
print("Celcius")
print("Fahrenheit")
print("Kelvin")
print("1. Celcius Ke Fahrenheit: ")
print("2. Fahrenheit Ke Celcius: ")
print("3. Celcius Ke Kelvin: ")
print("4. Kelvin Ke Celcius:")
print("5. Fahrenheit Ke Kelvin: ")
print("6. Kelvin Ke Fahrenheit: ")
pilihan = input("Masukan Pilihan (1-6): ")

if pilihan == "1":
    hasil = konversi.celciuskefahrenheit(suhu)
    print(f"Hasil: {suhu}'C = {hasil} 'F")
elif pilihan  == "2":
     hasil = konversi.farhrenheitkecelcius(suhu)
     print(f"Hasil: {suhu}'F = {hasil} 'C")
elif pilihan == "3":
     hasil = konversi.celciuskefahrenheit(suhu)
     print(f"Hasil: {suhu}'C = {hasil} 'F")
elif pilihan == "4":
    hasil = konversi.kelvinkecelcius(suhu)
    print(f"Hasil: {suhu}'K = {hasil} 'C")
elif pilihan == "5":
    hasil = konversi.farhrenheitkecelcius(suhu)
    print(f"Hasil: {suhu}'F = {hasil} 'C")
elif pilihan == "6":
    hasil = konversi.kelvinkefarhrenheit(suhu)
    print(f"Hasil: {suhu}'K = {hasil} 'F")
else:
    print("Pilihan Tidak Ada")
    