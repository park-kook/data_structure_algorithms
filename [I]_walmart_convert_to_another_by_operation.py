Consider a pair of integers, (a, b). The following operations 
can be performed on (a, b) in any order, zero or more times. 

(a, b) → (a + b, b) 

(a, b) → (a, a + b)
Return a string (“yes”, “no”) that denotes whether or not 
(a, b) can be converted to (c, d) by performing the operation zero or more times.

E.g.: 
(a, b) = (1, 1) 

(c, d) = (5, 2) 



def can_convert_recursive(a, b, c, d, memo=None):
    if memo is None:
        memo = {}

    # Base case: if we reach the target state
    if a == c and b == d:
        return 'yes'  # Stopping factor: target state reached
    
    # Base case: if the current state is out of bounds, return 'no'
    if a > c or b > d:
        return 'no'  # Stopping factor: out of bounds
    
    # Check if the current state has been computed before
    if (a, b) in memo:
        return memo[(a, b)]  # Stopping factor: memoization

    # Recursively check the two possible operations
    result1 = can_convert_recursive(a + b, b, c, d, memo)
    result2 = can_convert_recursive(a, a + b, c, d, memo)
    
    # If either recursive call returns 'yes', the current state is valid
    if result1 == 'yes' or result2 == 'yes':
        memo[(a, b)] = 'yes'
        return 'yes'
    
    # If both recursive calls return 'no', the current state is invalid
    memo[(a, b)] = 'no'
    return 'no'

# Example usage
a, b = 1, 1
c, d = 5, 2
output = can_convert_recursive(a, b, c, d)
print(output)  # Output: 'yes'


def can_convert(a, b, c, d):
    while c >= a and d >= b:
        if c == a and d == b:
            return 'yes'
        if c > d:
            c -= d
        else:
            d -= c
    return 'no'

# Example usage
a, b = 1, 1
c, d = 5, 2
output = can_convert(a, b, c, d)
print(output)  # Output: 'yes'
