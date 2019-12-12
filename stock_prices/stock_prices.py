#!/usr/bin/python

import argparse
# pass in a list of prices
def find_max_profit(prices):
      #get the min price from the list
      cur_min_price = min(prices)
      cur_max_profit = 0
      #loop through the prices subtracing the cur min price and compare against cur max profit, store highest max profit
      for amount in prices:
            if amount - cur_min_price > cur_max_profit:
                  cur_max_profit = amount - cur_min_price
      return cur_max_profit


print(find_max_profit([1050, 270, 1540, 3800]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))