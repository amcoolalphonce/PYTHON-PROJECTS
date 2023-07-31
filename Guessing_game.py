import random
number = random.randrange(1,6) #choose a random number between  1 and 6(6 excluded)
guess = int(input("Enter any number: "))
while number!= guess:
    if guess < number:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > number:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("You guessed the number right!!")