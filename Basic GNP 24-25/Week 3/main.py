# Power Function 

def fungsi_pangkat(angka):
    return (angka ** 2)

print(f"Hasil dari pangkat 2 adalah {fungsi_pangkat(5)}")

# Lambda Function

fungsi_kuadrat = lambda angka:angka ** 2
print(f"Hasil kuadrat menggunakan lambda adalah {fungsi_kuadrat(5)}")

fungsi_kuadrat = lambda num,pow : num**pow
print(f"Hasil kuadrat menggunakan lamba 2 input adalah {fungsi_kuadrat(2,3)}")

# Sort Function

list_anak = ["Ucup", "Otong", "Dudung"]
def panjang_nama(nama):
    return len(nama)

print(f"Sorted list by function: {list_anak}")

# Lambda Sort Function

list_anak = ["Ucup", "Otong", "Dudung"]
list_anak.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda: {list_anak}")

# Filter angka < 5

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

def kurang_dari_lima(angka):
    return angka < 5

angka_baru = list(filter(kurang_dari_lima,kumpulan_angka))
print(angka_baru)

# Filter dengan lambda

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

angka_baru = list(filter(lambda angka:angka < 8, kumpulan_angka))
print(angka_baru)

# Kasus Genap

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

def fungsi_genap(angka):
    return angka % 2 == 0

angka_baru = list(filter(fungsi_genap, kumpulan_angka))

print(f"Hasil filtering genap adalah {angka_baru}")

# Pake lambda

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

angka_baru = list(filter(lambda angka:angka % 2 == 0, kumpulan_angka))

print(f"Hasil filtering genap dengan lambda adalah {angka_baru}")

# Kasus Ganjil

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

def fungsi_genap(angka):
    return angka % 2 == 1

angka_baru = list(filter(fungsi_genap, kumpulan_angka))

print(f"Hasil filtering genap adalah {angka_baru}")

# Pake lambda

kumpulan_angka = [1,2,3,4,5,6,7,8,9,10]

angka_baru = list(filter(lambda angka:angka % 2 == 1, kumpulan_angka))

print(f"Hasil filtering genap dengan lambda adalah {angka_baru}")
