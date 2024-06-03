import re
def words(text):
    return re.findall(r'\w+', text.lower())

from collections import Counter

# Assume 'big.txt' is a large text file with lots of correct words
def load_words():
    with open('big.txt') as f:
        return Counter(words(f.read()))

WORD_COUNTS = load_words()

def P(word, N=sum(WORD_COUNTS.values())):
    # Probability of `word`.
    return WORD_COUNTS[word] / N
def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces   = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts    = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def known(words):
    return set(w for w in words if w in WORD_COUNTS)

def candidates(word):
    return (known([word]) or
            known(edits1(word)) or
            [word])

def correct(word):
    return max(candidates(word), key=P)

# Example usage
search_query = "pythn programing tutrial"
corrected_query = ' '.join(correct(word) for word in search_query.split())
print("Corrected Query:", corrected_query)


Corrected Query: python programming tutorial
