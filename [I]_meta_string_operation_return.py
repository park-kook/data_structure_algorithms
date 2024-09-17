'''
Problem Statement

Given a string representing an arithmetic expression consisting of non-negative integers,
+, and *, return the result of evaluating the expression. 
The expression will follow the normal precedence rules, i.e., 
multiplication has higher precedence than addition.

given a string representing an aithmetic expression with only addition and multiplicatiion operations, 
return the result of the calculation. 2*3 + 4 return 10

'''

def evaluate_expression(expression):
    operands = []
    current_num = 0
    last_operator = '+'

    for char in expression + '+':  # Add a '+' to handle the last number in the expression
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            if last_operator == '+':
                operands.append(current_num)
            elif last_operator == '*':
                operands[-1] *= current_num

            last_operator = char
            current_num = 0

    return sum(operands)


'''
Explanation

	1.	Initialization:
	•	operands: List to store the results of the evaluated parts of the expression.
	•	current_num: The current number being processed.
	•	last_operator: Keeps track of the last operator encountered.
	2.	Iteration:
	•	We iterate over each character in the expression, treating it as a digit or an operator.
	•	If it’s a digit, we build the current number.
	•	If it’s an operator (+ or *), we evaluate the expression based on the last operator encountered:
	•	If last_operator is +, we add current_num to operands.
	•	If last_operator is *, we multiply the last number in operands by current_num.
	3.	Final Calculation:
	•	After iterating through the expression, we sum up the numbers in operands to get the final result.

Time Complexity

	•	O(n): The code iterates over each character in the expression once, 
 making the time complexity O(n), where n is the length of the expression.

Space Complexity

	•	O(n): The space complexity is O(n) because the list operands may store all 
 numbers from the expression in the worst case.

This simplified version of the code is straightforward, avoiding any unnecessary 
complexity while ensuring that the operations are evaluated with the correct precedence.

'''
