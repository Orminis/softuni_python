import re

some_string = input()

pattern = r"((?<=\s)(?P<username>[a-z0-9]+[\-\.\_a-z0-9]*)@(?P<host>([a-z]+)(-[a-z]+)*\.([a-z\.]+)))\b"

# valid_emails = [match.group() for match in re.finditer(pattern, some_string)]
#
# print("\n".join(valid_emails))


matches = re.findall(pattern, some_string)
print("\n".join([match[0] for match in matches]))
