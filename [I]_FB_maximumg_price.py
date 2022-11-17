'''
Facebook onsite interview 3
Problem
Create a function that takes in a list of unsorted prices (integers) and a maximum possible price value, 
and return a sorted list of prices

Requirements
Your function should be able to perform this in less than O(nlogn) time.

Solution
We can actually solve this problem by using a counting sort. Basically a counting sort works well 
when you know the range of integer values you will have ahead of time.

Read the wikipedia article linked above for a full break down, and an implementation is here below 
(using the prices situation described in the problem above).

'''
def solution(unsorted_prices,max_price):
    
    # list of 0s at indices 0 to max_price
    prices_to_counts = [0]* (max_price+1)
    
    # populate prices
    for price in unsorted_prices:
        prices_to_counts[price] +=1
        
    # populate final sorted prices
    sorted_prices = []
    
    # For each price in prices_to_counts
    for price,count in enumerate(prices_to_counts):
        if count==0:
            continue
        # for the number of times the element occurs
#        for time in range(count):
            
            # add it to the sorted price list
#            sorted_prices.append(price)
        sorted_prices.append(price)           
    return sorted_prices
solution([4,6,2,7,3,8,9],9)
unsorted_prices = [4,6,2,7,3,8,9]
max_price=9
