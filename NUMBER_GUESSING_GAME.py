import random

random_number = random.randint(1,20)

input_number = ' '
number_attempts = 0

print("Welcome to the Number Guessing Game!")
print(" ")

while input_number != random_number:
    input_number = float(input("Guess a number between 1 and 20: "))
    if input_number == random_number:
        print(f"Correct!")
    elif input_number > random_number:
        print(f"Too high!")
    else:
        print(f"Too low!")

    number_attempts += 1

print(" ")
print("Congratulations! You guessed it!")
print(" ")
print(f"You guessed the number in {number_attempts} attempts!")








