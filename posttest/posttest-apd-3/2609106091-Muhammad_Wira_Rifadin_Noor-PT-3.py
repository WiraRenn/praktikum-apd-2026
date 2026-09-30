nama = input("Masukkan nama panggilan anda : ")
nim = input("Masukkan NIM anda : ")
status_pesan = True

if nama == "WiraRen" and nim == "91":
    PS4 = 10000
    PS4PRO = 15000
    PS5 = 20000

    print("=========================")
    print("1. PS4 = Rp 10.000/jam")
    print("2. PS4PRO = Rp 15.000/jam")
    print("3. PS5 = Rp 20.000/jam")
    print("=========================")

    ps = int(input("pilih lah dalam angka : "))
    if ps == 1:
        jam_sewa = int(input("Masukan jam sewa: "))
        total_harga = PS4 * jam_sewa
        jenis_ps = "PS4"
    elif ps == 2:
        jam_sewa = int(input("Masukan jam sewa: "))
        total_harga = PS4PRO * jam_sewa
        jenis_ps = "PS4PRO"
    elif ps == 3:
        jam_sewa = int(input("Masukan jam sewa: "))
        total_harga = PS5 * jam_sewa
        jenis_ps = "PS5"
    else:
        print("Pilihan tidak tersedia")

    if status_pesan == True:
        if jam_sewa >= 5:
            diskon_durasi = 0.08 * total_harga
        elif jam_sewa >= 3:
            diskon_durasi = 0.05 * total_harga
        else:
            diskon_durasi = 0
        hari_sewa = input("Masukan hari sewa (weekday/weekend): ")
        print("=========================================")
        if hari_sewa == "weekend":
            biaya_tambahan = 0.10 * total_harga
        else:
            biaya_tambahan = 0
        
        total_bayar = total_harga - diskon_durasi + biaya_tambahan

        print("========================================")
        print("Nama : ", nama)
        print("NIM : ", nim)
        print("Jenis PS yang disewa : ", jenis_ps)
        print("Jumlah jam sewa : ", jam_sewa, "jam")
        print("Total harga : Rp", int(total_harga))
        print("Diskon durasi : Rp", int(diskon_durasi))
        print("Biaya tambahan : Rp", int(biaya_tambahan))
        print("Total bayar : Rp", int(total_bayar))
        print("=========================================")
    else:
            print("Pilihan tidak tersedia!")
else:
    print("Nama panggilan atau NIM anda salah!")