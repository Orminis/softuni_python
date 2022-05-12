n = int(input())                        #input number of how many lines with information will be input next

list_courses = []                       #empty list to be filled

for i in range(n):
    courses = input()                   #inputing information
    list_courses.append(courses)        #adding the information to the list

print(list_courses)