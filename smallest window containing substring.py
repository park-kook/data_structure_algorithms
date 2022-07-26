
'''
Smallest Window containing Substring (hard)
Given a string and a pattern, find the smallest substring in the given string 
which has all the character occurrences of the given pattern.
'''
c=""
a="abc"
c+=a[1]
c+=a[2]

c+=a[0]
c+=a[2]
c = c.replace(a[2],'',1)
c

str1="aabdec"
pattern="abc"
output = "abdec"

str1="aabdec"
pattern="abac"
output ="aabdec"

str1="abdbca"
pattern="abc"
output ="bca"

str1="adcad"
pattern="abc"
output =""

def find_substring(str1, pattern):
  # TODO: Write your code here
#  min_str = ""
  left = 0
  dict={}
  matched = 0
  substr_start =0
  min_length = len(str1)+1

  for p in range(len(pattern)):
    dict[pattern[p]] =1+ dict.get(pattern[p],0)
  for right in range(len(str1)):
    if str1[right] in dict:
      dict[str1[right]]-=1
      if dict[str1[right]] >=0:
        matched +=1
    while matched == len(dict):
        if min_length > right-left+1:
           min_length= right-left+1
           substr_start = left
            

        if str1[left] in dict: 
            if dict[str1[left]] ==0:
              matched-=1
            dict[str1[left]]+=1
        left+=1
  if min_length > len(str1):
      return ""
    
  return str1[substr_start:substr_start+min_length]

str1="aabdec"
pattern="abc"
output = "abdec"
find_substring(str1, pattern)
