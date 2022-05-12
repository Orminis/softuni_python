# word = input()
# reversed_word = ""
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

##############################################
word = input()
rev_word = [x for x in word[::-1]]
print(list(rev_word))
