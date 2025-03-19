# ===== MINI-EXERCISE 1: SIMPLE IF STATEMENT =====
# Ice Cream Choice

print("===== EXERCISE 1: SIMPLE IF =====")
flavor = input("What's your favorite ice cream flavor? ")

if flavor.lower() == "chocolate":
    print("Yum! Chocolate is a classic choice!")

print("Ice cream is delicious no matter what flavor!")

# ===== MINI-EXERCISE 2: IF-ELSE =====
# Weather Activity Chooser

print("\n===== EXERCISE 2: IF-ELSE =====")
weather = input("Is it sunny or rainy today? ")

if weather.lower() == "sunny":
    print("Great day for playing outside!")
else:
    print("Perfect day to read a book inside!")

# ===== MINI-EXERCISE 3: IF-ELIF-ELSE =====
# Pet Sounds

print("\n===== EXERCISE 3: IF-ELIF-ELSE =====")
pet = input("Choose a pet (dog, cat, bird): ")

if pet.lower() == "dog":
    print("Woof woof!")
elif pet.lower() == "cat":
    print("Meow!")
elif pet.lower() == "bird":
    print("Tweet tweet!")
else:
    print("I don't know what sound that pet makes!")

# ===== MINI-EXERCISE 4: SIMPLE WHILE LOOP =====
# Countdown

print("\n===== EXERCISE 4: SIMPLE WHILE LOOP =====")
count = 5

while count > 0:
    print(f"Countdown: {count}")
    count = count - 1

print("Blast off! 🚀")

# ===== MINI-EXERCISE 5: SIMPLE FOR LOOP =====
# Favorite Foods

print("\n===== EXERCISE 5: SIMPLE FOR LOOP =====")
foods = ["pizza", "sushi", "tacos", "ice cream", "pasta"]

print("My favorite foods:")
for food in foods:
    print(f"I love {food}!")

# ===== MINI-EXERCISE 6: LOOP WITH BREAK =====
# Secret Number

print("\n===== EXERCISE 6: LOOP WITH BREAK =====")
secret = 7

for guess in range(1, 11):
    print(f"Is it {guess}?")
    if guess == secret:
        print("That's the secret number!")
        break

# ===== MINI-EXERCISE 7: NESTED IF =====
# Movie Night

print("\n===== EXERCISE 7: NESTED IF =====")
age = int(input("How old are you? "))

if age >= 13:
    print("You can watch PG-13 movies!")
    movie = input("Do you like action or comedy movies? ")
    if movie.lower() == "action":
        print("Try watching Spider-Man!")
    else:
        print("Try watching a funny movie!")
else:
    print("Let's find a movie rated PG for you!")

# ===== MINI-EXERCISE 8: NESTED LOOP =====
# Multiplication Table

print("\n===== EXERCISE 8: NESTED LOOP =====")
print("Mini Multiplication Table:")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print("---")