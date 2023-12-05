# from https://www.python-engineer.com/posts/regular-expressions/
# Further readings¶
# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://developers.google.com/edu/python/regular-expressions


import re

# finditer()
# finditer(): Find all substrings where the RE matches, and returns them as an iterator.
my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group()) # returns the string

# <re.Match object; span=(3, 6), match='123'>
# (3, 6) 3 6
# 123
# <re.Match object; span=(9, 12), match='123'>
# (9, 12) 9 12
# 123
# ^that was finditer
print("^that was finditer")


# findall()
# findall(): Find all substrings where the RE matches, and returns them as a list.
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)
# 123
# 123
# ^that was findall
print("^that was findall")


# match
# match(): Determine if the RE matches at the beginning of the string.
match = pattern.match(my_string)
print(match)
pattern = re.compile(r'abc')
match = pattern.match(my_string)
print(match)
# None
# <re.Match object; span=(0, 3), match='abc'>
# ^that was match
print("^that was match")


# search
# search(): Scan through a string, looking for any location where this RE matches.
match = pattern.search(my_string)
# <re.Match object; span=(0, 3), match='abc'>
print(match)

"""
Methods on a Match object¶
    group(): Return the string matched by the RE
    start(): Return the starting position of the match
    end(): Return the ending position of the match
    span(): Return a tuple containing the (start, end) positions of the match

Meta characters
Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with \) if we actually want to search for the char.

test_string = 'python-engineer.com'
pattern = re.compile(r'\.')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    <re.Match object; span=(15, 16), match='.'>


. Any character (except newline character) "he..o"
^ Starts with "^hello"
\$ Ends with "world\$"
* Zero or more occurrences "aix*"
+ One or more occurrences "aix+"
{ } Exactly the specified number of occurrences "al{2}"
[] A set of characters "[a-m]"
\ Signals a special sequence (can also be used to escape special characters) "\d"
| Either or "falls|stays"
( ) Capture and group


More Metacharacters / Special Sequences¶
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

    \d :Matches any decimal digit; this is equivalent to the class [0-9].
    \D : Matches any non-digit character; this is equivalent to the class [^0-9].
    \s : Matches any whitespace character;
    \S : Matches any non-whitespace character;
    \w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
    \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
    \b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
    \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
    \A Returns a match if the specified characters are at the beginning of the string "\AThe"
    \Z Returns a match if the specified characters are at the end of the string "Spain\Z"


Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning. 
Append multiple conditions back-to back, e.g. [aA-Z].
A ^ (caret) inside a set negates the expression.
A - (dash) in a set specifies a range if it is in between, otherwise the dash itself.

Examples:
- [arn] Returns a match where one of the specified characters (a, r, or n) are present
- [a-n] Returns a match for any lower case character, alphabetically between a and n
- [^arn] Returns a match for any character EXCEPT a, r, and n
- [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
- [0-9] Returns a match for any digit between 0 and 9
- [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
- [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case

Quantifiers
* : 0 or more
+ : 1 or more
? : 0 or 1, used when a character can be optional
{4} : exact number
{4,6} : range numbers (min, max)


Conditions¶
Use the | for either or condition.


Grouping¶
( ) is used to group substrings in the matches."""


# Modifying strings¶
# split(): Split the string into a list, splitting it wherever the RE matches
# sub(): Find all substrings where the RE matches, and replace them with a different string
my_string = 'abc123ABCDEF123abc'
pattern = re.compile(r'123') #  no escape for the . here in the set
matches = pattern.split(my_string)
print(matches)

my_string = "hello world, you are the best world"
pattern = re.compile(r'world')
subbed_string = pattern.sub(r'planet', my_string)
print(subbed_string)

# ['abc', 'ABCDEF', 'abc']
# hello planet, you are the best planet

urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    #print(match)
    print(match.group()) # 0
    #print(match.group(1))
    #print(match.group(2))
    print(match.group(3))

# substitute using back references to replace url + domain name
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
    # http://python-engineer.com
    # .com
    # https://www.python-engineer.org
    # .org
    # http://www.pyeng.net
    # .net
    #
    # python-engineer.com
    # python-engineer.org
    # pyeng.net

# Compilation Flags¶
# ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
# DOTALL, S : Make . match any character, including newlines.
# IGNORECASE, I : Do case-insensitive matches.
# LOCALE, L : Do a locale-aware match.
# MULTILINE, M : Multi-line matching, affecting ^ and $.
# VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.

my_string = "Hello World"
pattern = re.compile(r'world', re.IGNORECASE) # No match without I flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

my_string = '''
hello
cool
Hello
'''
# line starts with ...
pattern = re.compile(r'^[a-z]', re.MULTILINE) # No match without M flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
# <re.Match object; span=(6, 11), match='World'>
# <re.Match object; span=(1, 2), match='h'>
# <re.Match object; span=(7, 8), match='c'>

