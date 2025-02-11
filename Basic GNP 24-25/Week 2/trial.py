'''Creating functions'''

def my_func():
    print("Hai SHB Modernhill")
    print("Ini adalah ekskul coding")
    print("Kelas basic")

my_func()

''' Kalkulator '''

def my_class(angka_pertama, angka_kedua):
    hasil = angka_pertama + angka_kedua
    print(f"Hasil dari kalkulasi adalah {hasil}")

my_class(5,3)

''' Murid Kelas '''

def my_class(firstName, lastName):
    print(f"{firstName} {lastName}")

my_class("John", "Doe")

def display_info(first_name, last_name):
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')

display_info('Cartman', 'Eric')

''' Maximum of 3 numbers '''

def max_func(a,b,c):
    max = a if a > b and a > c else b if b > c else c
    print(f'bilangan maksimum dari 3 angka ini adalah {max}')

max_func(1,4,7)

# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)

def sum_machine(angka_1, angka_2, angka_3, angka_4, angka_5):
    total = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
    print(f'hasil akhirnya dari penjumlahan {angka_1}, {angka_2}, {angka_3}, {angka_4} dan {angka_5} adalah {total}')

sum_machine(9,5,4,3,9)

''' Shortest & Longest '''
def filter_function(list):
    short = min(list, key=len)
    long = max(list, key=len)
    return short, long

list = ['surya', 'ardit', 'bintang', 'pavita']
hasil = filter_function(list)

print (hasil)