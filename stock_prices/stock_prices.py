#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Start at a super super low number as your base case to compare to
    max_profit = -100000000000000000000000000000000000000000000000000000

    # Outer loop for pegging it at the buy price before checking the rest against it
    for index_a in range(0, len(prices)):

        # Inner loop for comparing the remaining numbers with the start price
        for index_b in range(index_a + 1, len(prices)):

            # Get the difference between outer loop num and inner loop num
            diff = prices[index_b] - prices[index_a]

            # Check and store in outer most scoped variable
            if diff > max_profit:
                max_profit = diff

    # Celebrate
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
