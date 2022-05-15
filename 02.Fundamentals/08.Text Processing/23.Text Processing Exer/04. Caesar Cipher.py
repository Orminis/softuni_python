text = input()
cypher = ''
for char in text:
    cypher += chr(ord(char) + 3)
print(cypher)