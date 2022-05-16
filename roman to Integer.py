
Roman to Integer

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

'''
def romanToInt(s):
    #s=str(s)
    MathchDic = {"I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000}
    exceptDict = {"IV":4,
                  "IX":9,
                  "XL":40,
                  "XC":90,
                  "CD":400,
                  "CM":900}
    sumint=[]
    rmstr=[]
    
    for k,v in exceptDict.items():
        if k in s:
            sumint.append(v)
            rmstr.append(k)
    for v in rmstr:
        s=s.replace(v,'')
        
    spliunm = [MatchDic.get(d) for d in s] #dictionary.get(keyname, value)
    return sum(spliunm)+sum(sumint)

romanToInt('IV')

s='IV'
