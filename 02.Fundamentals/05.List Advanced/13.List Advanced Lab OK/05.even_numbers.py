string = input().split(", ")

int_list = [int(x) for x in string]
filtered_list = [index for index in range(len(int_list)) if int_list[index] % 2 == 0]
print(filtered_list)

filtered_list_filter = [int_list.index(el) for el in list(filter(lambda x: x % 2 == 0, int_list))]
filtered_list_filter_map = list(map(lambda el: int_list.index(el), list(filter(lambda x: x % 2 == 0, int_list))))
print(filtered_list_filter)
print(filtered_list_filter_map)
