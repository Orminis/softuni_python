"""
Write a program which decrypts a message by a given key and gathers information about hidden treasure type and its coordinates.
On the first line you will receive a key (sequence of numbers separated by a space).
 On the next few lines until you receive "find" you will get lines of strings.
 You should loop through every string and decrease the ascii code of each character with a corresponding number of the key sequence.
 The way you choose a key number from the sequence is just looping through it.
 If the length of the key sequence is less than the string sequence, you start looping from the beginning of the key.
 For more clarification see the example below.

 After decrypting the message, you will get a type of treasure and its coordinates.
 The type will be between the symbol "&" and the coordinates will be between the symbols '<' and '>'.
 For each line print the type and the coordinates in the format "Found {type} at {coordinates}".

Example:
```
1 2 1 3
ikegfp'jpne)bv=41P83X@
ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
find
```
"""
def take_coordinates(string_to_be_checked):
    for idx, ch in enumerate(string_to_be_checked):
        if ch == "<":
            return string_to_be_checked[idx+1:-1:]

    return None

input_key = [int(x) for x in input().split()]

command = input()
hidden_msg = []
while not command == "find":
    counter = 0
    for ch in command:
        letter = ord(ch) - input_key[counter]
        hidden_msg.append(chr(letter))
        counter += 1
        if counter == len(input_key):
            counter = 0
    hidden_msg = (''.join(hidden_msg)).split("&")
    treasure = hidden_msg[1]
    coordinates = take_coordinates(hidden_msg[2])
    print(f"Found {treasure} at {coordinates}")
    hidden_msg  = []
    command = input()
