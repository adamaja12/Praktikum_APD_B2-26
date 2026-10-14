import os

users = [["adam", "adam12", "Admin"]]
members = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== SISTEM PENDATAAN ANGGOTA GYM ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Username: ")
        pw = input("Password: ")
        peran = ""

        for u in users:
            if u[0] == nama and u[1] == pw:
                peran = u[2]

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

                    if nama and hp.isdigit() and paket in ["1", "2", "3"]:
                        idm = max([m[0] for m in members], default=0) + 1
                        nama_paket = ["1 Bulan", "3 Bulan", "6 Bulan"][int(paket)-1]
                        members.append([idm, nama, hp, nama_paket, "Aktif"])
                        print("Anggota berhasil ditambahkan!")
                    else:
                        print("Data tidak valid!")

                elif (peran == "Admin" and p == "2") or (peran != "Admin" and p == "1"):
                    if not members:
                        print("Belum ada data anggota.")
                    for m in members:
                        print("ID:", m[0])
                        print("Nama:", m[1])
                        print("No HP:", m[2])
                        print("Paket:", m[3])
                        print("Status:", m[4])

                elif peran == "Admin" and p in ["3", "4"]:
                    for m in members:
                        print("ID:", m[0], "Nama:", m[1])

                    idm = input("Masukkan ID anggota: ")
                    ketemu = False

                    for m in members:
                        if str(m[0]) == idm:
                            ketemu = True

                            if p == "3":
                                print("1. Ubah nomor HP")
                                print("2. Perbarui paket")
                                ubah = input("Pilih perubahan: ")

                                if ubah == "1":
                                    hp = input("Nomor HP baru: ")
                                    if hp.isdigit():
                                        m[2] = hp
                                        print("Nomor HP berhasil diubah!")
                                    else:
                                        print("Nomor HP tidak valid!")

                                elif ubah == "2":
                                    print("1. Paket 1 Bulan")
                                    print("2. Paket 3 Bulan")
                                    print("3. Paket 6 Bulan")
                                    paket = input("Pilih paket baru: ")

                                    if paket in ["1", "2", "3"]:
                                        m[3] = ["1 Bulan", "3 Bulan", "6 Bulan"][int(paket)-1]
                                        m[4] = "Aktif"
                                        print("Paket berhasil diperbarui!")
                                    else:
                                        print("Paket tidak tersedia!")

                            else:
                                if input("Hapus data? (y/n): ").lower() == "y":
                                    members.remove(m)
                                    print("Data anggota berhasil dihapus!")
                                else:
                                    print("Penghapusan dibatalkan!")
                            break

                    if not ketemu:
                        print("Anggota tidak ditemukan!")

                elif peran != "Admin" and p == "2":
                    idm = input("Masukkan ID anggota: ")
                    ketemu = False

                    for m in members:
                        if str(m[0]) == idm:
                            print("Nama:", m[1])
                            print("Status:", m[4])
                            ketemu = True

                    if not ketemu:
                        print("Anggota tidak ditemukan!")

                elif (peran == "Admin" and p == "5") or (peran != "Admin" and p == "3"):
                    break
                else:
                    print("Menu tidak tersedia!")

                input("Tekan Enter untuk lanjut...")

    elif pilih == "2":
        nama = input("Username: ")
        pw = input("Password: ")
        ada = False

        for u in users:
            if u[0] == nama:
                ada = True

        if nama and pw and not ada:
            users.append([nama, pw, "Pengguna"])
            print("Register berhasil!")
        else:
            print("Username tidak valid atau sudah ada!")

    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Menu tidak tersedia!")

    input("Tekan Enter untuk lanjut...")