w = float(input()) # length in meters
h = float((((((((((input())))))))))) # width in meters

w = w * 100
h = h * 100
places_in_rows = (h - 100) // 70
places_in_columns = w // 120
total_places = (places_in_columns * places_in_rows) - 3
print(total_places)