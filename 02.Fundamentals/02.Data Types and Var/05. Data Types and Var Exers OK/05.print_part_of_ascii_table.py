start_index = int(input())
stop_index = int(input())
all_symbols = ""
for i in range(start_index, stop_index + 1):
    all_symbols += chr(i) + " "
print(all_symbols)