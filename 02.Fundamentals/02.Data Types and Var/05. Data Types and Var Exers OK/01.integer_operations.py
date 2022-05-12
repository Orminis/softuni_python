# Four numbers will be input. 1st and 2nd will be add to each other \
# then divided by the 3rd and finally multiply by 4th number.

n1_to_add = int(input())
n2_to_add = int(input())
n3_to_divide = int(input())
n4_to_multiply = int(input())

final_number = int((n1_to_add + n2_to_add) / n3_to_divide ) * n4_to_multiply
print(final_number)
