"""
Write a program which returns an encrypted version of the same text.
Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
For example, A would be replaced with D, B would become E, and so on. Print the encrypted text
"""
text = input()
cypher = ''
for char in text:
    cypher += chr(ord(char) + 3)
print(cypher)

# as list comprehension
# print("".join([chr(ord(x) +3) for x in text]))