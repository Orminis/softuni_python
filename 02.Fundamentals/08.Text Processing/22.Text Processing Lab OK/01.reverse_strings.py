word = input()

while not word == "end":
    print(f"{word} = {word[::-1]}")

    word = input()

#####################################

# word = input()
# while not word == "end":
#     text_reversed = ""
#     for i in reversed(word):
#         text_reversed += i
#
#     print(f"{word} = {text_reversed}")
#
#     word = input()
#
#
# ######################################
#
# word = input()
# while not word == "end":
#     text_reversed = ""
#     for index in range(len(word)-1, -1, -1):
#         text_reversed += word[index]
#
#     print(f"{word} = {text_reversed}")
#
#     word = input()
