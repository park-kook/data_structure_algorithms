'''
Amazon interview question onsite1
#You've been given a list of historical stock prices for a single day for Amazon stock. 
#The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, 
#the element at index 1 is the next recorded price of the stock for that day, etc. 
Your task is to write a function that will return the maximum profit possible from 
the purchase and sale of a single share of Amazon stock on that day. 
#Keep in mind to try to make this as efficient as possible.
#For example, if you were given the list of stock prices:
'''
stock_prices = [12,11,15,3,10]

#Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).  

def profit(stock_prices):
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with a profit of zero
    max_profit = 0
    
    for price in stock_prices:
        
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
        # Check the current price against our minimum for a profit 
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        
        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)
        
    return max_profit

profit([12,11,15,3,10])
profit([30,22,21,5])

profit([12,11,15,3,10])
profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10])

def maxProfit(stock_prices):
    l,r=0,1
    maxP = 0
    while r < len(stock_prices):
        if stock_prices[l] < stock_prices[r]:
            profit = stock_prices[r] - stock_prices[l]
            maxP = max(maxP, profit)
        else: 
            l=r
        r+=1
    return maxP

maxProfit([12,11,15,3,10])


    



def sum_profit(arr):
    if len(arr)==0:
        return 0
    max_sum=current_sum=arr[0]
    for num in arr[1:]:
        current_sum =  max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum
sum_profit([12,11,15,3,10])


def profit2(stock_prices):
    
    # Check length
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with an initial max profit
    max_profit = stock_prices[1] - stock_prices[0]
    
    # Skip first index of 0
    for price in stock_prices:
        
       
        # NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING
        
        # Check the current price against our minimum for a profit 
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        
        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)
        
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
        
        
    return max_profit
profit2([12,11,15,3,10])
# Exception Raised
profit2([1])
profit2([30,22,21,5])




"""
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (continaing at least one number) 
which has the largest product
"""
#nums = [2,3,-2,4] #output = 6

nums = [-2,3,-2,4] #output = 48
#nums = [0,3,-2,4] #output = 4

def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1,1
    
    for n in nums:
        if n ==0:
            curMin, curMax = 1,1 
            continue 
        tmp = curMax * n #-2, -6, -6, 48
        curMax = max(n*curMax, n*curMin, n) #-2, 3, 12 from -6 min * -2 n = 12, 48
        curMin = min(tmp, n*curMin, n) #-2, -6, -6, -24
        res = max(res, curMax)# -2, -2, 12, 48
    return res

maxProduct(nums)
