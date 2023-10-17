"""
You will receive a string with even integers, separated by a "@" - this is our neighborhood.
After that, a series of Jump commands will follow until you receive "Love!".
Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's Day.
The integers in the neighborhood indicate those needed hearts.
Cupid starts at the position of the first house (index 0) and must jump by a given length.
The jump commands will be in this format: "Jump {length}".
Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day."
If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it, he should start from the first house again (index 0)

10@10@10@2
Jump 1
Jump 2
Love!
"""

neighbourhood = [int(x) for x in input().split("@")]
cupid_pos = 0
commands = input()
while commands != "Love!":
    command = commands.split()
    action, step = command[0], int(command[1])

    cupid_pos += step
    if cupid_pos >= len(neighbourhood):
        cupid_pos = 0
    if neighbourhood[cupid_pos] - 2 >= 0:
        new_heart_val = neighbourhood[cupid_pos] - 2
        neighbourhood.pop(cupid_pos)
        neighbourhood.insert(cupid_pos, new_heart_val)
        if neighbourhood[cupid_pos] == 0:
            print(f"Place {cupid_pos} has Valentine's day.")
    elif neighbourhood[cupid_pos] - 2 < 0:
        print(f"Place {cupid_pos} already had Valentine's day.")
    commands = input()

print(f"Cupid's last position was {cupid_pos}.")

if all([x == 0 for x in neighbourhood]):
    print("Mission was successful.")
else:
    failed_pos = len([x for x in neighbourhood if not x == 0])
    print(f"Cupid has failed {failed_pos} places.")