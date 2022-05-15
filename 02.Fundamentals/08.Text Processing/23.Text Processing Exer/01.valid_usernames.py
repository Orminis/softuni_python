# usernames = input().split(", ")
# list_of_usernames = []
# is_username = True
# for username in usernames:
#     if 3 <= len(username) <= 16:
#         for char in username:
#             if not (char == '-' or char == '_' or char.isalnum()):
#                 is_username = False
#             if char == " ":
#                 is_username = False
#         if is_username:
#             list_of_usernames.append(username)
#     is_username = True
# print("\n".join(list_of_usernames))
#
# ##########################################
#
# usernames = input().split(', ')
#
# for word in usernames:
#     if 3 <= len(word) <= 16 and all(c.isalnum() or c == '_' or c == '-' for c in word):
#         print(word)
#
def is_valid_char(char):
    if char == "-" or char == "_" or char.isallnum():
        return True

usernames = input().split(", ")
for username in usernames:
    is_username = False
    if 3 <= len(username) <= 16:
        if all(is_valid_char(char) for char in username):
            is_username = True
    if is_username:
        print(username)