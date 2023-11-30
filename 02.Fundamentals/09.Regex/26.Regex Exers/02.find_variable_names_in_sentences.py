"""
Write a program which finds all variable names in each string. A variable name starts with an underscore ("_")
and contains only capital and non-capital letters and digits. Extract only their names, without the underscore.
Try to do this only with regular expressions.
The output consists of all variable names, extracted, and printed on a single line, separated by a comma.
Example:
    The _id and _age variables are both integers.
Output:
    id,age
"""
import re

some_input = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, some_input)
print(",".join(matches))