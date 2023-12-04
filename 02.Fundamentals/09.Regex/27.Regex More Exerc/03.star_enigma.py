"""
You will receive several messages, which are encrypted using the legendary star enigma.
You should decrypt the messages, following these rules:
To properly decrypt a message, you should count all the letters [s, t, a, r] – case-insensitive and
remove the count from the current ASCII value of each symbol of the encrypted message.
After decryption:
Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
    The planet name starts after '@' and contains only letters from the Latin alphabet.
    The planet population starts after ':' and is an Integer;
    The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
    The soldier count starts after "->" and should be an Integer.
The order in the message should be: planet name -> planet population -> attack type -> soldier count. Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
Input / Constraints
    The first line holds n – the number of messages– integer in range [1…100];
    On the next n lines, you will be receiving encrypted messages.
Output
After decrypting all messages, you should print the decrypted information in the following format:
First print the attacked planets, then the destroyed planets.
    "Attacked planets: {attackedPlanetsCount}"
    "-> {planetName}"
    "Destroyed planets: {destroyedPlanetsCount}"
    "-> {planetName}"
The planets should be ordered by name alphabetically.
Example input:
2
STCDoghudd4=63333$D$0A53333
EHfsytsnhf?8555&I&2C9555SR

3
tt(''DGsvywgerx>6444444444%H%1B9444
GQhrr|A977777(H(TTTT
EHfsytsnhf?8555&I&2C9555SR
Output:
Attacked planets: 1
-> Alderaa
Destroyed planets: 1
-> Cantonica
"""
import re

num_of_messages = int(input())

pattern = r"[^@!:>-]*@(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<attack>[A|D])![^@!:>-]*->(?P<soldiers>\d+)"
_decr_key_lst = ['s', 't', 'a', 'r']
attacked_planets = []
destroyed_planets = []

for _ in range(num_of_messages):
    message_str = input()
    # counting how many of the characters in the `message_str` are [s, t, a, r]
    dec_key = 0
    for ch in message_str:
        if ch.lower() in  _decr_key_lst:
            dec_key +=1

    decrypted_msg = ''
    # decrypting the message with `dec_key`
    for char in message_str:
        decr_char = chr(ord(char) - dec_key)
        decrypted_msg += decr_char

    mess_match = re.search(pattern, decrypted_msg)

    # assigning planets to corresponding lists
    if mess_match is not None:
        attack = mess_match.group('attack')
        planet = mess_match.group('planet')
        if attack == "A":
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

# Printing first attacked then destroyed planets in desc order
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
