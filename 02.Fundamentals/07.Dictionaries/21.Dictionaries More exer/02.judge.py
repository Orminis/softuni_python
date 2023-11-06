"""
You know the judge system, right?! Your job is to create a program similar to the Judge system.
You will receive several input lines in one of the following formats:
    "{username} -> {contest} -> {points}"
The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every contest and points of each user:
    If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
    Otherwise, just save the data - contest, username, and points.
Also, you need to keep individual statistics for each user - the total points of all contests (including even points from the same contents).
You should end your program when you receive the command "no more time".
At that point you should print each contest in order of input,
for each contest print the participants ordered by points in descending order, then ordered by name in ascending order.
After that, you should print individual statistics for every participant ordered by total points in descending order, and then by alphabetical order.

Input / Constraints
    The input comes in the form of commands in one of the formats specified above.
    Username and contest name always will be one word.
    Points will be an integer will be an integer in range [0, 1000].
    There will be no invalid input lines.
    If all sorting criteria fail, the order should be by order of input.
    The input ends when you receive the command "no more time".
Output
    The output format for the contests is:
        "{constest_name}: {number_participants} participants
        1. {username1} <::> {points}
        2. {username2} <::> {points}
        …
        {N}. {usernameN} <::> {points}"
    After you print all contests, print the individual statistics for every participant.
    The output format is:
        "Individual standings:
        1.{username1} -> {total_points}
        2.{username} -> {total_points}
        …
        {N}. {username} -> {total_points}
"""

judge_input = input()
contest_dict = {}
user_dict = {}

while not judge_input == "no more time":
    username, contest, points = judge_input.split(" -> ")
    points = int(points)

    if not contest in contest_dict:
        contest_dict[contest] = {username: points}
    elif not username in contest_dict[contest]:
        contest_dict[contest][username] = points

    elif username in contest_dict[contest]:
        if points > contest_dict[contest][username]:
            contest_dict[contest][username] = points

    judge_input = input()

# Console printing
for cont, users in contest_dict.items():
    print(f"{cont}: {len(contest_dict[cont])} participants")
    counter = 1
    sort_users = dict(sorted(users.items(), key= lambda up: (-up[1], up[0])))
    for user, points in sort_users.items():
        print(f"{counter}. {user} <::> {points}")
        counter += 1
        if not user in user_dict:
            user_dict[user] = 0
        user_dict[user] += points

sorted_user_dict = dict(sorted(user_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])))
counter = 1
print("Individual standings:")
for user, points in sorted_user_dict.items():
    print(f"{counter}. {user} -> {points}")
    counter += 1