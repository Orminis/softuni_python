import sys

n = int(input())   # Number of numerals to be checked

odd_sum = 0                     #total sum of numbers on odd places
odd_sum_min = sys.maxsize       #minimum number on odd places
odd_sum_max = -sys.maxsize      #Max number on odd places
even_sum = 0                    #total sum of numbers on even plaes
even_sum_min = sys.maxsize      #min number on even place
even_sum_max = -sys.maxsize     #max number on even place

for i in range (1, n + 1):
    if i % 2 != 0:                  #check for odd place
        num = float(input())        #num on odd place
        odd_sum += num              #increasing of total sum of numbers on odd places
        if num < odd_sum_min:       #check for min and max number on odd places
            odd_sum_min = num
        if num > odd_sum_max:
            odd_sum_max = num

    elif i % 2 == 0:                #even place
        num = float(input())        #num on even places
        even_sum += num             #increasing of total sum of numbers on even places
        if num < even_sum_min:      #check for min and max number on even places
            even_sum_min = num
        if num > even_sum_max:
            even_sum_max = num


print(f"OddSum={odd_sum:.2f},")
if odd_sum_min != sys.maxsize:
    print(f"OddMin={odd_sum_min:.2f},")
else:
    print(f"OddMin=No,")
if odd_sum_max != -sys.maxsize:
    print(f"OddMax={odd_sum_max:.2f},")
else:
    print(f"OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
if even_sum_min != sys.maxsize:
    print(f"EvenMin={even_sum_min:.2f},")
else:
    print(f"EvenMin=No,")
if even_sum_max != -sys.maxsize:
    print(f"EvenMax={even_sum_max:.2f}")
else:
    print(f"EvenMax=No")
