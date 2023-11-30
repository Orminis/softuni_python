"""
Write a program which finds how many times a given word is used in each sentence.
Note that letter case does not matter – it is case-insensitive.
The output is a single number indicating the number of times the sentence contains the word.
Example:
    The waterfall was so high, that the child couldn't see its peak.
    the
Output:
    2
"""

import re

sentence = input()
searched_word = input()
# Can be used .lower() or flags=re.IGNORECASE to lower letters.
# sentence = input().lower()
# # searched_word = input().lower()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, sentence, flags=re.IGNORECASE)    # flags=re.I = IGNORECASE

print(len(matches))