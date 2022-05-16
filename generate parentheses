'''
backtrack problem
Generate Parentheses
Given n paris of parentheses, write a fucntion to generate all combinations of well-formed parentheses. 
note: condition: 
    1) n = open = closed
    2) closeN <  openN
    3) n > openN

'''
input = 3
output = ["((()))", "(()())", "(())()","()(())","()()()"]
def generateParenthesis(n):
    stack = []
    res = []
    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return 
        if openN <n:
            stack.append("(")
            backtrack(openN+1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN +1)
            stack.pop()
    backtrack(0,0)
    return res

generateParenthesis(3)

##############
