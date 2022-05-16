factorial_memo = {}
def factorial(k):
    #if k<2:
    if k == 1:
        return 1
    if k not in factorial_memo:
        factorial_memo[k]=k*factorial(k-1)
    return factorial_memo[k]

factorial(5)


factorial_memo = {}
def factorial(k):
    #if k<2:
    if k == 1:
        return 1
    if k not in factorial_memo:
        factorial_memo[k]=k*factorial(k-1)
    return factorial_memo[k]

factorial(5)


class Memoize:
    def __init__(self,value):
        self.value=value
        self.memo={}
    def __call__(self,*args):
        if not args in self.memo:
            self.memo[args]= self.value(*args)
        return self.memo[args]
################################    
def factorial2(k):
    if k<2:
        return 1
    return k*factorial2(k-1)
factorial2(5)

factorial3 = Memoize(factorial2(5))
factorial3.value
