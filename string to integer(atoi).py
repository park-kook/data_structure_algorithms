
'''
String to integer(atoi)

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively.
 Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit charcter or the end of the input is reached. 
The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, 
then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], then clamp the integer 
so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, 
and integers greater than 2**31 - 1 should be clamped to 2**31 - 1.
6. Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

  
#############################
    def myAtoi(s: str) -> int:
        result = ''
        sign = 1
        index = 0
        while index < len(s) and s[index] == ' ':
            index += 1
        if index < len(s):
            if s[index] == '+':
                index += 1
            elif s[index] == '-':
                sign = -1
                index += 1
        for i in range(index,len(s)):
            if s[i].isdigit():
                result += s[i]
                i += 1
            else:
                break
        if result =='':
            return 0
        result = sign * int(result)
        if result>2**31-1:
            return 2**31-1
        elif result<(-2**31):
            return -2**31
        else:
            return result

    
myAtoi("42")
myAtoi("   -42")
myAtoi("4193 with words")
myAtoi("words and 987")
myAtoi("-91283472332")


'''
#################################
    def myAtoi(s: str) -> int:
        s = s.strip() #remove every whitespace. 
        num, i, sign, n = 0, 0, 1, len(s)
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            i+=1
        if s[0] == '+':
            i+=1
            
        while i < n:
            dg = ord(s[i]) - ord('0')
            if dg >= 0 and dg <= 9:
                num = (num*10) + dg
            else:
                break #terminate the current loop and resumes execution at the next statement. 
            i+=1
        num = sign * num
        if num < -(2**31):
            return -(2**31)
        if num > (2**31) -1:
            return (2**31) -1
        return num
  
