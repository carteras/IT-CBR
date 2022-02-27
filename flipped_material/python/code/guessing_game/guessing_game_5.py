from random import randint

def make_guess(min_value, max_value, moves):
    still_guessing = True
    while still_guessing:
        guess = int(input(f"Guess a number between {min_value} and {max_value} "))
        if guess > min_value or guess < max_value:
            still_guessing = False
    return guess, moves + 1

def check_for_hints(guess, answer):
    if guess < answer:
        return "your guess was too low!"
    elif guess > answer:
        return "your guess was too high!"
    return f"{guess} was the right answer. "

min_value = 1
max_value = 100
answer = randint(min_value, max_value)
guess = -1
moves = 0

while answer != guess:
    guess, moves = make_guess(min_value, max_value, moves)
    print(check_for_hints(guess, answer))

print(f"You won in {moves} moves.")
