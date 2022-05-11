# Pipe condition after H hours of time after a worker started filling it from 2 pipes

volume_of_pool = int(input())
water_income_from_p1 = int(input())
water_income_from_p2 = int(input())
H = float(input())

vol_from_p1 = water_income_from_p1 * H
vol_from_p2 = water_income_from_p2 * H
filled_volume = vol_from_p1 + vol_from_p2
filled_volume_in_perc = filled_volume / volume_of_pool * 100

if volume_of_pool >= (water_income_from_p1 * H) + (water_income_from_p2 * H):
    print(f"The pool is {filled_volume_in_perc:.2f}% full. Pipe 1: {vol_from_p1 / filled_volume * 100:.2f}%. \
Pipe 2: {vol_from_p2 / filled_volume * 100:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with {filled_volume - volume_of_pool:.2f} liters.")
