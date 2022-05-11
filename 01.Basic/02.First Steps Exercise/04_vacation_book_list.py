number_of_pages = int(input())
pages_read_per_hour = int(input())
days_to_read_book = int(input())

time_for_a_book = number_of_pages // pages_read_per_hour
hours_per_day = time_for_a_book // days_to_read_book
print(hours_per_day)