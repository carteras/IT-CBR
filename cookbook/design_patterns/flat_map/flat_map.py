from typing import Iterable

def coins_possibility(option):
    return [f'{option} door and flips {"heads"}', f'{option} door and flips {"tails"}']

def food_possibilities(option):
    return [f"{option} eats a {'apple'}", f"{option} eats a {'banana'}", f"{option} eats a {'orange'}"]

def lives_or_dies_possibilities(option):
    return [f'{option} and yet {"lives"}',f'{option} and yet {"dies"}']

def flat_map(transform: callable, i: Iterable):
    if type(i) is str: i = i.split(", ")
    # return ", ".join([val for sublist in list(map(transform, i)) for val in sublist])
    return [val for sublist in list(map(transform, i)) for val in sublist]

doors = ['red', 'green', 'blue']
door_and_coins = flat_map(coins_possibility, doors)
food_and_coins = flat_map(food_possibilities, door_and_coins)
lives_or_dies = flat_map(lives_or_dies_possibilities, food_and_coins)
for option in lives_or_dies:
    print(f"Stephen Strange goes through the {option}")