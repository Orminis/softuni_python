"""
Write a program that translates messages from Morse code to English (capital letters).
Use this page to help you (without the numbers). https://morsecode.world/international/morse2.html
The words will be separated by a space (' '). There will be a '|' character which you should replace with a space - ' '.
"""

morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D','.': 'E', '..-.':'F', '--.':'G','....':'H', '..':'I',
                   '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---': 'O', '.--.':'P', '--.-':'Q','.-.':'R',
                   '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}

morse_code_lst = [x for x in input().split()]
translated_lst = []
for cde in morse_code_lst:
    if cde == '|':
        translated_lst.append(' ')
    else:
        letter = morse_code_dict.get(cde)
        translated_lst.append(letter)

print(''.join(translated_lst))