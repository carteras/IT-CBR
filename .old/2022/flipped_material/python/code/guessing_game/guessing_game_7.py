from random import randint

def make_guess(min_value, max_value, moves):
    still_guessing = True
    while still_guessing:
        guess = int(input(f"Guess a number between {min_value} and {max_value} "))
        if guess > min_value or guess < max_value:
            still_guessing = False
    return guess, moves + 1

def auto_guess(min_value, max_value):
    return randint(min_value, max_value)
    

def check_for_hints(guess, answer):
    if guess < answer:
        return "your guess was too low!"
    elif guess > answer:
        return "your guess was too high!"
    return f"{guess} was the right answer."

def guess_fitness_test(hint):
    if hint == "your guess was too low!":
        return -1
    elif hint == "your guess was too high!":
        return 1
    return 0


min_value = 1
max_value = 100
sum_of_moves = 0
games_played = 0

for i in range(1, 10):
    answer = randint(min_value, max_value)
    guess = -1
    moves = 0
    low_guess = min_value
    high_guess = max_value
    fitness = 0
    while answer != guess:
        guess = auto_guess(min_value, max_value)
        moves += 1
        hint = check_for_hints(guess, answer)
        fitness = guess_fitness_test(hint)
        print(hint, guess, answer, fitness)

    print(f"You won in {moves} moves.")
    sum_of_moves += moves
    games_played += 1
print(sum_of_moves, games_played, sum_of_moves/games_played)
