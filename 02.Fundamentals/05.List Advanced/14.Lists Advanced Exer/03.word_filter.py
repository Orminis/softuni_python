"""
Using comprehension, write a program that receives some text, separated by space,
and take only those words whose length is even. Print each word on a new line.
"""

words = input().split()
even_length = [word for word in words if len(word) % 2 == 0]
print("\n".join(even_length))
