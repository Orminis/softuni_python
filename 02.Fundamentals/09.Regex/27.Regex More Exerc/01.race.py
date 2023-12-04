"""
Write a program that processes information about a race.
On the first line you will be given list of participants separated by ", ".
On the next few lines until you receive a line "end of race" you will be given some info which will be some alphanumeric characters.
In between them you could have some extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e".
The letters are the name of the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km.
Store the information about the person only if the list of racers contains the name of the person.
If you receive the same person more than once just add the distance to his old distance.
At the end print the top 3 racers ordered by distance in descending in the format:
"1st place: {first racer}
2nd place: {second racer}
3rd place: {third racer}"
"""
import re
# preparing dictionary for participants where can be input the distance for each runner
participants_dict = {x: 0 for x in input().split(', ')}

# regex to take all letters from the string
pattern_letters = r"[A-Za-z]"
# regex to take all numbers from the string
pattern_nums = r"\d"

given_string = input()

while not given_string == 'end of race':
    # finding all letters in the string to make name
    name = re.findall(pattern_letters, given_string)
    name = ''.join(name)

    if name in participants_dict:
        # finding numbers for the participants who are in the `participant_dict`
        nums_list = re.findall(pattern_nums, given_string)
        nums_list = sum(int(x) for x in nums_list)
        participants_dict[name] += nums_list
    # continuing with next participant in the race
    given_string = input()

# ordering by distance in desc
ordered_participants_list = sorted(participants_dict.items(), key=lambda kvp: -kvp[1])
print(f"1st place: {ordered_participants_list[0][0]}\n"
      f"2nd place: {ordered_participants_list[1][0]}\n"
      f"3rd place: {ordered_participants_list[2][0]}")
