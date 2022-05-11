deposit_sum = float(input())
deposit_time = int(input())
yearly_profit_percentage = float(input()) / 100
sum = deposit_sum + deposit_time * ((deposit_sum * yearly_profit_percentage)/12)
print(sum)
