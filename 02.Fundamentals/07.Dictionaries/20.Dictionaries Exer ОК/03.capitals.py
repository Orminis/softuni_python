country_name = input().split(", ")
capital_name = input().split(", ")

result = dict(zip(country_name, capital_name))

res = {print(f"{country} -> {capital}") for country, capital in result.items()}
