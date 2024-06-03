
import re
from collections import Counter

# Function to tokenize words
def words(text):
    return re.findall(r'\w+', text.lower())

# Load words from a large corpus
def load_words():
    with open('big.txt') as f:
        return Counter(words(f.read()))

# Load the word counts
WORD_COUNTS = load_words()
TOTAL_WORDS = sum(WORD_COUNTS.values())

# Probability of a word
def P(word):
    return WORD_COUNTS[word] / TOTAL_WORDS

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


'''
backpointer

[0, 0, 0, 2, 0, 4, 4, 6, 6, 6, 9, 7]



dp
[1,
 0.0011814397429875546,
 8.96388272372955e-06,
 6.174185707370271e-08,
 0.003642025550651316,
 2.508571652904541e-05,
 3.190561005184289e-05,
 6.041424851604079e-07,
 1.9416414181755398e-07,
 6.005961081409092e-10,
 3.028854473515989e-12,
 2.8701950642622207e-11]

dp[1] = p('t')
dp[2] = p('th')
dp[3] = p('th') * ('i')
dp[4] = p('this') #0:4
dp[5] = p('this') * p('i') 
dp[6] = p('this') * p('is') #4:6
dp[7] = p('this') * p('is') * p('a') #6:7
dp[8] = p('this') * p('is') * p('at')
dp[9] = p('this') * p('is') * p('ate')
dp[10] = p('this') * p('is') * p('ate') *p('s')
dp[11] = p('this') * p('is') * p('a') * p('test') #7:11


'''
