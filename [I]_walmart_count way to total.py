def count_ways_to_total(total, k):
    # Create a list for dp where dp[i] will be the number of ways to sum up to weight i
    dp = [0] * (total + 1)
    # There is one way to make the sum of 0, which is using no weights at all
    dp[0] = 1
    
    # Process each possible item weight from 1 to k
    for weight in range(1, k + 1):
        # Update dp values for all sums that can include this weight
        for i in range(weight, total + 1):
            dp[i] += dp[i - weight]
    
    return dp[total]

# Example usage:
result = count_ways_to_total(10, 3)  # Calculate number of ways to sum up to 10 using weights 1 to 3
print(result)