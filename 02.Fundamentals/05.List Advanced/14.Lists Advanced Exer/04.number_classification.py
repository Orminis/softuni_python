numbers_as_int = [int(x) for x in input().split(", ")]
positive_numbers = list(map(str, [x for x in numbers_as_int if x >= 0]))
negative_numbers = list(map(str, [x for x in numbers_as_int if x < 0]))
even_numbers = list(map(str, [x for x in numbers_as_int if x % 2 == 0]))
odd_numbers = list(map(str, [x for x in numbers_as_int if x % 2 != 0]))


print(f"Positive: {', '.join(positive_numbers)}\nNegative: {', '.join(negative_numbers)}\nEven: {', '.join(even_numbers)}"
      f"\nOdd: {', '.join(odd_numbers)}")
