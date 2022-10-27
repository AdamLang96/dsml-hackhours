import pytest
from solutions.file1 import highest_profit


# Testing highest_profit with invalid inputs
# Expected input: list of integers
@pytest.mark.parametrize("apple_stock, profit", 
[
  (['ten', 'nine', 'eight'], 0),
  ({0: 10, 1: 5, 2: 0}, 0),
  ('stocks', 0),
  (1000, 0),
  (None, 0)
]
)
def test_invalid_inputs(apple_stock, profit):
  assert highest_profit(apple_stock) == profit


# Testing highest_profit
# Function should return 0 if there's no possibility of making a profit
@pytest.mark.parametrize("apple_stock, profit", 
[
  ([100, 90, 70, 40, 0], 0),
  ([], 0)
]
)
def test_no_profit(apple_stock, profit):
  assert highest_profit(apple_stock) == profit


# Testing highest_profit
# Function should return the highest profit possible
@pytest.mark.parametrize("apple_stock, profit", 
[
  ([0, 2000, 4000, 6000, 8000, 10000], 10000),
  ([2000, 1000, 100, 200, 400, 100], 300),
  ([8, 5, 4, 3, 2, 7, 2], 5)
]
)
def test_highest_profit1(apple_stock, profit):
  assert highest_profit(apple_stock) == profit


# Testing highest_profit
# Function should return the highest profit possible when given multiple possible profits
@pytest.mark.parametrize("apple_stock, profit", 
[
  ([1000, 500, 1000, 1500, 0, 200, 800, -10, 0, 100], 1000),
  ([0, 300, 200, 500, 600, 100, 399, 350, 500], 600),
  ([200, 600, 700, 100, 300, 200, 620], 520)
]
)
def test_highest_profit2(apple_stock, profit):
  assert highest_profit(apple_stock) == profit