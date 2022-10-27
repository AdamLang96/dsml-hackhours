"""
Time Complexity:  O(n^2)
Space Complexity: O(1)
Iterative: nested for-loops --> Brute force solution
"""
def highest_profit(apple_stock): 
  # validate that apple_stock is a list and has integers
  if type(apple_stock) != list or not len(apple_stock) or not isinstance(apple_stock[0], int): return 0
  # declare a variable to store the profit
  profit = 0

  # iterate through each element in apple_stock
  for i in range(len(apple_stock)):
    # the current element is the bought stock
    buy_stock = apple_stock[i]
    # iterate through the remaining elements and find the best time to sell for maximum profit
    for j in range(i + 1,len(apple_stock)):
      sell_stock = apple_stock[j]

      curr_profit = sell_stock - buy_stock
      profit = max(profit, curr_profit)
  
  # return the maxium profit
  return profit



"""
Time Complexity:  O(1)
Space Complexity: O(1)
Iterative: Single loop using pointers
"""
def highest_profit(apple_stock):
  # validate that apple_stock is a list and has integers
  if type(apple_stock) != list or not len(apple_stock) or not isinstance(apple_stock[0], int): return 0

  # declare a variable to store the profit
  profit = 0

  # initialize a high and low pointer, starting at the first two indices in the list
  low, high = 0, 1

  # iterate while high is less than the length of apple_stock
  while (high < len(apple_stock)):
    curr_profit = apple_stock[high] - apple_stock[low]

    profit = max(profit, curr_profit)
    
    if apple_stock[high] < apple_stock[low]:
      low = high

    high += 1

  # return the maximum profit
  return profit


"""
Time Complexity:  O(1)
Space Complexity: O(1)
Iterative: Single loop using reduce
Must import reduce from functools module
"""
from functools import reduce

def highest_profit(apple_stock):
  # validate that apple_stock is a list and has integers
  if type(apple_stock) != list or not len(apple_stock) or not isinstance(apple_stock[0], int): return 0

  # initialize the position on the lowest value to buy stock
  minIndex = 0

  def reduce_func(acc, index):
    # provide access to minIndex within this scope
    nonlocal minIndex
    # if the current stock is smaller than the smallest saved, 
    # update the index position of the lowest value
    if apple_stock[index] < apple_stock[minIndex]: minIndex = index
    # save the value of selling the stock at this index
    sell_stock = apple_stock[index]
    # save the value of buying the stock at the minIndex
    buy_stock = apple_stock[minIndex]
    # calculate the current profit
    profit = sell_stock - buy_stock

    if profit > acc: acc = profit
    return acc

  return reduce(reduce_func, range(0, len(apple_stock)))
