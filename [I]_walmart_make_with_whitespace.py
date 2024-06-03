def segment(text):
    n = len(text)
    # dp[i] will store the maximum probability of the first i characters
    dp = [0] * (n + 1)
    # backpointer to reconstruct the best segmentation
    backpointer = [0] * (n + 1)
    dp[0] = 1  # Probability of an empty string

    for i in range(1, n + 1):
        for j in range(i):
            word = text[j:i]
            if word in WORD_COUNTS:
                prob = dp[j] * P(word)
                if prob > dp[i]:
                    dp[i] = prob
                    backpointer[i] = j

    # Reconstruct the best segmentation
    segments = []
    i = n
    while i > 0:
        j = backpointer[i]
        segments.append(text[j:i])
        i = j

    segments.reverse()
    return ' '.join(segments)

# Example usage
text = "thisisatest"
segmented_text = segment(text)
print("Segmented Text:", segmented_text)
