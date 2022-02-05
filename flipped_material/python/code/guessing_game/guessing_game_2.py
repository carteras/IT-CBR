answer = 5
guess = input("Pick a number between 1 and 10 ")
guess = int(guess)
if guess < answer:
    print("Your guess was too low.")
elif guess > answer:
    print("Your guess was too high.")
else:
    print("You win")