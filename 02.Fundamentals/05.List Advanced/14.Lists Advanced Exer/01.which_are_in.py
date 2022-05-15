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

