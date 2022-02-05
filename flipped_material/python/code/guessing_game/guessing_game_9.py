from random import randint

def make_guess(min_value, max_value, moves):
    still_guessing = True
    while still_guessing:
        guess = int(input(f"Guess a number between {min_value} and {max_value} "))
        if guess > min_value or guess < max_value:
            still_guessing = False
    return guess, moves + 1

def auto_guess(low, high, last_guess, fitness):
    if fitness > 0:
        high = last_guess
    elif fitness < 0:
        low = last_guess
    guess = int((high+low)/2)
    return guess, low, high
    

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


sum_of_moves = 0
games_played = 0
quickest_game = 999999
longest_game = -1
min_value = 1
max_value = 1000_000_000_000
for _ in range(0, 1000000):
    answer = randint(min_value, max_value)
    guess = -1
    moves = 0
    low_guess = min_value
    high_guess = max_value
    fitness = 0

    while answer != guess:
        guess, low_guess, high_guess = auto_guess(low_guess, high_guess, guess, fitness)
        moves += 1
        hint = check_for_hints(guess, answer)
        fitness = guess_fitness_test(hint)
    
    sum_of_moves += moves
    games_played += 1
    if moves < quickest_game: 
        quickest_game = moves
    if moves > longest_game:
        longest_game = moves
print(f"You played a total of {games_played:,} games")
print(f"On average, you took {sum_of_moves/games_played:,} moves")
print(f"The quickest game was {quickest_game}")
print(f"Your longest game was {longest_game}")