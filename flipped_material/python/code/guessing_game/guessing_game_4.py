from random import randint
min_value = 1
max_value = 100
answer = randint(min_value, max_value)
guess = -1
moves = 0
while answer != guess:
    guess = int(input(f"Guess a number between {min_value} and {max_value} "))
    
    if guess < min_value or guess > max_value:
        continue

    moves = moves + 1
    if guess < answer:
        print("your guess was too low!")
    elif guess > answer:
        print("your guess was too high!")
print(f"{guess} was the right answer. You won in {moves} moves.")
