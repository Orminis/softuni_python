"""
You will be given a number n representing the number of rows of the field.
On the following n lines, you will receive each field row as a string with numbers separated by a space.
Each number greater than zero represents a ship with health equal to the number value.
After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed
"""

row_num = int(input())
battlefield = []

for r in range(row_num):
    row = [int(x) for x in input().split(' ')]
    battlefield.append(row)

attacks = [x for x in input().split(' ')]
sunken_ships = 0

for _ in range(len(attacks)):
    attack_row, attack_col = [int(x) for x in attacks[0].split("-")]
    if not battlefield[attack_row][attack_col] == 0:
        # then there is a ship let sunk it.
        battlefield[attack_row][attack_col] -= 1
        if battlefield[attack_row][attack_col] == 0:
            sunken_ships += 1
    attacks.pop(0)

print(sunken_ships)