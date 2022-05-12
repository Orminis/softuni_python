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