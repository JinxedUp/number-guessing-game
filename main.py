import os
import random

from colorama import Back, Fore, Style, init

os.system("cls")

print(Fore.GREEN + "welcome to the number guessing game!")
print(Fore.GREEN + "im thinking of a number between 1 and 100.")

print(
    Fore.CYAN
    + """
please select the difficulty leve:

1. Easy (10 chanches)
2. Medium (5 chanches)
3. Hard (3 chances)
"""
)

choice = input("\nEnter your choice (1/2/3):")

if choice == "1":
    attempts = 10
    print(Fore.GREEN + "\nYou selected Easy difficulty.")
elif choice == "2":
    attempts = 5
    print(Fore.GREEN + "\nYou selected Medium difficulty")
elif choice == "3":
    attempts = 3
    print(Fore.GREEN + "\nYou selected Hard difficulty")
else:
    print(Fore.RED + "\ninvalid choice defaulting to Medium difficulty")
    attempts = 5

number_to_guess = random.randint(1, 100)


print("\nLets start the game!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < number_to_guess:
        print(Fore.RED + "Incorrect! the number is greater than", guess)
    elif guess > number_to_guess:
        print(Fore.RED + "Incorrect! number is less than", guess)
    else:
        print(
            Fore.GREEN
            + "Congratulations! you guessed the correct number in 4 attempts."
        )
        break
else:
    print(
        Fore.RED
        + f"\n Sorry youve used all your chances. The number was {number_to_guess}"
    )
