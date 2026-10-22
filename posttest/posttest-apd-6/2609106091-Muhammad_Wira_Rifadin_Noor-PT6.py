import os
from datetime import datetime

users = [
    {"username": "Wiraa", "password": "100508", "role": "admin"},
    {"username": "Ren", "password": "9009", "role": "user"},
]
data_wifi = [
    {"ip": "192.168.1.1", "nama": "Kantor DISKOMINFO", "lokasi": "lantai 1", "pj": "Reoo", "status": "Aktif", "masalah": "-", "terakhir": "14-10-2026 09.00", "keterangan": "Router utama"},
    {"ip": "192.168.1.2", "nama": "Kantor BPJS", "lokasi": "Ruang Staff L2", "pj": "Nishi", "status": "Bermasalah", "masalah": "Sinyal putus-putus", "terakhir": "14-10-2026 11:05", "keterangan": "Untuk staff"},
    {"ip": "192.168.1.3", "nama": "Kantor Pariwisata", "lokasi": "Ruang Rapat utama", "pj": "Elio", "status": "Tidak Aktif", "masalah": "-", "terakhir": "13-10-2026 15:00", "keterangan": "Dinonaktifkan sementara"},
]
program_jalan = True

while program_jalan:
    os.system("cls" if os.name == "nt" else "clear")
    print(".")
    print("SYSTEM PENGECEKAN JARINGAN WIFI INSTANSI/KANTOR")
    print(".")
    print("1. Login")
    print("2. Register (User)")
    print("3. Log out")
    print(".")
    pilihan_awal = input("Pilih Menu (1-3) : ").strip()

    if pilihan_awal == "1":
        percobaan = 0
        user_login = None

        while percobaan < 3 and user_login is None:
            os.system("cls" if os.name == "nt" else "clear")
            print(".")
            print("Login")
            print(".")
            username = input("Username : ").strip()
            password = input("Password : ").strip()

            for u in users:
                if u["username"] == username and u["password"] == password:
                    user_login = u

            if user_login is None:
                percobaan += 1
                print("\n Username atau Password salah! Sisa percobaan : ", 3 - percobaan)
                input("Tekan Enter untuk melanjutkan ---")

        if user_login is None:
            print("\n Gagal login 3 kali. Kembali ke menu awal!")
            input("Tekan Enter untuk melanjutkan ---")
        else:
            nama_user = user_login["username"]
            role = user_login["role"]
            sesi = True

            while sesi:
                os.system("cls" if os.name == "nt" else "clear")
                print(".")
                print("Menu Utama -", nama_user, "(" + role.upper() + ")")
                print(".")
                print("1. Daftar Wifi")
                print("2. Cari Wifi")
                print("3. Cek Koneksi Wifi")
                if role == "admin":
                    print("4. Tambah Data Wifi")
                    print("5. Ubah Data Wifi")
                    print("6. Hapus Data Wifi")
                print("0. Log out")
                print(".")
                pilih = input("Pilih menu :").strip()

                if pilih == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("DAFTAR JARINGAN WIFI")
                    print(".")

                    if len(data_wifi) == 0:
                        print("Belum ada data Wifi!")
                    else:
                        print(f"{'No':<4}{'IP Address':<16}{'Nama Wifi':<16}{'Lokasi':<20}{'Penanggung Jawab':<18}{'Status':<13}{'Cek Terakhir':<17}")
                        print(".")
                        no = 1
                        jml_aktif = 0
                        jml_masalah = 0
                        jml_nonaktif = 0
                        jml_belum = 0
                        for w in data_wifi:
                            print(f"{no:<4}{w["ip"]:<16}{w["nama"]:<16}{w["lokasi"]:<20}{w["pj"]:<18}{w["status"]:<13}{w["terakhir"]:<17}")
                            if w["masalah"] != "-":
                                print("-> Masalah : ", w["masalah"])
                            if w["keterangan"] != "-":
                                print("-> Keterangan : ", w["keterangan"])
                            if w["status"] == "Aktif":
                                jml_aktif += 1
                            elif w["status"] == "Bermasalah":
                                jml_masalah += 1
                            elif w["status"] == "Tidak Aktif":
                                jml_nonaktif += 1
                            else:
                                jml_belum += 1
                            no += 1
                        print(".")
                        print("Total:", len(data_wifi), "| Aktif :", jml_aktif, "| Bermasalah : ", jml_masalah,"| Tidak Aktif : ", jml_nonaktif, "| Belum dicek : ", jml_belum)
                    input("\n Tekan Enter untuk kembali ---")

                elif pilih == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("CARI WIFI")
                    print(".")
                    kata = input("Cari (IP / Nama / Lokasi / Penanggung jawab) : ").strip().lower()

                    if kata == "":
                        print("\n[!] Kata kunci tidak boleh kosong!")
                    else:
                        ketemu = 0
                        print()
                        for w in data_wifi:
                            if kata in w["ip"].lower() or kata in w["nama"].lower() or kata in w["lokasi"].lower() or kata in w["pj"].lower():
                                ketemu += 1
                                print("IP Address :", w["ip"])
                                print("Nama WiFi        :", w["nama"])
                                print("Lokasi           :", w["lokasi"])
                                print("Penanggung Jawab :", w["pj"])
                                print("Status           :", w["status"])
                                print("Masalah          :", w["masalah"])
                                print("Cek Terakhir     :", w["terakhir"])
                                print("Keterangan       :", w["keterangan"])
                                print(".")
                        if ketemu == 0:
                            print("Data Tidak ditemukan!")
                    input("\n Tekan Enter untuk kembali ---")

                elif pilih == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("CEK KONEKSI WIFI")
                    print(".")

                    if len(data_wifi) == 0:
                        print("Belum ada data wifi!")
                    else:
                        for w in data_wifi:
                            print(f"  {w["ip"]:<16}{w["nama"]:<16}{w["status"]}")
                        print(".")
                        target = input("Masukkan IP yang dicek (atau ketik 'semua') : ").strip()

                        daftar_cek = []
                        if target.lower() == "semua":
                            daftar_cek = data_wifi
                        else:
                            for w in data_wifi:
                                if w["ip"] == target:
                                    daftar_cek.append(w)

                        if len(daftar_cek) == 0:
                            print("\n IP tidak ditemukan!")
                        else:
                            print()
                            for w in daftar_cek:
                                if w["status"] == "Tidak Aktif":
                                    print(f"{w["ip"]:<16}{w["nama"]:<16}-> dilewati (berstatus Tidak Aktif)")
                                else:
                                    print(f"Mengecek {w["ip"]} ({w["nama"]}) ...", end=" ")
                                    if os.name == "nt":
                                        hasil = os.system("ping -n 1 -w 1000 " + w["ip"] + " > nul")
                                    else:
                                        hasil = os.system("ping -c 1 -W 1 " + w["ip"] + " > /dev/null 2>&1")

                                    if hasil == 0:
                                        w["status"] = "Aktif"
                                        w["masalah"] = "-"
                                        print(" AKTIF")
                                    else:
                                        w["status"] = " Bermasalah"
                                        w["masalah"] = " Tidak merespons ping"
                                        print(" BERMASALAH (tidak merespons)")
                                    w["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")
                    input("\n Tekan Enter untuk kembali ---")

                elif pilih == "4" and role == "admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("TAMBAH DATA WIFI")
                    print(".")

                    ip_baru = input("IP Address (Contoh  : 192.168.1.10) : ").strip()

                    bagian = ip_baru.split(".")
                    ip_valid = len(bagian) == 4
                    for b in bagian:
                        if not b.isdecimal() or len(b) > 3 or int(b) > 255:
                            ip_valid = False

                    if not ip_valid:
                        print("\n Format IP tidak valid! (harus 4 angka 0-255 dipisah titik)")
                        input("Tekan Enter untuk kembali ---")
                        continue

                    duplikat = False
                    for w in data_wifi:
                        if w["ip"] == ip_baru:
                            duplikat = True
                    if duplikat:
                        print("\n IP sudah terdaftar! Setiap Wifi harus punya IP unik.")
                        input("Tekan Enter untuk kembali ---")
                        continue

                    nama_baru = input("Nama WiFi                 : ").strip()
                    lokasi_baru = input("Lokasi perangkat           : ").strip()
                    pj_baru = input("Nama penanggung jawab      : ").strip()
                    ket_baru = input("Keterangan (boleh kosong)  : ").strip()

                    if nama_baru == "" or lokasi_baru == "" or pj_baru == "":
                        print("\n Nama Wifi, lokasi, dan penanggung jawab tidak boleh kosong!")
                    else:
                        if ket_baru == "":
                            ket_baru = "-"
                        data_wifi.append({
                            "ip": ip_baru,
                            "nama": nama_baru,
                            "lokasi": lokasi_baru,
                            "pj": pj_baru,
                            "status": "Belum dicek",
                            "masalah": "-",
                            "terakhir": "-",
                            "keterangan": ket_baru
                        })
                        print("\n Data Wifi berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali ---")

                elif pilih == "5" and role == "admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("UBAH DATA WIFI")
                    print(".")

                    if len(data_wifi) == 0:
                        print("Belum ada data Wifi.")
                        input("\n Tekan Enter untuk kembali ---")
                        continue

                    for w in data_wifi:
                        print(f"  {w["ip"]:<16}{w["nama"]:<16}{w["lokasi"]}")
                    print(".")
                    ip_cari = input("Masukkan IP Wifi yang akan diubah : ").strip()

                    target_wifi = None
                    for w in data_wifi:
                        if w["ip"] == ip_cari:
                            target_wifi = w

                    if target_wifi is None:
                        print("\n IP tidak ditemukan.")
                        input("Tekan Enter untuk kembali ---")
                        continue

                    mengubah = True
                    while mengubah:
                        os.system("cls" if os.name == "nt" else "clear")
                        print(".")
                        print("UBAH DATA : ", target_wifi["nama"], "-", target_wifi["ip"])
                        print(".")
                        print("IP Address       :", target_wifi["ip"])
                        print("Nama WiFi        :", target_wifi["nama"])
                        print("Lokasi           :", target_wifi["lokasi"])
                        print("Penanggung Jawab :", target_wifi["pj"])
                        print("Status           :", target_wifi["status"])
                        print("Masalah          :", target_wifi["masalah"])
                        print("Keterangan       :", target_wifi["keterangan"])
                        print(".")
                        print("1. Ubah Nama WiFi")
                        print("2. Ganti Lokasi Perangkat")
                        print("3. Ubah Penanggung Jawab")
                        print("4. Ubah Keterangan")
                        print("5. Ubah IP Address")
                        print("6. Ubah Status / Masalah (manual)")
                        print("0. Selesai")
                        print(".")
                        sub = input("Pilih yang diubah : ").strip()

                        if sub == "1":
                            isi = input("Nama Wifi baru : ").strip()
                            if isi == "":
                                print("Tidak boleh kosong!")
                            else:
                                target_wifi["nama"] = isi
                                print("Nama Wifi diperbarui.")
                            input("Tekan Enter ---")

                        elif sub == "2":
                            isi = input("Lokasi baru : ").strip()
                            if isi == "":
                                print("Tidak boleh kosong!")
                            else:
                                target_wifi["lokasi"] = isi
                                print("Lokasi diperbarui.")
                            input("Tekan Enter ---")

                        elif sub == "3":
                            isi = input("Penanggung jawab baru : ").strip()
                            if isi == "":
                                print("Tidak boleh kosong!")
                            else:
                                target_wifi["pj"] = isi
                                print("Penanggung jawab diperbarui.")
                            input("Tekan Enter ---")

                        elif sub == "4":
                            isi = input("Keterangan baru (kosongkan untuk '-'): ").strip()
                            if isi == "":
                                isi = "-"
                            target_wifi["keterangan"] = isi
                            print("[+] Keterangan diperbarui.")
                            input("Tekan Enter...")

                        elif sub == "5":
                            ip_ganti = input("IP baru : ").strip()
                            bagian = ip_ganti.split(".")
                            ip_valid = len(bagian) == 4
                            for b in bagian:
                                if not b.isdecimal() or len(b) > 3 or int(b) > 255:
                                    ip_valid = False

                            duplikat = False
                            for w in data_wifi:
                                if w["ip"] == ip_ganti and w is not target_wifi:
                                    duplikat = True

                                if not ip_valid:
                                    print("Format IP tidak valid!")
                                elif duplikat:
                                    print("IP sudah dipakai Wifi lain!")
                                else:
                                    target_wifi["ip"] = ip_ganti
                                    print("IP Address diperbarui.")
                                input("Tekan Enter ---")

                        elif sub == "6":
                            print("\n1. Aktif")
                            print("2. Bermasalah")
                            print("3. Tidak Aktif")
                            st = input("Pilih status baru [1-3]: ").strip()
                            if st == "1":
                                target_wifi["status"] = "Aktif"
                                target_wifi["masalah"] = "-"
                                target_wifi["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")
                                print("Status diubah menjadi Aktif.")
                            elif st == "2":
                                masalah = input("Deskripsi masalah: ").strip()
                                if masalah == "":
                                    masalah = "Tidak dijelaskan"
                                target_wifi["status"] = "Bermasalah"
                                target_wifi["masalah"] = masalah
                                target_wifi["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")
                                print("Status diubah menjadi Bermasalah.")
                            elif st == "3":
                                target_wifi["status"] = "Tidak Aktif"
                                target_wifi["masalah"] = "-"
                                target_wifi["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")
                                print("Status diubah menjadi Tidak Aktif.")
                            else:
                                print("Pilihan tidak valid!")
                            input("Tekan Enter...")

                        elif sub == "0":
                            mengubah = False

                        else:
                            print("Pilihan tidak valid!")
                            input("Tekan Enter")

                elif pilih == "6" and role == "admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(".")
                    print("HAPUS DATA WIFI")
                    print(".")

                    if len(data_wifi) == 0:
                        print("Belum ada data Wifi.")
                        input("\n Tekan Enter untuk kembali ---")
                        continue

                    for w in data_wifi:
                        print(f"{w["ip"]:<16}{w["nama"]:<16}{w["status"]}")
                    print(".")
                    ip_hapus = input("Masukkan IP Wifi yang akan di hapus : ").strip()

                    target_wifi = None
                    for w in data_wifi:
                        if w["ip"] == ip_hapus:
                            target_wifi = w

                    if target_wifi is None:
                        print("\n IP tidak ditemukan.")
                    else:
                        print("\n Nama Wifi : ", target_wifi["nama"])
                        print("Lokasi : ", target_wifi["lokasi"])
                        print("Status : ", target_wifi["status"])
                        if target_wifi["status"] == "Aktif":
                            print("\n PERINGATAN : Wifi ini masih berstatus AKTIF!")
                        yakin = input("\n Yakin ingin menghapus? (ya/tidak) : ").strip().lower()
                        if yakin == "ya":
                            data_wifi.remove(target_wifi)
                            print("Data Wifi berhasil dihapus!")
                        else:
                            print("Penghapusan dibatalkan.")
                    input("\n Tekan Enter untuk kembali ---")

                elif pilih == "0":
                    sesi = False

                else:
                    print("\n Pilihan tidak valid!")
                    input("Tekan Enter untuk melanjutkan ---")

    elif pilihan_awal == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print(".")
        print("REGISTER PENGGUNA BARU")
        print(".")

        user_baru = input("Username (min. 3 karakter, tanpa spasi): ").strip()
        ada = False
        for u in users:
            if u["username"].lower() == user_baru.lower():
                ada = True

        if len(user_baru) < 3 or " " in user_baru:
            print("\n Username minimal 3 karakter dan tidak boleh mengandung spasi!")
        elif ada:
            print("\n Username sudah digunakan!")
        else:
            pass_baru = input("Password (min. 6 karakter)              : ").strip()
            pass_ulang = input("Ulangi password                          : ").strip()

            if len(pass_baru) < 6:
                print("\n Password minimal 6 karakter!")
            elif pass_baru != pass_ulang:
                print("\n Konfirmasi password tidak sama!")
            else:
                users.append({
                    "username": user_baru,
                    "password": pass_baru,
                    "role": "user"
                })
                print("\n Registrasi berhasil! Silahkan login sebagai Pengguna biasa.")
        input("Tekan Enter untuk melanjutkan ---")

    elif pilihan_awal == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        program_jalan = False
    else:
        print("\n Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan ---")