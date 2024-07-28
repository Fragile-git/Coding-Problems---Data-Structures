
"""
 Suppose you have given the stock prices for respective days like 
 (100, 180, 260, 310, 40, 535, 695). 
 The stock price for the 1st day is 100, the 2nd day it is 180 and so on.

In the above case, in the following scenarios user will get maximum profit.

Buy stock on 1st day (100)
Sell stock on 4th day (310)
Buy stock on 5th day  (100)
Sell stock on 7th day (695)
Algorithm steps:

Find the local minima (buying stock)
Find local maxima (selling stock)
Repeat until all days are covered.


"""

stock = [100,180,260,310,40,535,695]


# Valley Approach
def valley(stock): 
    profit = 0
    sell_day = 0
    buy_day = 0 # with respect to list indexing, this is day 1 
    days = len(stock) # how many days 

    for i in range(1,days): # main algorithm, start at index 1 (day2)
                            # when to buy/sell stock
        # Sell:
        if stock[i] > stock[i-1]:
            # if the next day price is higher than the current day, update the sell day
            sell_day = i # update the sell date to next day 

        # Buy:
        else: # if the next day  price is lower than the current day, we need to sell it 
            print(f"Buy Stock on day {buy_day + 1} {stock[buy_day]}") 
            print(f"Sell Stock on day {sell_day + 1} {stock[sell_day]}") 
            profit += stock[sell_day] - stock[buy_day]
            buy_day = i  # Update buy date to the next day

    # Runs after the for loop is done
    # Check for the last potential sell opportunity
    if sell_day > buy_day: # if sell day is 
        print(f"Buy Stock on day {buy_day + 1} {stock[buy_day]}")
        print(f"Sell Stock on day {sell_day + 1} {stock[sell_day]}")
        profit += stock[sell_day] - stock[buy_day]


    return f" The profit is {profit}"


valley(stock)        
    
