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
