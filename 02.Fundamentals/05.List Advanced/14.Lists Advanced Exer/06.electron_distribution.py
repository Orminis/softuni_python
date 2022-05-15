number_of_electrons = int(input())
filled_electrons = []
shell_number = 0

while number_of_electrons > 0:
    shell_number += 1
    electrons_to_be_add_to_shell = 2 * (shell_number ** 2)
    if number_of_electrons > electrons_to_be_add_to_shell:
        number_of_electrons -= electrons_to_be_add_to_shell
        filled_electrons.append(electrons_to_be_add_to_shell)
    else:
        filled_electrons.append(number_of_electrons)
        break

print(filled_electrons)
