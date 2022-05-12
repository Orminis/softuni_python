def password_length(password):
    is_length = False
    if 5 < len(password) < 11:
        is_length = True
    return is_length


def password_characters(password):
    is_character = False
    if password.isalnum():
        is_character = True
    return is_character


def password_contains_two_digits(password):
    is_contain_two_digits = False
    counter = 0
    for i in password:
        if i.isdigit():
            counter += 1
    if counter >= 2:
        is_contain_two_digits = True
    return is_contain_two_digits


password_input = input()

password_check = [password_length(password_input), password_characters(password_input),
                  password_contains_two_digits(password_input)]

if all(password_check):
    print("Password is valid")
else:
    if not password_length(password_input):
        print("Password must be between 6 and 10 characters")
    if not password_characters(password_input):
        print("Password must consist only of letters and digits")
    if not password_contains_two_digits(password_input):
        print("Password must have at least 2 digits")
