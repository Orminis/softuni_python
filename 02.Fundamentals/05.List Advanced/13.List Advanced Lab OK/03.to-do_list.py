# notes = [0] * 10
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split("-")
#     priority = int(tokens[0])
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# result = [el for el in notes if el != 0]
# print(result)

##################################################################

notes = input()

to_do_list = [0] * 10
while not notes == "End":
    importance, task = notes.split("-")
    importance = int(importance) - 1
    to_do_list[importance] = task
    notes = input()

print([task for task in to_do_list if not task == 0])



# По този начин priority взима 0вия индекс а note 1вия индекс.
# Трите реда могат да се заменят с горният ред.