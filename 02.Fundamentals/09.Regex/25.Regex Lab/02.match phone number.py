"""
Write a regular expression to match a valid phone number from Sofia.
After you find all valid phones, print them on the console, separated by a comma and a space ", ".
Compose the Regular Expression
A valid number has the following characteristics:
It starts with "+359"
Then, it is followed by the area code (always 2)
After that, it is followed by the number itself:
oThe number consists of 7 digits (separated in two groups of 3 and 4 digits respectively).
The different parts are separated by either a space or a hyphen ('-').
Example input:
+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222
Output:
+359 2 222 2222, +359-2-222-2222
"""
import re

phone_numbers = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

valid_phones = re.findall(pattern, phone_numbers)
print(", ".join(valid_phones))
