import os
 
users = {"adam": {"password": "adam12", "peran": "Admin"}}
members = {}
PAKET = {"1": "1 Bulan", "2": "3 Bulan", "3": "6 Bulan"}

 
def buat_id():
    """Membuat ID anggota baru."""
    id_baru = max(members, default=0) + 1
    return id_baru
 
    
def input_paket():
    """Menampilkan pilihan paket dan mengembalikan nama paket."""
    print("1. Paket 1 Bulan")
    print("2. Paket 3 Bulan")
    print("3. Paket 6 Bulan")
    pilihan = input("Pilih paket: ")
    if pilihan not in PAKET:
        raise ValueError("Paket tidak tersedia!")
    return PAKET[pilihan]
 
 
def login():
    """Proses login. Mengembalikan peran, atau None jika gagal."""
    username = input("Username: ")
    pw = input("Password: ")
    try:
        if username not in users or users[username]["password"] != pw:
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        print("Login gagal!", e)
        return None
    else:
        print("Login berhasil!")
        return users[username]["peran"]
    finally:
        print("Proses login selesai.")
 
def validasi_hp(hp):
    """Memastikan nomor HP hanya berisi angka."""
    if not hp.isdigit():
        raise ValueError("Nomor HP harus berupa angka!")
    return hp
 
 
def ambil_id(teks_id):
    """Mengubah input ID menjadi int dan memastikan anggota ada."""
    try:
        ida = int(teks_id)
    except ValueError:
        raise ValueError("ID harus berupa angka!")
    if ida not in members:
        raise KeyError(ida)
    return ida
 
 
def hitung_aktif(daftar_id):
    """Menghitung jumlah anggota berstatus Aktif secara rekursif."""
    if not daftar_id:  # basis
        return 0
    aktif = 1 if members[daftar_id[0]]["status"] == "Aktif" else 0
    return aktif + hitung_aktif(daftar_id[1:])  # rekursi
 
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
 
 
def jeda():
    input("Tekan Enter untuk lanjut...")
 
 
def tampil_menu(peran):
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
 
 
def tampil_daftar():
    if not members:
        print("Belum ada data anggota.")
        return
    for ida, data in members.items():
        print("ID:", ida)
        print("Nama:", data["nama"])
        print("No HP:", data["hp"])
        print("Paket:", data["paket"])
        print("Status:", data["status"])
        print("-" * 20)
    total = len(members)
    aktif = hitung_aktif(list(members))
    print(f"Total anggota: {total} | Aktif: {aktif}")
 
 
def tambah_anggota():
    try:
        nama = input("Nama anggota: ").strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        hp = validasi_hp(input("Nomor HP: "))
        paket = input_paket()
    except ValueError as e:
        print("Data tidak valid!", e)
    else:
        ida = buat_id()
        members[ida] = {"nama": nama, "hp": hp, "paket": paket, "status": "Aktif"}
        print("Anggota berhasil ditambahkan!")
    finally:
        print("Proses tambah anggota selesai.")
 
 
def ubah_anggota():
    if not members:
        print("Belum ada data anggota.")
        return
    for ida, data in members.items():
        print("ID:", ida, "Nama:", data["nama"])
    try:
        ida = ambil_id(input("Masukkan ID anggota: "))
        print("1. Ubah nomor HP")
        print("2. Perbarui paket")
        ubah = input("Pilih perubahan: ")
        if ubah == "1":
            members[ida]["hp"] = validasi_hp(input("Nomor HP baru: "))
        elif ubah == "2":
            members[ida]["paket"] = input_paket()
            members[ida]["status"] = "Aktif"
        else:
            raise ValueError("Pilihan perubahan tidak valid!")
    except ValueError as e:
        print("Gagal mengubah data!", e)
    except KeyError:
        print("Anggota tidak ditemukan!")
    else:
        print("Data anggota berhasil diperbarui!")
 
 
def hapus_anggota():
    if not members:
        print("Belum ada data anggota.")
        return
    for ida, data in members.items():
        print("ID:", ida, "Nama:", data["nama"])
    try:
        ida = ambil_id(input("Masukkan ID anggota: "))
    except ValueError as e:
        print(e)
    except KeyError:
        print("Anggota tidak ditemukan!")
    else:
        if input("Hapus data? (y/n): ").lower() == "y":
            del members[ida]
            print("Data anggota berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan!")
 
 
def cek_status():
    try:
        ida = ambil_id(input("Masukkan ID anggota: "))
    except ValueError as e:
        print(e)
    except KeyError:
        print("Anggota tidak ditemukan!")
    else:
        print("Nama:", members[ida]["nama"])
        print("Status:", members[ida]["status"])
 
 
def register():
    try:
        username = input("Username: ").strip()
        pw = input("Password: ")
        if not username or not pw:
            raise ValueError("Username dan password tidak boleh kosong!")
        if username in users:
            raise ValueError("Username sudah digunakan!")
    except ValueError as e:
        print("Register gagal!", e)
    else:
        users[username] = {"password": pw, "peran": "Pengguna"}
        print("Register berhasil!")
 
 
def menu_utama_user(peran):
    """Perulangan menu setelah login (Admin / Pengguna)."""
    while True:
        bersihkan_layar()
        tampil_menu(peran)
        pilihan = input("Pilih: ")
 
        try:
            if peran == "Admin":
                if pilihan == "1":
                    tambah_anggota()
                elif pilihan == "2":
                    tampil_daftar()
                elif pilihan == "3":
                    ubah_anggota()
                elif pilihan == "4":
                    hapus_anggota()
                elif pilihan == "5":
                    break
                else:
                    raise ValueError("Menu tidak tersedia!")
            else:
                if pilihan == "1":
                    tampil_daftar()
                elif pilihan == "2":
                    cek_status()
                elif pilihan == "3":
                    break
                else:
                    raise ValueError("Menu tidak tersedia!")
        except ValueError as e:
            print(e)
 
        jeda()
 
 
def main():
    try:
        while True:
            bersihkan_layar()
            print("=== SISTEM PENDATAAN ANGGOTA GYM ===")
            print("1. Login")
            print("2. Register")
            print("3. Keluar")
            pilih = input("Pilih: ")
 
            if pilih == "1":
                peran = login()
                if peran is not None:
                    jeda()
                    menu_utama_user(peran)
                    continue
            elif pilih == "2":
                register()
            elif pilih == "3":
                print("Terima kasih!")
                break
            else:
                print("Menu tidak tersedia!")
 
            jeda()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan oleh pengguna.")
    finally:
        print("Program selesai.")
 
 
main()