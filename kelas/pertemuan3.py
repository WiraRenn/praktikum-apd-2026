# praktikum = "orsikom"

# if praktikum == "apd":
#     print("kamu lagi mengikuti praktikum apd sekarang")
#     else:
#         print("Kamu mengikuti praktikum lain")

# umur = int(input("Masukkan umur kalian :"))

# if umur > 17:
#     print("kamu sudah legal")
# else:
#     print("kamu belum cukup umur")

# Input jenis kendaraan dari user
# kendaraan = input("Masukkan jenis kendaraan anda: ").lower()
# # Misalnya, kendaraan = "mobil"

# # Percabangan
# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# umur = 20
# status = "Dewasa" if umur >= 18 else "Belum Dewasa"
# print(status)

total_pembelian = int(input("Masukkan total pembelian anda :"))
if total_pembelian > 200000:
    print("maka diskon 30%")
elif total_pembelian > 100000:
    print("tidak mendapat diskon")
elif total_pembelian <= 100000:
    print("tidak mendapat diskon")
else:
    print("diskon tidak dapat diakumulasikan")