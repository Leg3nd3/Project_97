import random
number = random.randint(1, 5)
guess = int(input("Enter a number from 1 to 5: "))
while number != "guess":
    print
    if guess < number:
        print("Guess is low")
        guess = int(input("Enter a number from 1 to 5: "))
    elif guess > number:
        print("Guess is high")
        guess = int(input("Enter a number from 1 to 5: "))
    else:
        print("You guessed it!")
        break