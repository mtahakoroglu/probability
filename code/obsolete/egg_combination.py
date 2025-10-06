import math

print("Kutuda 20 yumurta var.")
print("13 tanesi beyaz yumurta.")
print("7 tanesi kahverengi yumurta.")
print("Rasgele 4 yumurta seçersek 3 tanesinin kahverengi olma olasılığı nedir?")
x = math.comb(7,3)*math.comb(13,1) / math.comb(20,4)
print(f"Olasılık {x}. Yani %{x*100} ihtimal.")