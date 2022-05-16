
#2Dynamically
# Instantiate Cache information, store previous known result

#Cache information
n = 10 #needs to be changed
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        cache[n] = n
    
    # Check cache
    if cache[n] != None:
       return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]
  
fib_dyn(10)
type(cache)
