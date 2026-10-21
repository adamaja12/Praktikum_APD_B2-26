import os

users = {"adam": {"password": "adam12", "peran": "Admin"}}

members = {}

PAKET = {"1": "1 Bulan", "2": "3 Bulan", "3": "6 Bulan"}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== SISTEM PENDATAAN ANGGOTA GYM ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        username = input("Username: ")
        pw = input("Password: ")
        peran = ""

        if username in users and users[username]["password"] == pw:
            peran = users[username]["peran"]

        if peran == "":
            print("Login gagal!")
        else:
            print("Login berhasil!")

            while True:
                if peran == "Admin":
                    print("=== MENU ADMIN ===")
                    print("1. Tambah anggota")
                    print("2. Lihat daftar anggota")
                    print("3. Ubah anggota")
                    print("4. Hapus anggota")
                    print("5. Logout")
                else:
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat daftar anggota")
                    print("2. Cek status anggota")
                    print("3. Logout")

                p = input("Pilih: ")

                if peran == "Admin" and p == "1":
                    nama = input("Nama anggota: ")
                    hp = input("Nomor HP: ")
                    print("1. Paket 1 Bulan")
                    print("2. Paket 3 Bulan")
                    print("3. Paket 6 Bulan")
                    paket = input("Pilih paket: ")

                    if nama and hp.isdigit() and paket in PAKET:
                        ida = max(members, default=0) + 1
                        members[ida] = {
                            "nama": nama,
                            "hp": hp,
                            "paket": PAKET[paket],
                            "status": "Aktif"
                        }
                        print("Anggota berhasil ditambahkan!")
                    else:
                        print("Data tidak valid!")

                elif (peran == "Admin" and p == "2") or (peran != "Admin" and p == "1"):
                    if not members:
                        print("Belum ada data anggota.")
                    for ida, data in members.items():
                        print("ID:", ida)
                        print("Nama:", data["nama"])
                        print("No HP:", data["hp"])
                        print("Paket:", data["paket"])
                        print("Status:", data["status"])

                elif peran == "Admin" and p in ["3", "4"]:
                    for ida, data in members.items():
                        print("ID:", ida, "Nama:", data["nama"])

                    pilih_id = input("Masukkan ID anggota: ")

                    if pilih_id.isdigit() and int(pilih_id) in members:
                        ida = int(pilih_id)

                        if p == "3":
                            print("1. Ubah nomor HP")
                            print("2. Perbarui paket")
                            ubah = input("Pilih perubahan: ")

                            if ubah == "1":
                                hp = input("Nomor HP baru: ")
                                if hp.isdigit():
                                    members[ida]["hp"] = hp
                                    print("Nomor HP berhasil diubah!")
                                else:
                                    print("Nomor HP tidak valid!")

                            elif ubah == "2":
                                print("1. Paket 1 Bulan")
                                print("2. Paket 3 Bulan")
                                print("3. Paket 6 Bulan")
                                paket = input("Pilih paket baru: ")

                                if paket in PAKET:
                                    members[ida]["paket"] = PAKET[paket]
                                    members[ida]["status"] = "Aktif"
                                    print("Paket berhasil diperbarui!")
                                else:
                                    print("Paket tidak tersedia!")

                        else:
                            if input("Hapus data? (y/n): ").lower() == "y":
                                del members[ida]
                                print("Data anggota berhasil dihapus!")
                            else:
                                print("Penghapusan dibatalkan!")
                    else:
                        print("Anggota tidak ditemukan!")

                elif peran != "Admin" and p == "2":
                    pilih_id = input("Masukkan ID anggota: ")

                    if pilih_id.isdigit() and int(pilih_id) in members:
                        data = members[int(pilih_id)]
                        print("Nama:", data["nama"])
                        print("Status:", data["status"])
                    else:
                        print("Anggota tidak ditemukan!")

                elif (peran == "Admin" and p == "5") or (peran != "Admin" and p == "3"):
                    break
                else:
                    print("Menu tidak tersedia!")

                input("Tekan Enter untuk lanjut...")

    elif pilih == "2":
        username = input("Username: ")
        pw = input("Password: ")

        if username and pw and username not in users:
            users[username] = {"password": pw, "peran": "Pengguna"}
            print("Register berhasil!")
        else:
            print("Username tidak valid atau sudah ada!")

    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Menu tidak tersedia!")

    input("Tekan Enter untuk lanjut...")