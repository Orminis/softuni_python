# Write a program that receives a single integer number and prints different messages depending on the number:
# -If the number is 88 - "Leo finally won the Oscar! Leo is happy".
# -If the number is 86 - "Not even for Wolf of Wall Street?!"
# -If the number is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
# -If the number is over 88 - "Leo got one already!"

number = int(input())

if number <= 87:
    if number == 86:
        print("Not even for Wolf of Wall Street?!")
    else:
        print("When will you give Leo an Oscar?")
elif number > 87:
    if number == 88:
        print("Leo finally won the Oscar! Leo is happy")
    else:
        print("Leo got one already!")