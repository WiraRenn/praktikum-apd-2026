import os
import ipaddress
import subprocess
from datetime import datetime

users = [
    {"username": "Wiraa", "password": "100508", "role": "admin"},
    {"username": "Ren", "password": "9009", "role": "user"},
]

data_wifi = [
    {"ip": "192.168.1.1", "nama": "Kantor DISKOMINFO", "lokasi": "Lantai 1",
     "pj": "Reoo", "status": "Aktif", "masalah": "-",
     "terakhir": "14-10-2026 09:00", "keterangan": "Router utama"},
    {"ip": "192.168.1.2", "nama": "Kantor BPJS", "lokasi": "Ruang Staff L2",
     "pj": "Nishi", "status": "Bermasalah", "masalah": "Sinyal putus-putus",
     "terakhir": "14-10-2026 11:05", "keterangan": "Untuk staff"},
    {"ip": "192.168.1.3", "nama": "Kantor Pariwisata", "lokasi": "Ruang Rapat utama",
     "pj": "Elio", "status": "Tidak Aktif", "masalah": "-",
     "terakhir": "13-10-2026 15:00", "keterangan": "Dinonaktifkan sementara"},
]
program_jalan = True

def cari_wifi(kata_kunci):
    "Mengembalikan daftar Wifi yang cocok dengan IP, Nama, Lokasi, Atau PJ!"
    kata_kunci = kata_kunci.strip().lower()
    if not kata_kunci:
        raise ValueError("Kata kunci pencarian tidak boleh kosong!")

    hasil_pencarian = []
    for wifi in data_wifi:
        if any(kata_kunci in wifi[kunci].lower()
                for kunci in ("ip", "nama", "lokasi", "pj")):
            hasil_pencarian.append(wifi)
    return hasil_pencarian

def validasi_ip(ip):
    "Memeriksa format IP dan memastikan IP belum digunakan..."
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        raise ValueError("Format IP tidak valis! Masukkan IP yang benar!")

    for wifi in data_wifi:
        if wifi["ip"] == ip:
            raise ValueError("IP sudah terdaftar!")
    return True

def tampilkan_daftar_wifi():
    "Menampilkan seluruh data Wifi..."
    print("\n---DAFTAR JARINGAN WIFI---")
    if not data_wifi:
        print("Belum ada data Wifi!")
        return

    print(f"{'No':<4}{'IP Address':<16}{'Nama Wifi':<24}{'Lokasi':<22}"
          f"{'Penanggung Jawab':<20}{'Status':<16}{'Cek Terakhir':<18}")
    jumlah_aktif = jumlah_masalah = jumlah_nonaktif = jumlah_belum = 0

    for nomor, wifi in enumerate(data_wifi, start=1):
        print(f"{nomor:<4}{wifi['ip']:<16}{wifi['nama']:<24}"
              f"{wifi['lokasi']:<22}{wifi['pj']:<20}"
              f"{wifi['status']:<16}{wifi['terakhir']:<18}")
        if wifi["masalah"] != "-":
            print("   Masalah:", wifi["masalah"])
        if wifi["keterangan"] != "-":
            print("   Keterangan:", wifi["keterangan"])

        if wifi["status"] == "Aktif":
            jumlah_aktif += 1
        elif wifi["status"] == "Bermasalah":
            jumlah_masalah += 1
        elif wifi["status"] == "Tidak Aktif":
            jumlah_nonaktif += 1
        else:
            jumlah_belum += 1

    print(f"\nTotal: {len(data_wifi)} | Aktif: {jumlah_aktif} | "
          f"Bermasalah: {jumlah_masalah} | Tidak Aktif: {jumlah_nonaktif} | "
          f"Belum dicek: {jumlah_belum}")

def bersihkan_layar():
    "Membersihkan Terminal..."
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    "Menahan tampilan sampai menekan Enter..."
    input("\nTekan Enter untuk melanjutkan...")

def tampilkan_detail(wifi):
    "Menampilkan detail satu data Wifi."
    print("\nIP Address       :", wifi["ip"])
    print("Nama Wifi        :", wifi["nama"])
    print("Lokasi           :", wifi["lokasi"])
    print("Penanggung Jawab :", wifi["pj"])
    print("Status           :", wifi["status"])
    print("Masalah          :", wifi["masalah"])
    print("Cek Terakhir     :", wifi["terakhir"])
    print("Keterangan       :", wifi["keterangan"])

