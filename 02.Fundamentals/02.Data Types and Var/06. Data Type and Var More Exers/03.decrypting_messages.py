key = int(input())
n = int(input())    # number of lines
decrypted_message = ""

for x in range(n):
    letter = input()
    letter_ascii = ord(letter)
    decrypted_message += chr(letter_ascii + key)
print(decrypted_message)

