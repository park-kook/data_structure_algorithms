def uni_char2(s):
    chars = set()
    for let in s:
#        if let in chars:
#            return False
#        else:
#            chars.add(let)
        if let not in chars:
            chars.add(let)
            
        else:
            return False
    return True
uni_char2('aabcde')
uni_char2('abcde')
