pengguna_true = "Wiraa"
password_true = "091"
uang_bulanan = 3000000
total_pengeluaran = 0
print("===========================")
print("-----------Login-----------")
print("===========================")
login_berhasil = False

for l in range(1,4):
    pengguna = input("Masukkan nama pengguna : ")
    password = input("Masukkan kata sandi : ")
    print("===========================")
    if pengguna == pengguna_true and password == password_true:
        login_berhasil = True
        break
    else:
        sisa_login = 3 - l
        if sisa_login > 0:
            print(f"Login gagal! nama pengguna atau password anda salah! anda memiliki {sisa_login}x lagi")
        else:
            print("Anda telah gagal login sebanyak 3 kali! Akun anda telah diblkir.")

if login_berhasil:
    print("Login berhasil!")
    status = True
    while status:
        print("===========================")
        print("   Menu Pilihan :   ")
        print("---------------------------")
        print("1. Catat Pengeluaran")
        print("2. Cek sisa uang saku")
        print("3. Keluar")
        print("---------------------------")
        pilihan = input("Silahkan pilih menu (1-3) : ")

        if pilihan == "1":
            status_pilihan = True
            while status_pilihan:
                print("---------------------------")
                pengeluaran = float(input("Masukan jumlah pengeluaran anda : "))
                total_pengeluaran += pengeluaran
                print("                  Catatan Pengeluaran")
                print("pengeluaran anda sebesar : Rp.", pengeluaran, "telah ditambahkan!")
                print("Total pengeluaran anda saat ini : Rp.", total_pengeluaran)
                print("-----------------------------------------------------------------")

                while True:
                    pilihan2 = input("Ingin mencatat pengeluaran lagi? (ya/skip) : ").lower()
                    if pilihan2 == "ya":
                        break
                    elif pilihan2 == "skip":
                        status_pilihan = False
                        break
                    else:
                        print("Pilihan tidak valid! Silahkan pilih ya/skip")
        elif pilihan == "2":
                uang_saku = uang_bulanan - total_pengeluaran
                print("Sisa uang saku anda saat ini : Rp.", uang_saku)

        elif pilihan == "3":
            print("===================================================")
            print("Terima kasih telah menggunakan pencatatan keuangan!")
            print("===================================================")
            status = False
        else:
            print("!!!!!!!!!!!!!!!!!!!!")
            print("Pilihan tidak valid!")
            print("!!!!!!!!!!!!!!!!!!!!")