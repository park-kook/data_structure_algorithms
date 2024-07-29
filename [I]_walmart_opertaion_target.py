def can_reach_target(input_list, target):
    def backtrack(index, current_value):
        if index == len(input_list):
            return current_value == target
        # Try both addition and multiplication
        return (backtrack(index + 1, current_value + input_list[index]) or
                backtrack(index + 1, current_value * input_list[index]))

    # Edge case for an empty input list
    if not input_list:
        return target == 0
    # Start backtracking from the first element
    return backtrack(1, input_list[0])

# Example usage:
input_list = [1, 2, 3]
target = 6
print(can_reach_target(input_list, target))  # Output: True

input_list = [1, 2, 3]
target = 7
print(can_reach_target(input_list, target))  # Output: False

input_list = [1, 2, 3]
target = 9
print(can_reach_target(input_list, target))  # Output: True
