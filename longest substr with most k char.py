
'''
Longest Substring with at most K distinct Characters

Given a string s and an integer k, return the length of the longest substring of s 
that contains at most k distinct characters.
'''
from collections import defaultdict
import collections
    def lengthOfLongestSubstringKDistinct(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if n * k == 0:
            return 0

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1

        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

lengthOfLongestSubstringKDistinct("eceba",2) #3 ece
lengthOfLongestSubstringKDistinct("aa",1) #2 aa
