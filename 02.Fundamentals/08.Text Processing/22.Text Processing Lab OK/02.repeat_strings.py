# string = input()
#
# if len(string) > 1:
#     string_split = string.split()
#     for i in string_split:
#         print(i * len(i), end="")
# else:
#     print(string * len(string))

###############################

# string = input().split()
#
# for word in string:
#     print(word * len(word), end="")

#################################

# print(f"{''.join([word * len(word) for word in input().split()])}")


# list1 = [print(el*len(el), end='') for el in input().split()]


print(f"{''.join(map(lambda x: x * len(x), input().split()))}")

