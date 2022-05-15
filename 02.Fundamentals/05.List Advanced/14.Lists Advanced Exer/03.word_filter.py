words = input().split()
even_length = [word for word in words if len(word) % 2 == 0]
print("\n".join(even_length))
