# Given a n-number of strings. To print 2 lists: first with all given strings and second list with the given word only

# n = int(input())
# specific_word = input()
# full_list = []
# specific_word_list = []
#
# for i in range(n):
#     new_string = input()
#     full_list.append(new_string)
#     if specific_word in new_string:
#         specific_word_list.append(new_string)
#
# print(full_list)
# print(specific_word_list)




n = int(input())
specific_word = input()
list = []

for i in range(n):
    list.append(input())
print(list)

for x in range(len(list) - 1, -1, -1):
    element = list[x]
    if specific_word not in element:
        list.remove(element)
print(list)
