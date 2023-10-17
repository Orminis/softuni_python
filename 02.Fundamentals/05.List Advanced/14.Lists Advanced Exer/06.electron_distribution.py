"""
You will receive a single integer – the number of electrons.
Your task is to fill shells until there are no more electrons left.
The rules for electron distribution are as follows:
    The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
        For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
    You should start filling the shells from the first one at the first position.
    If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
In the end, print a list with the filled shells.
"""
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
