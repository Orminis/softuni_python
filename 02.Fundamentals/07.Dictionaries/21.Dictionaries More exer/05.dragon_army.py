"""
You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats (damage, health, and armor).
Type is preserved as in the order of input, but dragons are sorted alphabetically by their name.

For each type, you should also print the average damage, health, and armor of the dragons.
For each dragon, print his own stats.

There may be missing stats in the input, though.
If a stat is missing you should assign it default values.
Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".

The input is in the following format "{type} {name} {damage} {health} {armor}".
The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers.
Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
If the same dragon is added a second time, the new stats should overwrite the previous ones.
Two dragons are considered equal if they match by both name and type.

Input
    On the first line, you are given number N -> the number of dragons to follow
    On the next N lines, you are given input in the above-described format. There will be a single space separating each element.
Output
    Print the aggregated data on the console
    For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})"
    Damage, health, and armor should be rounded to two digits after the decimal separator
    For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}"


"""
class Dragon:
    _DEFAULT_DMG = 45
    _DEFAULT_HP = 250
    _DEFAULT_ARM = 10
    def __init__(self, typee: str, namee: str, dmg, hp, arm):
        self.type = typee
        self.name = namee
        self.damage = dmg if dmg != "null" else self._DEFAULT_DMG
        self.health = hp if hp != "null" else self._DEFAULT_HP
        self.armor = arm if arm != "null" else self._DEFAULT_ARM

    def __str__(self):
        return f"-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}"

    def __repr__(self):
        return self.name


num_of_dragons = int(input())

dragons = {}                    # Example: {Red: [Argo, Sylvanas, Erixtraza], Black: [Deathwing], ... Orange: [Garfield]}

for _ in range(num_of_dragons):
    tpe, name, damage, health, armor = input().split()

    dragon = Dragon(tpe, name, damage, health, armor)
    if tpe not in dragons:
        dragons[tpe] = [dragon]
    else:
        for idx, drg in enumerate(dragons[tpe]):
            if drg.name == name:
                dragons[tpe].pop(idx)
        dragons[tpe].append(dragon)

for typ, drgs_info in dragons.items():
    drg_hp = sum([int(drg.health) for drg in drgs_info])
    drg_dmg = sum([int(drg.damage) for drg in drgs_info])
    drg_arm = sum([int(drg.armor) for drg in drgs_info])
    print(f"{typ}::"
          f"({drg_dmg/len(drgs_info):.2f}/"
          f"{drg_hp/len(drgs_info):.2f}/"
          f"{drg_arm/len(drgs_info):.2f})")
    drgs = sorted([drg for drg in drgs_info], key=lambda x: x.name)
    for drg_name in drgs:
        print(drg_name)
