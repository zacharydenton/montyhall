#!/usr/bin/env python3
import random


def new_game():
    game = [("closed", "goat"), ("closed", "goat"), ("closed", "car")]
    random.shuffle(game)
    return game


def others(game, choice):
    return [i for i, _ in enumerate(game) if i != choice]


def closed(game):
    return [i for i, (status, _) in enumerate(game) if status == "closed"]


def open(game, door):
    open_door = ("open", game[door][1])
    game[door] = open_door
    return game


def simulate(swap=False, iterations=10000):
    total = 0
    success = 0
    for _ in range(iterations):
        total += 1
        game = new_game()
        choice = random.randrange(len(game))
        goats = [i for i in others(game, choice) if game[i][1] == "goat"]
        game = open(game, random.choice(goats))
        if swap:
            choice = [i for i in closed(game) if i != choice][0]
        if game[choice][1] == "car":
            success += 1
    return success / total


def main():
    standard = simulate(False)
    swapped = simulate(True)
    print("win probability (standard): {}".format(standard))
    print("win probability (swapped): {}".format(swapped))


if __name__ == "__main__":
    main()
