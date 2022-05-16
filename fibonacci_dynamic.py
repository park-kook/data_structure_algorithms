
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




#3Iteratively
#In this solution we can take advantage of Python's tuple unpacking!
def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    #a,b=0,1
    out=[]
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b
        out.append(a)
    return a, out

fib_iter(10)    



##Write a function that computes the Nth fibonazzi number
#using looping  techinque
def fib(n):
    a,b,=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
#using memoiztion
def memoize(fn,arg):
    memo={}
    if arg not in memo:
        memo[arg]=fn(arg)
    return memo[arg]

#fib() as writeen in example1
fibm=memoize(fib,7)
print(fibm)

#using memoization as decorator
class Memoize: 
    def __init__(self,fn):
        self.fn=fn
        self.memo={}
    def __call__(self,arg):
        if arg not in self.memo:
            self.memo[arg]=self.fn(arg)
            return self.memo[arg]
