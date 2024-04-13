correct_guess = "Brazil"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != correct_guess and not(out_of_guesses):
    if guess_limit > guess_count:
        guess = input("Who has won the most world cups? ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You're out of guesses, game over!")
else:
    print("Correct")



