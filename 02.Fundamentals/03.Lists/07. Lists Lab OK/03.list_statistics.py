# Creating a lists with positive and negative integers

n = int(input())    # Number of integers

positive_int_list = []
negative_int_list = []
positive_count = 0
negative_sum = 0


for i in range(n):
    new_integer = int(input())
    if new_integer >= 0:
        positive_int_list.append(new_integer)
        positive_count += 1
    else:
        negative_int_list.append(new_integer)
        negative_sum += new_integer

print(positive_int_list)
print(negative_int_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")

############################################################


n = int(input())    # Number of integers

positive_int_list = []
negative_int_list = []

for i in range(n):
    new_integer = int(input())
    if new_integer >= 0:
        positive_int_list.append(new_integer)
    else:
        negative_int_list.append(new_integer)

print(positive_int_list)
print(negative_int_list)
positive_count = len(positive_int_list)
negative_sum = sum(negative_int_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")