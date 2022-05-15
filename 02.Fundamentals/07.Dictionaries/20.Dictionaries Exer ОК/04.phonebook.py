
data = input()
phonebook = {}

while len(data) > 1:

    name, phone = data.split("-")
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name] = phone

    data = input()

data = int(data)

for d in range(data):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

