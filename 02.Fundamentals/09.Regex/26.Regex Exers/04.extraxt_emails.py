"""
Write a program which receives a single string and extracts all email addresses from it.
Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
    {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
        oExamples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
        oExamples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
    {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".". Each word consists of only letters and can have hyphens "-" between the letters.
        oExamples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
        oExamples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"
"""
"""
Examples of valid emails: 
    @softuni-bulgaria.org, kiki@hotmail.co.uk, no-reply@github.com,  s.peterson@mail.uu.net, 
    info-bg@software-university.software.academy
Examples of invalid emails: 
    --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn, mike@helloworld, mike@.unknown.soft., s.johnson@invalid-
Example input:
Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.
Output:
steve.parker@softuni.de
"""
import re

some_string = input()

pattern = r"((?<=\s)(?P<username>[a-z0-9]+[\-\.\_a-z0-9]*)@(?P<host>([a-z]+)(-[a-z]+)*\.([a-z\.]+)))\b"

valid_emails = [match.group() for match in re.finditer(pattern, some_string)]
print("\n".join(valid_emails))

# matches = re.findall(pattern, some_string)
# print("\n".join([match[0] for match in matches]))
