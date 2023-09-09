#Calculator of sum which will be received at the end of deposit time based on yearly profit percentage.

deposit_sum = float(input())
deposit_time = int(input())
yearly_profit_percentage = float(input()) / 100
total_sum = deposit_sum + deposit_time * ((deposit_sum * yearly_profit_percentage)/12)
print(total_sum)
