#!/usr/bin/python

import argparse


# My time is too valuable to spend it trying to decipher horrible instructions
#  and comparing it to the test cases to figure out what they actually mean.
#
#  This might help whoever wrote them.
#  https://megabyterose.com/2018/02/write-technical-instructions/
#
#  kthxbia
def find_max_profit(prices):
    pass


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
