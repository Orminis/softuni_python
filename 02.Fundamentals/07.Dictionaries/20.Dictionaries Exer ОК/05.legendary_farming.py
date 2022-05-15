# found_materials = input()
#
# legendary_weapons = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
#
# materials_storage = {"shards": 0, "fragments": 0, "motes": 0}
# others = {}
#
# is_obtained = False
#
# while not is_obtained:
#     split_found_materials = found_materials.split()
#
#     for index in range(0, len(split_found_materials), 2):
#         if is_obtained:
#             break
#         quantity = int(split_found_materials[index])
#         material = split_found_materials[index + 1].lower()
#
#         if material in materials_storage:
#             materials_storage[material] += quantity
#         else:
#             if material not in others:
#                 others[material] = quantity
#             else:
#                 others[material] += quantity
#
#         for material, quantity in materials_storage.items():
#             if quantity >= 250:
#                 is_obtained = True
#                 materials_storage[material] -= 250
#                 print(f"{legendary_weapons[material]} obtained!")
#                 break
#
#     if is_obtained:
#         break
#
#     found_materials = input()
#
# # sorted_items = sorted(materials_storage.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
# for material, quantity in materials_storage.items():
#     print(f"{material}: {quantity}")
#
# # sorted_other_items = sorted(others.items(), key=lambda kvpt: kvpt[0])
# for other, quantity in others.items():
#     print(f"{other}: {quantity}")


materials = input()

legendary_weapons = {"Shadowmourne": {"shards": 0}, "Valanyr": {"fragments": 0}, "Dragonwrath": {"motes": 0}}
others = {}
mats_list = ["shards", "fragments", "motes"]
is_obtained = False

while not is_obtained:
    split_materials = materials.split()

    for idx in range(0, len(split_materials), 2):
        if is_obtained:
            break
        quantity = int(split_materials[idx])
        material = split_materials[idx + 1].lower()

        if material not in mats_list:
            if material not in others:
                others[material] = 0
            others[material] += quantity
        else:
            for weapon in legendary_weapons:
                if material in legendary_weapons[weapon]:
                    legendary_weapons[weapon][material] += quantity
                    if legendary_weapons[weapon][material] >= 250:
                        is_obtained = True
                        legendary_weapons[weapon][material] -= 250
                        print(f"{weapon} obtained!")
                        break
    if is_obtained:
        break

    materials = input()

for weapon, materials in legendary_weapons.items():
    for mats, quantity in materials.items():
        print(f"{mats}: {quantity}")
for junk, quantity in others.items():
    print(f"{junk}: {quantity}")

