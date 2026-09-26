nama = "Adam"
nim = int("70")

print("SISTEM PENENTUAN RANK GAME BERDASARKAN POIN")

username = input("Masukkan nama pemain: ")
pasword = int(input("Masukkan pasword pemain: "))

if username == nama and pasword == nim:
    print("login berhasil")

    total_poin = int(input("Masukkan total poin pemain: "))

    if total_poin < 0:
        print("Poin tidak boleh kurang dari 0")
    elif total_poin < 100:
        rank = "Rokie"
        sisa = 100 - total_poin

    elif total_poin < 300:
        rank = "Warrior "
        sisa = 300 - total_poin

    elif total_poin < 1000:
        rank = "Master"
        sisa = 1000 - total_poin

    elif total_poin < 5000:
        rank = "Grand Master"
        sisa = 5000 - total_poin

    else:
        rank = "Legend"
          
    if total_poin >= 0:
        print("username: ", username)
        print("rank: ", rank)
    

    if rank == "Legend":
        print("Selamat! kamu telah mencapai rank tertinggi.")
    else:
        print("sisa poin:", sisa)

else:  
    print("login gagal")