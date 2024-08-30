'''
Meta interview screnning test
Given a long string, write a method that returns true if the string is a valid number or false otherwise. 
Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, 
"-" and ".". The string can be very long (think millions of characters) and no built-in function/class 
can handle it without overflowing or losing precision.

| Input     | Output 
| -----     | ----- 
| "13"      | TRUE 
| "3.0"     | TRUE 
| "-7.4"    | TRUE 
| "-13.5"   | TRUE 
| "abc"     | FALSE 
| "123a"    | FALSE 
| "-."      | FALSE 
| "-..---." | FALSE 
| "1.0.0.1" | FALSE
'''

def valid(s):

    isdigit = set("0123456789.-")
    dotcount=0
    minuscount=0
    stack=[]

    flagDotorM = False
    if len(s) == 0:
        return False
    for i,cha in enumerate(s):
        if cha not in isdigit:
          return False
        if cha == '-' and i!=0:
          return False
        if cha =='-':
          minuscount +=1
          if minuscount >=2:
            return False
    
        if cha =='.':
          dotcount+=1
          if dotcount >=2:
              return False
#          if s[i+1] not in isdigit:
#              return False
        

        if s[i] =='.' :
            if i+1==len(s):# if .  or - is the last character
                return False
            
#            if  s[i-1] not in onlynum:
#                return False

    return True
s='-.'
valid('') #false
valid('3-.5') #false
valid('35') #True
valid('-3.5') #True
valid('abc') #false
valid('-abc') #false
valid('3.5') #true
valid('-.') # false
valid('35-') # false
valid('3.') # false
valid('-..---') #false
valid('1.0.0.1') #false
'''




''
check if a given string is a valid number (integer or floating point)
input str = '11.5' output: true
input: str = "abc" output: false

input: str = "2e10"
output: true

input: 10e5.4
output: false

1.ignore the leading and trailing white space
2.ignore the +,- and . at the start. 
3. ensure that the characters in the string belong to {+,-,.,e,[0-9]}
4. ensure that no '.' comes after 'e'
5. a dot character '.' should be followed by a digit
6. the character 'e' should be followed either by +,- or a digit.
'''

def valid_number(str):
    i = 0
    j = len(str)-1
    
    #handling whitespaces
    while i<len(str) and str[i] == ' ':
        i+=1
    while j>= 0 and str[j] == ' ':
        j-=1
        
    if i>j:
        return False
    #if a string is of length 1 and the only character is not a digit
    if (i==j and not(str[i]>='0' and str[i]<='9')):
        return False
    
    #if the 1st char is not '+', '-', '.' or digit
#    if (str[i] != '.' and str[i] !='+' and str[i] !='-' and not(str[i]>='0' and str[i]<='9')):
#        return False
    
    #to check if a '.' or 'e' is found in given string. We use this flag to make sure that either of them appear
    #only once. 
    flagDotOrE = False
    
    for i in range(j+1):
        # if any of the char does not belong to (digit,+,-.,e)
        if (str[i]!='e' and str[i]!='.' and str[i]!='+' and str[i] !='-' and not (str[i]>='0' and str[i]<='9')):
            return False
        
        if str[i]=='.':
            
            #check if the char e has already occured before '.'. If yes, return 0
            if flagDotOrE: #currently this is False, if it is true then retrun False otherwise pass
                return False
            if i+1 >= len(str):
                return False
            if (not(str[i+1]>='0' and str[i+1]<='9')):
                return False
            
        elif str[i]=='e':
            #set flagDotOrE= 1 when e is encountered
            flagDotOrE = True
            if (not (str[i-1]>='0' and str[i-1] <= '9')):
                return False
            
            # if e is the last character
            if i+1 >= len(str):
                return False
            
            #if e is not followed by + - or a digit
            if (str[i+1] != '+' and str[i+1] != '-' and str[i+1]>='0' and str[i+1]<='9'):
                return False

    return True


    
valid_number ("11.5")      
valid_number ("11..5")      
valid_number ("abc")     
valid_number ("10e5.4")   #false  
valid_number ("1.0e54") 
valid_number ("2e10")   
'''

To solve the problem of determining whether a string is a valid number, considering only integers and decimals as valid, we can follow these steps:

	1.	Check for invalid characters: The only valid characters in the string are digits (‘0’-‘9’), a single minus sign (’-’), and a single decimal point (’.’). Any other characters would make the string invalid.
	2.	Check placement of special characters: The minus sign (’-’) can only appear at the beginning of the string, and there should be at most one decimal point (’.’).
	3.	Ensure proper format: The string should have digits either before or after the decimal point (or both). Strings like “.”, “-.”, and “-..” are invalid.

Let’s implement this in Python:

Python Code:
'''
def is_valid_number(s):
    if len(s) == 0:
        return False
    
    # Check for initial minus sign
    if s[0] == '-':
        s = s[1:]
    
    # Variables to keep track of occurrences of '.' and digits
    has_dot = False
    has_digit = False
    
    for char in s:
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot:
                return False
            has_dot = True
        else:
            return False
    
    # A valid number should have at least one digit
    return has_digit

# Example usage and tests:
test_cases = ["13", "3.0", "-7.4", "-13.5", "abc", "123a", "-.", "-..---.", "1.0.0.1"]
results = [is_valid_number(tc) for tc in test_cases]
expected_results = [True, True, True, True, False, False, False, False, False]

print("Results:", results)
print("Expected:", expected_results)

'''
Explanation:

	1.	Minus sign handling: If the string starts with a minus sign, it’s removed for further checks, as the minus sign is valid only at the start.
	2.	Dot and digit tracking: We maintain two flags (has_dot and has_digit) to track the occurrence of a decimal point and at least one digit, respectively.
	3.	Loop through the string: We loop through each character in the string:
	•	If it’s a digit, we mark has_digit as True.
	•	If it’s a decimal point:
	•	If we have already encountered a decimal point, the string is invalid, so return False.
	•	Otherwise, mark has_dot as True.
	•	If it’s any other character, return False because it’s invalid.
	4.	Final Check: After the loop, if there is at least one digit, the string is valid.

Time Complexity:

	•	O(n): The function checks each character in the string once, where n is the length of the string.

Space Complexity:

	•	O(1): The function uses a constant amount of extra space, regardless of the input size.

This approach ensures that the function handles very long strings efficiently without relying on built-in functions that could overflow or lose precision.

'''

