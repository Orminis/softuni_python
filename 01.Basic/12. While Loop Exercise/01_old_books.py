# Търсене на името на книга

book_name = input()  # Името на търсената книга

book_count = 0       # Бройка на проверените книги
is_book_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")

############################################################

wanted_book = input()
book_counter = 0

while True:
    current_book_name = input()

    if current_book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    elif current_book_name == wanted_book:
        print(f"You checked {book_count} books and found it.")
        break

    book_counter += 1
