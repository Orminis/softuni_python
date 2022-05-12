username = input()
password = input()
data = input()
while data != password:
    data = input()
else:                                   # data == password
    print(f"Welcome {username}!")
