n = int(input())       # How many lines of numbers will be given

list_of_numbers = []

for i in range(n):
    number = int(input())
    list_of_numbers.append(number)

command = input()

filtered = []
for num in list_of_numbers:
    if command == "even" and num % 2 == 0:
        filtered.append(num)
    elif command == 'odd' and num % 2 != 0:
        filtered.append(num)
    elif command == 'negative' and num < 0:
        filtered.append(num)
    elif command == 'positive' and num >= 0:
        filtered.append(num)

print(filtered)


#################################################################################
n = int(input())       # How many lines of numbers will be given

list_of_numbers = []

for i in range(n):
    number = int(input())
    list_of_numbers.append(number)

command = input()

filtered = []
for num in list_of_numbers:
    if (command == "even" and num % 2 == 0) \
            or (command == 'odd' and num % 2 != 0) \
            or (command == 'negative' and num < 0) \
            or (command == 'positive' and num >= 0):

        filtered.append(num)

print(filtered)

####################################################################################

n = int(input())       # How many lines of numbers will be given

list_of_numbers = []

for i in range(n):
    number = int(input())
    list_of_numbers.append(number)

command = input()
filtered = []
is_even = command == 'even'
is_odd = command == 'odd'
is_neative = command == 'negative'
is_positive = command == 'positive'
function = None

for num in list_of_numbers:
    if function(num):
        filtered.append(num)

print(filtered)