count = int(input())

parking = {}

for _ in range(count):
    split_data = input().split()

    if split_data[0] == "register":
        username, license = split_data[1], split_data[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license}")
        else:
            parking[username] = license
            print(f"{username} registered {license} successfully")
    elif split_data[0] == "unregister":
        username = split_data[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            # del parking[username]
            parking.pop(username)
            print(f"{username} unregistered successfully")

for k, v in parking.items():
    print(f"{k} => {v}")
