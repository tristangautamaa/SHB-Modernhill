import random
import math

# MENJALANKAN PROGRAM DARI FILE LAIN / EXTERNAL --> import

# === IMPORT RANDOM ===
listAngka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(listAngka))

# === IMPORT MATH ===
pie = math.pi
print(pie)
print(math.pi)

# === LOCAL IMPORT LIBRARY

# Additions

from logic import tambah
print(tambah(5, 5))

# Multiplications

from logic import kali
print(kali(5, 5))

# Reversed Words

from logic import uno_reverse
print(uno_reverse("Ciko"))


# === RAND INT (RANDOM INTEGER) ===

# positive range
vivi = random.randint(1, 10)
print(f"Random integer between 1 - 10 is: {vivi}")

# === STRING LIBRARY ===
import random
import string

def randomString(jassen):
    return ''.join(random.choices(string.ascii_letters, k=jassen))

print("Random String is", randomString(10))