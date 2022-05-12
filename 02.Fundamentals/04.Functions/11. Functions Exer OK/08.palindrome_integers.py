# [print(x == x[::-1]) for x in input().split(', ')]


############################################################

numbers = input().split(", ")


def is_palindrome(some_list):
    is_it_pal = []
    for element in some_list:
        if element == element[::-1]:
            is_it_pal.append("True")
        else:
            is_it_pal.append("False")
    return is_it_pal


result = is_palindrome(numbers)
print("\n".join(result))


##############################################################
