"""
On the first line, you will be given the population (numbers separated by comma and space ", ").
On the second line, you will be given the minimum wealth.
You should distribute the wealth so that no part of the population has less than the minimum wealth.
To do that, you should always take wealth from the wealthiest part of the population.
There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".

Example
2, 3, 5, 15, 75     [5, 5, 5, 15, 70]
5
2, 3, 5, 15, 75     [20, 20, 20, 20, 20]
20
2, 3, 5, 45, 45     No equal distribution possible
30
"""

population = [int(x) for x in input().split(', ')]
min_wealth = int(input())

poor_lst = [x for x in population if x < min_wealth]
rich_lst = [x for x in population if x > min_wealth]
needed_wealth = (len(poor_lst) * min_wealth) - sum(poor_lst)
wealth_to_be_spent = sum(rich_lst) - (len(rich_lst) * min_wealth)
if wealth_to_be_spent < needed_wealth:
    print("No equal distribution possible")
else:
    is_break = False
    while True:
        poorest = min(population)
        richest = max(population)
        poor_loc = population.index(poorest)
        rich_loc = population.index(richest)
        if richest - (min_wealth - poorest) >= min_wealth:
            richest -= (min_wealth - poorest)
            population.pop(rich_loc)
            population.insert(rich_loc, richest)
            population.pop(poor_loc)
            population.insert(poor_loc, min_wealth)
        else:
            population.pop(rich_loc)
            population.insert(rich_loc, min_wealth)
            population.pop(poor_loc)
            poorest += richest - min_wealth
            population.insert(poor_loc, poorest)

        if not any([x for x in population if x < min_wealth]):
            print(population)
            break