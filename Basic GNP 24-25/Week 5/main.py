# APLIKASI INPUT NILAI

# Function input_nilai()
# Function hitung_nilai()
# Function main()

def input_nilai():
    daftar_nilai = [] # LIST
    print("Masukkan 3 nilai:")
    
    for i in range(3):
            while True:
                try:
                    nilai = float(input(f"Masukkan Nilai {i+1}: "))
                    daftar_nilai.append(nilai)
                    break
                except ValueError:
                    print("Input Salah! Silahkan Masukkan Angka.")
    return daftar_nilai

def hitung_nilai(daftar_nilai):
    print("\nKalkulasi Nilai:")
    print("Nilai Tertinggi: ", max(daftar_nilai))
    print("Nilai Terendah: ", min(daftar_nilai))
    print("Nilai Rata-rata: ", sum(daftar_nilai) / len(daftar_nilai))

def main():
    print("KALKULATOR NILAI SISWA")
    final = input_nilai()
    hitung_nilai(final)

main()
