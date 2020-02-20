#!/usr/bin/python

import sys


def rock_paper_scissors(number_of_rounds):
    available_throws = ["rock", "paper", "scissors"]
    combinations = []

    def combination_builder(rounds, result):
        # When it makes it all the way back to 0, we
        # need to stop it. (Base Case)
        if rounds == 0:
            combinations.append(result)
            return

        for throw in available_throws:
            # Build each list within each available throw up by looping
            # through the combination_builder until it hits 0
            combination_builder(rounds - 1, result + [throw])

    # Kick off the builder
    combination_builder(number_of_rounds, [])
    # print(combinations)

    # Celebrate
    return combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
