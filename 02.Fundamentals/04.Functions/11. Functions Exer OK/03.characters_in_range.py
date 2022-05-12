# To write a function which returns a strung with all the characters between 2 input characters as per ASCII Table

def characters_range(char1, char2):
    collected_symbols = ''
    for i in range(ord(char1) + 1, ord(char2)):
        collected_symbols += chr(i) + " "
    return collected_symbols


character1 = input()
character2 = input()


result = characters_range(character1, character2)
print(result)



##################################################


def characters_range(char1, char2):
    collected_symbols = []
    for i in range(ord(char1) + 1, ord(char2)):
        collected_symbols.append(chr(i))
    return collected_symbols


character1 = input()
character2 = input()


result = characters_range(character1, character2)
print(' '.join(result))

######################################

def characters_range(char1, char2):
    return [chr(s) for s in range(ord(char1) + 1, ord(char2))]


character1 = input()
character2 = input()


result = characters_range(character1, character2)
print(' '.join(result))
