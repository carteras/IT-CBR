answer = 5
guess = input("Pick a number between 1 and 10 ")
guess = int(guess)
if guess != answer:
    print("You lose")
else:
    print("You win")