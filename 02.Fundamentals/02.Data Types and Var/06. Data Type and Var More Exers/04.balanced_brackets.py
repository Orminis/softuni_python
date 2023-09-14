"""
On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
Opening bracket – "(",
Closing bracket – ")" or
Random string
Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one.
Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced.
You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
"""

n = int(input())
previous_bracket = ")"
is_balanced = True
for _ in range(n):
    data = input()
    if data == chr(40) or data == chr(41):
        if not previous_bracket == data:
            previous_bracket = data
        else:
            is_balanced = False
            print("UNBALANCED")
            break

if is_balanced:
    print("BALANCED")


#####################################################

lines = int(input())
balanced = []
counter_open = 0
counter_close = 0
is_balanced = False
for i in range(lines):
    line = input()
    if line in ["(", ")"]:
        balanced.append(line)
print(balanced)