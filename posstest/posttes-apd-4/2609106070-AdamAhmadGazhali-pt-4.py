username = "Adam"
password = "70"

percobaan = 0
login = False

while percobaan < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username.lower() == username.lower() and password == password:
        print("Login berhasil!")
        login = True
        break
    else:
        percobaan = percobaan + 1
        print("login gagal")

if login == False:
    print("Gagal login 3 kali. program akan keluar.")

while login == True:
    print("=== MENU DISTRIBUSI PAKET ===")
    print("1. paket Reguler")
    print("2. paket Anak")
    print("3. paket Keluarga")
    print("4. Keluar dari program")

    pilihan = input("Masukkan pilihan Anda (1-4): ")

    if pilihan == "1":
        jenis_paket = "Reguler"
        porsi = 1   

    elif pilihan == "2":
        jenis_paket = "Anak"
        porsi = 1

    elif pilihan == "3":
        jenis_paket = "Keluarga"
        porsi = 4

    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Opsi tidak valid")
        continue

jumlah = int(input("Masukkan jumlah paket= "))

total = 0 

for i in range(jumlah):
    total = total + porsi

if total >= 20:
    bonus = "5 paket buah"
elif total >= 10 and total < 20:
    bonus = "3 botol susu"
elif total >= 5 and total < 10:
    bonus = "1 paket vitamin    "

else:
    bonus = "Tidak ada bonus"

print("=== HASIL DISTRIBUSI PAKET ===")
print("Jenis paket:", jenis_paket)
print("Jumlah paket:", jumlah)
print("Total porsi:", total)    
print("Penerima:", total, "orang")
print("Bonus:", bonus)