def login():
    percobaan = 0
    user_login = None

    while percobaan < 3 and user_login is None:
        print("\nLOGIN")
        username_input = input("Username : ").strip()
        password_input = input("Password : ").strip()

        for akun in users:
            if akun ["username"] == username_input and akun ["password"] == password_input:
                user_login = akun
                break

        if user_login is None:
            percobaan += 1
            print(f"Username atau Password salah! Sisa percobaan : {3 - percobaan}")

    if user_login is None:
        print("Gagal Login 3 kali!")
        jeda()
        return
    
    menu_pengguna(user_login)

def menu_pengguna(akun):
    nama_user = akun["username"]
    role = akun["role"]
    sesi = True

    while sesi:
        print(f"\nMENU UTAMA - {nama_user} ({role.upper()})")
        print(" ")
        print("1. Daftar Wifi")
        print("2. Cari Wifi")
        print("3. Cek koneksi Wifi")
        if role == "admin":
            print("4. Tambah data Wifi")
            print("5. Ubah data Wifi")
            print("6. Hapus data Wifi")
        print("0. Log out")
        print(" ")

        pilihan = input("Pilih Menu : ").strip()
        try:
            if pilihan == "1":
                tampilkan_daftar_wifi()
                jeda()
            elif pilihan == "2":
                kata_kunci = input("Cari dengan IP/Nama/Lokasi/PJ : ")
                hasil = cari_wifi(kata_kunci)
                if not hasil:
                    print("Data Wifi tidak ditemukan.")
                for wifi in hasil:
                    tampilkan_detail(wifi)
                jeda()
            elif pilihan == "3":
                cek_koneksi()
                jeda()
            elif pilihan == "4" and role == "admin":
                tambah_wifi()
                jeda()
            elif pilihan == "5" and role == "admin":
                ubah_wifi()
                jeda()
            elif pilihan == "6" and role == "admin":
                hapus_wifi()
                jeda()
            elif pilihan== "0":
                print("Berhasil Log Out.")
                sesi = False
            else:
                print("Pilihan tidak valid atau menu khusus admin!")
                jeda()
        except (ValueError,KeyError,OSError, subprocess.SubprocessError) as error:
            print(f"Terjadi Kesalahan : {error}")
            jeda()

def tambah_wifi():
    ip_baru = input("IP Address : ").strip()
    validasi_ip(ip_baru)
    nama_baru = input("Nama Wifi : ").strip()
    lokasi_baru = input("Lokasi Perangkat : ").strip()
    pj_baru = input("Penanggung Jawab : ").strip()
    keterangan_baru = input("Keteerangan (boleh kosong) : ").strip()

    if not nama_baru or not lokasi_baru or not pj_baru:
        raise ValueError("Nama Wifi, Lokasi dan Penanggung jawab tidak boleh kosong!")

    data_wifi.append({
        "ip": ip_baru,
        "nama": nama_baru,
        "lokasi": lokasi_baru,
        "pj": pj_baru,
        "status": "Belum Di cek",
        "masalah": "-",
        "terakhir": "-",
        "keterangan": keterangan_baru or "-"
    })
    print("Data Wifi berhasil ditambahkan.")

def ubah_wifi():
    ip_cari = input("Masukkan IP Wifi yang akan di ubah : ").strip()
    target_wifi = next((wifi for wifi in data_wifi if wifi["ip"] == ip_cari), None)
    if target_wifi is None:
        raise ValueError("IP tidak ditemukan!")

    print("1. Nama Wifi\n2. Lokasi\n3. Penanggung jawab\n4. Keterangan\n5. Status")
    pilihan_ubah = input("Pilih data yang diubah: ").strip()

    if pilihan_ubah in ("1", "2", "3", "4"):
        kolom = {"1": "nama", "2": "lokasi", "3": "pj", "4": "keterangan"}[pilihan_ubah]
        nilai_baru = input("Masukkan nilai baru: ").strip()
        if pilihan_ubah != "4" and not nilai_baru:
            raise ValueError("Data tidak boleh kosong.")
        target_wifi[kolom] = nilai_baru or "-"
    elif pilihan_ubah == "5":
        print("1. Aktif\n2. Bermasalah\n3. Tidak Aktif")
        status_pilihan = input("Pilih status: ").strip()
        status_map = {"1": "Aktif", "2": "Bermasalah", "3": "Tidak Aktif"}
        if status_pilihan not in status_map:
            raise ValueError("Pilihan status tidak valid.")
        target_wifi["status"] = status_map[status_pilihan]
        target_wifi["masalah"] = input("Keterangan masalah (isi - jika tidak ada): ").strip() or "-"
        target_wifi["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")
    else:
        raise ValueError("Pilihan perubahan tidak valid.")
    print("Data Wifi berhasil diperbarui.")

