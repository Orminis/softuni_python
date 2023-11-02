"""
Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni.
Here is your final task.
You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests".
Save that data because you will need it later.
After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".

Here is what you need to do.
    Check if the contest is valid (It is considered valid if you received it in the first type of input)
    Check if the password is correct for the given contest
    If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests)
    and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.

In the end, you should print the info for the user with the most points (total points for all contents they participated in)
 in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names.
For each user print each contest with the points in descending order. See the examples.
"""

contest_dict = {}
users_dict = {}

contest_info = input()
while not contest_info == "end of contests":
    contest, password = contest_info.split(":")
    contest_dict[contest] = password

    contest_info = input()


submissions_info = input()
while not submissions_info == "end of submissions":
    contest, password, username, points = submissions_info.split("=>")
    points = int(points)
    if contest in contest_dict:

        if password == contest_dict[contest]:           # check is password correct

            if not username in users_dict:              # check is the user already included in `users_dict`
                users_dict[username] = {}
                users_dict[username][contest] = int(points)

            elif not contest in users_dict[username]:   # if contest not added before to the user
                users_dict[username][contest] = int(points)

            elif username in users_dict and contest in users_dict[username]:       # if user and contest are already included checks the score and update it if the new score is higher.
                old_score = users_dict[username][contest]
                if points > old_score:
                    users_dict[username][contest] = int(points)

    submissions_info = input()

for user, contests in users_dict.items():
    sorted_contest = dict(sorted(contests.items(), key=lambda kvp: -kvp[1]))

for user, contests in users_dict.items():
    sorted_contest = dict(sorted(contests.items(), key=lambda kvp: -kvp[1]))
    print(sorted_contest)
    for contest, score in sorted_contest.items():
        print(f"# {contest} -> {score}")