"""
You will be receiving several input lines which contain data about each dwarf in the following format:
    {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.

You must store the data about the dwarfs in your program. There are several rules though:
    If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store them both.
    If 2 dwarfs have the same name and the same color, store the one with the higher physics.

When you receive the command "Once upon a time", the input ends.
You must order the dwarfs by physics in descending order and then by total count of dwarfs with the same hat color in descending order.

Then you must print them all.
    Input
        The input will consist of several input lines, containing dwarf data in the format, specified above.
        The input ends when you receive the command "Once upon a time".
    Output
        As output, you must print the dwarfs, ordered in the way, specified above.
        The output format is: "({hat_color}) {name} <-> {physics}"
    Constraints
        The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
        The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
        The "dwarf_physics" will be an integer in range [0, 231 – 1].
        There will be no invalid input lines.
        If all sorting criteria fail, the order should be by order of input.
"""

def add_dwarf_physics_dict(phys_dict, physics, hat_c, name):
    if physics not in dwarf_phys_dict.keys():
        phys_dict[physics] = {hat_c: [name]}
    else:
        if hat_c not in phys_dict[physics]:
            phys_dict[physics][hat_c] = [name]
        else:
            phys_dict[physics][hat_c].append(name)


def update_dwarf_physics_dict(phys_dict, physics, hat_c, name, old_phys):
    # remove old phys
    if len(phys_dict[old_phys]) > 1:
        for v in phys_dict[old_phys].values():
            if v == name:
                phys_dict[old_phys][hat_c].remove(name)
    else:
        del phys_dict[old_phys]

    # adding new phys
    add_dwarf_physics_dict(phys_dict, physics, hat_c, name)


command_input = input()

dwarf_dict = {}         # `Red: Ivan: 10000, George: 10000`; `Blue: Ivan: 5000 `

dwarf_phys_dict = {}     # `10000: Red: [Ivan, George]` ; `5000: Blue: [Ivan]`

while not command_input == "Once upon a time":
    dwarf_name, hat_color, dwarf_physics = command_input.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if hat_color not in dwarf_dict.keys():
        dwarf_dict[hat_color] = {dwarf_name: dwarf_physics}
        add_dwarf_physics_dict(dwarf_phys_dict, dwarf_physics, hat_color, dwarf_name)

    elif hat_color in dwarf_dict.keys():
        if dwarf_name not in dwarf_dict[hat_color]:
            dwarf_dict[hat_color][dwarf_name] = dwarf_physics
            add_dwarf_physics_dict(dwarf_phys_dict, dwarf_physics, hat_color, dwarf_name)

        elif dwarf_physics > dwarf_dict[hat_color][dwarf_name]:
            old_physic = dwarf_dict[hat_color][dwarf_name]
            dwarf_dict[hat_color][dwarf_name] = dwarf_physics
            update_dwarf_physics_dict(dwarf_phys_dict, dwarf_physics, hat_color, dwarf_name, old_physic)
    command_input = input()

sort_list = []
for hat, d_info in dwarf_dict.items():
    for name, physic in d_info.items():
        sort_list.append((hat, name, physic))

sort_list.sort(key=lambda x: x[-1], reverse=True)


# for hat, name, physic  in sort_list:
#     print(f"({hat}) {name} <-> {physic}")