"""
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line
"""

# substrings = input().split(", ")
# words = input().split(", ")
#
# occ_substrings = []
#
# for substr in substrings:
#     for word in words:
#         if substr in word:
#             occ_substrings.append(substr)
#
# print(sorted(set(occ_substrings), key=substrings.index))

################## With Comprehension ###################

substrings = input().split(", ")
words = input().split(", ")

occ_substrings = [substr for substr in substrings for word in words if substr in word]
print(sorted(set(occ_substrings), key=substrings.index))