def hapus_wifi():
    ip_hapus = input("Masukkan IP Wifi yang akan dihapus : ").strip()
    target_wifi = next((wifi for wifi in data_wifi if wifi["ip"] == ip_hapus), None)
    if target_wifi is None:
        raise ValueError("IP tidak ditemukan!")

    print("Data yang dipilih:", target_wifi["nama"], "-", target_wifi["status"])
    konfirmasi = input("Yakin ingin menghapus? (ya/tidak): ").strip().lower()
    if konfirmasi == "ya":
        data_wifi.remove(target_wifi)
        print("Data Wifi berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def cek_koneksi():
    if not data_wifi:
        print("Belum ada data Wifi.")
        return

    for nomor, wifi in enumerate(data_wifi, start=1):
        print(f"{nomor}. {wifi['ip']} - {wifi['nama']} ({wifi['status']})")
    target = input("Masukkan IP yang dicek atau ketik 'semua': ").strip().lower()

    if target == "semua":
        daftar_cek = data_wifi
    else:
        daftar_cek = [wifi for wifi in data_wifi if wifi["ip"] == target]

    if not daftar_cek:
        raise ValueError("IP tidak ditemukan.")

    for wifi in daftar_cek:
        if wifi["status"] == "Tidak Aktif":
            print(wifi["ip"], "dilewati karena berstatus Tidak Aktif.")
            continue

        print(f"Mengecek {wifi['ip']} ({wifi['nama']})...")
        try:
            hasil = subprocess.run(
                ["ping", "-n" if os.name == "nt" else "-c", "1",
                 "-w" if os.name == "nt" else "-W", "1000" if os.name == "nt" else "1",
                 wifi["ip"]],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=3,
                check=False
            )
            if hasil.returncode == 0:
                wifi["status"] = "Aktif"
                wifi["masalah"] = "-"
                print("AKTIF")
            else:
                wifi["status"] = "Bermasalah"
                wifi["masalah"] = "Tidak merespons ping"
                print("BERMASALAH (tidak merespons)")
        except (subprocess.TimeoutExpired, OSError) as error:
            wifi["status"] = "Bermasalah"
            wifi["masalah"] = "Pengecekan gagal"
            print("Pengecekan gagal:", error)
        wifi["terakhir"] = datetime.now().strftime("%d-%m-%Y %H:%M")


def register():
    username_baru = input("Username (minimal 3 karakter, tanpa spasi): ").strip()
    if len(username_baru) < 3 or " " in username_baru:
        raise ValueError("Username minimal 3 karakter dan tidak boleh mengandung spasi.")

    if any(akun["username"].lower() == username_baru.lower() for akun in users):
        raise ValueError("Username sudah digunakan.")

    password_baru = input("Password (minimal 6 karakter): ").strip()
    konfirmasi_password = input("Ulangi password: ").strip()
    if len(password_baru) < 6:
        raise ValueError("Password minimal 6 karakter.")
    if password_baru != konfirmasi_password:
        raise ValueError("Konfirmasi password tidak sama.")

    users.append({"username": username_baru, "password": password_baru, "role": "user"})
    print("Registrasi berhasil. Silakan login sebagai pengguna biasa.")


def main():
    global program_jalan
    while program_jalan:
        print("\nSYSTEM PENGECEKAN JARINGAN WIFI INSTANSI/KANTOR")
        print("1. Login\n2. Register (User)\n3. Keluar")
        pilihan_awal = input("Pilih menu (1-3) : ").strip()

        try:
            if pilihan_awal == "1":
                login()
            elif pilihan_awal == "2":
                register()
                jeda()
            elif pilihan_awal == "3":
                print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                program_jalan = False
            else:
                raise ValueError("Pilihan menu harus 1, 2, atau 3.")
        except (ValueError, KeyError, OSError) as error:
            print(f"[ERROR] {error}")
            jeda()
        finally:
            pass

main()
print("Program Selesai.")