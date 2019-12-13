#!/usr/bin/python

import argparse
# pass in a list of prices
def find_max_profit(prices):
      #get the min price from the list
      if len(prices) > 0:
        # get biggest stock index
        biggest_stock = max(prices)
        #if biggest stock is in the first index go to the next
        is_biggest_stock_first = prices.index(biggest_stock)

        if is_biggest_stock_first == 0:
     
          biggest_stock_index = 0
          value_biggest_stock = prices[0]
          copy_prices = prices.copy()
          remove_biggest_index = copy_prices.remove(value_biggest_stock)
          second_biggest_stock = max(copy_prices)
          index_second_biggest_stock = prices.index(second_biggest_stock)
          # print(second_biggest_stock)
          # print(copy_prices)
          
          price_selection = copy_prices[:index_second_biggest_stock + 1]
          price_selection_two = prices[:index_second_biggest_stock + 1]
          # print(price_selection, "this is price selection")
          # print(price_selection_two, "this is price selection alt")
          if len(price_selection_two) == 2:
            price_max = max(price_selection_two)
            price_min = min(price_selection_two)
            profit = price_min - price_max
            return profit
          else:
          #get compare and return profit
              cur_min_price = min(price_selection)
              cur_max_profit = 0
              #loop through the prices subtracing the cur min price and compare against cur max profit, store highest max profit
              for amount in price_selection:
                    if amount - cur_min_price > cur_max_profit:
                          cur_max_profit = amount - cur_min_price

     
        else:
          biggest_stock_index = prices.index(biggest_stock)
          price_selection = prices[:biggest_stock_index + 1]
  
          #remove any prices after the biggest stock

          #get compare and return profit
          cur_min_price = min(price_selection)
          cur_max_profit = 0
          #loop through the prices subtracing the cur min price and compare against cur max profit, store highest max profit
          for amount in price_selection:
                if amount - cur_min_price > cur_max_profit:
                      cur_max_profit = amount - cur_min_price
             
     
      return cur_max_profit

print(find_max_profit([10, 7, 5, 8, 11, 9]), 6)
print(find_max_profit([100, 90, 80, 50, 20, 10]), -10)
print(find_max_profit([1050, 270, 1540, 3800, 2]), 3530)
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))