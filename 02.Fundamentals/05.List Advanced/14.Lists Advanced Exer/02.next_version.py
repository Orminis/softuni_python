"""
You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9.
If it happens, set the current number to 0 and increase the previous number.

Note: there will be no case in which the first number will become greater than 9.
"""

# version_number = [int(i) for i in input().split(".")]
#
# if version_number[2] + 1 > 9:
#     version_number[2] = 0
#     version_number[1] += 1
#     if version_number[1] + 1 > 9:
#         version_number[1] = 0
#         if version_number[0] < 9:
#             version_number[0] += 1
# else:
#     version_number[2] += 1
#
# temp = list(map(str, version_number))
# res = ".".join(temp)
# print(res)
# not ok 80/100

########################################################

version_as_list = input().split(".")
version_as_int = int("".join(version_as_list)) + 1
new_version = list(str(version_as_int))
print(".".join(new_version))
