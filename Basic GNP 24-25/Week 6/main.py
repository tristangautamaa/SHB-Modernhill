# DATA TYPES
# 1. NUMBERS - Integers and floats

my_number = 10 # Integer
my_float = 7.5 # Float

print("Ini adalah angka: ", my_number)
print("Ini adalah desimal: ", my_float)

# 2. STRINGS - Text data

my_name = "Tristan Gautama" # String
print("Nama saya adalah: ", my_name)

# 3. BOOLEANS - True or False values
a = 5
b = 10
my_boolean = a < b
print("Apakah a lebih besar dari b?", my_boolean)


# Try it yourself! Create your own variables with different data types
my_number = ... # Integer / Float
my_text = ... # String
my_boolean = ... # Boolean

print("......")
print("......")
print("......")

# ---------------
# COLLECTIONS
# ---------------

# 1. LISTS - Ordered collections that can be changed
# Lists use square brackets []

fruits = ["apel", "pisang", "mangga", "jeruk"]

print("List Buah-Buahan:")
print(fruits)
print("Buah index 1: ", fruits[2])
print("Buah index terakhir: ", fruits[-1])

# We can change lists
fruits.append("durian") # Menambahkan item
print("Setelah menambahkan durian: ", fruits)

fruits[3] = "anggur" # Mengganti item
print("Setelah mengganti menjadi anggur: ", fruits)

# 2. TUPLES - Ordered collections that CANNOT be changed
# Tuples use parentheses ()

colors = ("merah", "biru", "hitam", "putih", "hijau", "kuning")

print("My favorite colors: ")
print(colors)
print("The best color: ", colors[0])


# 3. DICTIONARIES - Collections of key-value pairs
# Dictionaries use curly braces {}

supra = {
    "Manufacturer": "Toyota",
    "Year": 2011,
    "Color": "Red",
}

print(supra)
print("Merk apa?: ", supra["Manufacturer"])
print("Warna apa?: ", supra["Color"])


# Challenge 1: Create a list of your favorite hobbies

# Challenge 2: Create a dictionary about your favorite movie or game