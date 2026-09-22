merchandise_1 =45000
merchandise_2 =50000
merchandise_3 =60000
merchandise_4 =75000
merchandise_5 =90000
merchandise_6 =120000
bungkus_kado = 7500
harga_merchandise = [merchandise_1,merchandise_2,merchandise_3,merchandise_4,merchandise_5,merchandise_6]
total_harga_merchandise = (harga_merchandise[0] + harga_merchandise[1] + harga_merchandise[2] + harga_merchandise[3] + harga_merchandise[4] + harga_merchandise[5])
total_harga = total_harga_merchandise + bungkus_kado
kurs_usd = 17810
total_usd = total_harga / kurs_usd

rata_rata = total_harga / len(harga_merchandise)

nim = 91
bolean = nim > rata_rata

slice_merchandise = harga_merchandise[-5:-2]

print("Harga Merchandise :", harga_merchandise)
print("Total Harga :", total_harga)
print("Rata-rata :", rata_rata)
print("Total dalam USD : $", total_usd)
print("NIM :", nim)
print("Bolean :", bolean)
print("Merchandise 2 hingga Merchandise 4 :", slice_merchandise)