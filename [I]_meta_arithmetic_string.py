
'''
Given a string representing an arithmetic expression consisting of non-negative integers, 
+, and *, return the result of evaluating the expression. The expression will follow the normal precedence rules, 
i.e., multiplication has higher precedence than addition.
'''


def evaluate_expression(expression):
    operands = []
    current_num = 0
    last_operator = '+'

    for char in expression + '+':  # Add a '+' to handle the last number in the expression
        if char.isdigit():
            current_num = current_num * 10 + int(char)
            #current_num =  int(char)
            print(current_num)
        else:
            if last_operator == '+':
                operands.append(current_num)
            elif last_operator == '*':
                operands[-1] *= current_num
            print(operands)

            last_operator = char
            current_num = 0

    return sum(operands)

# Example usage
expression = "2*3+4"
result = evaluate_expression(expression)
print(result)  # Output: 10
