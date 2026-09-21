skincare_1 = int(35000)
skincare_2 = int(42000)
skincare_3 = int(50000)
skincare_4 = int(55000)
skincare_5 = int(68000)
skincare_6 = int(70000)

total = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6
total_pajak = total + int(12000)
rata_rata = total_pajak / 6

nim = int(70)
bolean = nim < rata_rata

print ("Total harga skincare RP: ", total)
print ("Total harga yang harus dibayar setelah pajak RP: ", total_pajak)

print ("Nilai bolean: ", bolean)