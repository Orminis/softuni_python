# [print(x == x[::-1]) for x in input().split(', ')]


############################################################
#Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

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
