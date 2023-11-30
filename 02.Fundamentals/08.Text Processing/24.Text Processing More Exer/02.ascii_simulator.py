"""
Write a program which prints a sum of all found characters between two given characters (their ASCII code).
On each of the first two lines you will receive a single character. On the last line you get a random string.

Print the sum of the ASCII values of all characters in the random string which are in between the two given characters.
Example:
    ```
.
@
dsg12gr5653feee5
#######################
?
E
@ABCEF
```

"""

def char_between_given_characters(chr_1, chr_2, chr):
    if chr_1 > chr_2:
        if chr_1 > chr > chr_2:
            return True
    elif chr_2 > chr_1:
        if chr_2 > chr > chr_1:
            return True
    return False


char_1 = ord(input())
char_2 = ord(input())

input_string = input()
ch_lst = []

for ch in input_string:
    ch_ascii_num = ord(ch)
    if char_between_given_characters(char_1, char_2, ch_ascii_num):
        ch_lst.append(ch_ascii_num)

print(sum([x for x in ch_lst]))