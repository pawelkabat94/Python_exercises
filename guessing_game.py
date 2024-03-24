import random
my_number = random.randint(0,20)
guess = -1
trials = 0

print ("Guess my number")
while guess != my_number:
    trials += 1

    guess = int(input("Please provie a number: "))
    
    if guess == my_number:
        print("You guessed the number! It was",my_number, "it was your: ", trials, "try")
    elif guess > my_number:
        print("My number is lower than yours", guess, "it was your: ", trials, "try")
    else:
        print("My number is greather than", guess, "it was your: ", trials, "try")
