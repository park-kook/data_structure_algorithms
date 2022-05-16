
'''
Valid Palindrome (a word, phrase, sentence, or number that reas the same backward or forward )
Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.
'''
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        filtered_chars = list(filter(lambda ch: ch.isalnum(), s)) #isalnum method returns true if all 
        #characters in the sting are alphanumeric (either alphabets or numbers), if not it returns False
        lowercase_filtered_chars = list(map(lambda ch: ch.lower(), filtered_chars))

        filtered_chars_list = lowercase_filtered_chars
        
        reversed_chars_list = []
        index = len(filtered_chars_list)

        while index:
            index -= 1                 
        #new_string += words[index] # new_string = new_string + character
            reversed_chars_list.append(filtered_chars_list[index]) 
        #reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
    
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)

   
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
    
isPalindrome("A man, a plan, a canal: Panama")  
isPalindrome("race a car")  
s="A man, a plan, a canal: Panama"



'''
Valid Palindrome II
Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.
'''


def validPalindrome(s: str, n=0) -> bool:

        rev=s[::-1]
        i=0

        while i<len(s):
            if s[i]==rev[i]:
                i+=1
                #continue
            else:
                break
        cut=s[:i]+s[i+1:]
        # print(s)
        rev=cut[::-1]
        if cut==rev:
            return True
        newcut=s[:len(s)-i-1]+s[len(s)-i:]
        # print(newcut)
        rev2=newcut[::-1]
        if newcut==rev2:
            return True
        else: 
            return False
    
def validPalindrome(s: str, n=0) -> bool:   
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
        return True
    
    
for i in range(0, int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
        print(False)
    else: 
        print(True)    
s="abca"
s[1] == s[2]
s[2]
int(len(s)/2)
validPalindrome("aba")
validPalindrome("abca")
validPalindrome("abc")
validPalindrome("abcda")
validPalindrome("aacba")
validPalindrome("abcdba")
validPalindrome("cbbcc")
