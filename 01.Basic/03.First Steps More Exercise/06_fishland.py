price_mackerel = float(input())
price_sprat = float(input())
kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_mussels = int(input())

price_bonito = (price_mackerel + price_mackerel * 0.6) * kg_bonito
price_horse_mackerel = (price_sprat + price_sprat * 0.8) * kg_horse_mackerel
price_mussels = 7.50 * kg_mussels
total_price = price_bonito + price_horse_mackerel + price_mussels
print(f"{total_price:.2f}")