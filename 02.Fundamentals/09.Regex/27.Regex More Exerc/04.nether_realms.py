"""
You are assigned to sign in all the participants in the nether realm's mighty battle's demon book,
which of course is sorted alphabetically.
A demon's name contains his health and his damage.
The sum of the ASCII codes of all characters (excluding numbers (0-9), arithmetic symbols ('+', '-', '*', '/')
and delimiter dot ('.')) gives a demon's total health.
The sum of all numbers in his name forms his base damage.
Note that you should consider the plus '+' and minus '-' signs (e.g. +10 is 10 and -10 is -10).
However, there are some symbols ('*' and '/') that can further alter the base damage by
 multiplying or dividing it by 2 (e.g. in the name "m15*/c-5.0", the base damage is 15 + (-5.0) = 10
 and then you need to multiply it by 2 (e.g. 10 * 2 = 20) and then divide it by 2 (e.g. 20 / 2 = 10)).
So, multiplication and division are applied only after all numbers are included in the calculation
and in the order they appear in the name.
You will get all demons on a single line, separated by commas and zero or more blank spaces.
Sort them in alphabetical order and print their names along their health and damage.
Input
The input will be read from the console. The input consists of a single line containing all demon names
separated by commas and zero or more spaces in the format: "{demon name}, {demon name}, … {demon name}"
Output
Print all demons sorted by their name in ascending order, each on a separate line in the format:
"{demon name} - {health points} health, {damage points} damage"
Constraints
A demon's name will contain at least one character
A demon's name cannot contain blank spaces ' ' or commas ','
A floating point number will always have digits before and after its decimal separator
Number in a demon's name is considered everything that is a valid integer or floating point number (with dot '.' used as separator).
For example, all these are valid numbers: '4', '+4', '-4', '3.5', '+3.5', '-3.5'
"""
import re

inp_str = input().split(", ")
health_pattern = r"[^\d+*/.-]"
numbers_pattern = r"[+-]?\d(\.\d+)?"
signs_pattern = r"[*/]"

demons = {}

for demon_str in inp_str:
    demons[demon_str] = []

    demon_health = 0
    demon_dmg = 0

    # calculating demon's health
    demon_health_lst = re.findall(health_pattern, demon_str)
    for ch in demon_health_lst:
        demon_health += ord(ch)
    # adding health to demons dict on loc 0
    demons[demon_str].append(demon_health)

    # calculating demon's basic damage
    demon_dmg_lst = re.finditer(numbers_pattern, demon_str)
    for char in demon_dmg_lst:
        demon_dmg += float(char.group())
    # calculating demon's final damage if there are `*` or `/` signs
    signs_list = re.findall(signs_pattern, demon_str)
    if signs_list:
        for sign in signs_list:
            if sign == "*":
                demon_dmg *= 2
            elif sign == "/":
                demon_dmg /= 2
    demons[demon_str].append(demon_dmg)

sorted_demons = dict(sorted(demons.items(), key=lambda kvp: kvp[0]))
for demon, stats in sorted_demons.items():
    print(f"{demon} - {stats[0]} health, {stats[1]:.2f} damage")
