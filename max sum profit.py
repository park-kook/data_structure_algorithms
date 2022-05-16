
def sum_profit(arr):
    if len(arr)==0:
        return 0
    max_sum=current_sum=arr[0]
    for num in arr[1:]:
        current_sum =  max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum
sum_profit([12,11,15,3,10])



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
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else: 
            l=r
        r+=1
    return maxP

maxProfit([12,11,15,3,10])
