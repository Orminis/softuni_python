"""
On the first line, you will receive a key (integer).
On the second line, you will receive n – the number of lines, which will follow.
On the next n lines – you will receive a lower and an uppercase letter per line.
You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.
"""
key = int(input())
n = int(input())    # number of lines
decrypted_message = ""

for x in range(n):
    letter = input()
    letter_ascii = ord(letter)
    decrypted_message += chr(letter_ascii + key)
print(decrypted_message)

