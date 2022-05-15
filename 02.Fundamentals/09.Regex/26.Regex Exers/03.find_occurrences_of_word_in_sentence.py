# import re
#
# sentence = input().lower()
# searched_word = input().lower()
#
# pattern = fr"\b{searched_word}\b"
#
# matches = re.findall(pattern, sentence)

#################################################

import re

sentence = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, sentence, flags=re.I)  # flags=re.I = означава че не се интересува дали са главни или
                                                     # малки буквите

print(len(matches))