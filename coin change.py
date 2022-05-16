'''
#Coin Change1
you are given coins of different denominations and a total of money amount. 
Write a fucntion to compute the fewest number of conis that you need to make up that amount. 
if that amount of money cannot be made up by any combination of the coins, return -1
you may assume that you have an infinite number of each kind of coin.

3. Dynamic Programing - Bottom-up
time complexity = big o(amount * len(coins))
space complexity  = big o (amount) for just dynamic space
'''
amount = 7
def coninchange(amount,coins):
    dp = [amount+1]*(amount+1) #amount+1 just max number (amount+1) cause start from 0
    dp[0]=0
    
    for a in range(1, amount+1):
        for c in coins:
            if a - c>=0:
                dp[a] =  min(dp[a],1+dp[a-c])
                #coin = 4, a = 7, dp[7] = 1+dp[7-4]
            
    return dp[amount] if dp[amount] !=amount + 1 else -1 #if default value not given, then return dp[amount]

coninchange(7,[1,3,4,5])
coninchange(63,[1,5,10,25])
amount = 7
coins=[1,3,4,5]
#Coin Change2
#Given a target amount n and a list (array) of distinct coin values, 
#what's the fewest coins needed to make the change amount.
#1 cent = penny, 5cents = nickel, 10cents = dime, 25cents = quarter.
def rec_coin(target,coins):
    '''
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change
    
    Note, this solution is not optimized.
    '''
    
    # Default to target value
    min_coins = target
    
    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1
    
    else:
        
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive Call (add a count coin and subtract from the target) 
            num_coins = 1 + rec_coin(target-i,coins) # number of coins we need
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                
                min_coins = num_coins
                
    return min_coins

rec_coin(7,[1,3,4,5])

rec_coin(63,[1,5,10,25])

rec_coin(15,[1,5,10,25])


#Each node here corresponds to a call to the rec_coin function. 
#The label on the node indicated the amount of change for which 
#we are now computng the number of coins for. Note how we are recalculating values 
#we've already solved! For instance 15 is called 3 times. 
#It would be much better if we could keep track of function calls we've already made.


########### rec_coin_dynam

target = 73
coins = [1,5,10,25]
known_results = [0]*(target+1)
#known_results = [None]*(target+1)


    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)
    
    OUTPUT: Minimum number of coins needed to make the target.
    '''
def rec_coin_dynam(target,coins,known_results):

    
    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    # this is dynamic programming that's going to save you a lot of time in recursive calls
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
    #elif known_results[target]!=None:
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
                
    return min_coins



target = 7
coins = [1,3,4,5]
known_results = [0]*(target+1)

rec_coin_dynam(target,coins,known_results)

