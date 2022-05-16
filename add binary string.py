
'''
Add Binary
Given two binary strings a and b, return their sum as a binary string.
'''
def addBinary(a, b) -> str:
    return '{0:b}'.format(int(a, 2) + int(b, 2))

addBinary("11","1")
addBinary("1010","1011")

    def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #return '{0:b}'.format(int(a, 2) + int(b, 2))
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry = carry // 2
            #carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)
2%2 #0 mod residual
