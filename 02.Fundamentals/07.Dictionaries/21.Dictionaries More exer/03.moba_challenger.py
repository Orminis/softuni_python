"""
You are a pro MOBA player, you are struggling to become а master of the Challenger tier.
So, you carefully watch the statistics in the tier.

You will receive several input lines in one of the following formats:
    "{player} -> {position} -> {skill}"
    "{player} vs {player}"
The "player" and "position" are strings, and the given "skill" will be an integer number.
You need to keep track of every player.
When you receive a player with his position and skill, add him to the players' pool, if he isn`t present,
else add his position and skill or update his skill, only if the current position skill is lower than the new value.

If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
    If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him.
    If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
    If they don`t have positions in common, the duel isn`t happening and both continue in the Season.

You should end your program when you receive the command "Season end".
At that point you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order.
For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.

Input / Constraints
    The input comes in the form of commands in one of the formats specified above.
    Player and position will always be one word string, containing no whitespaces.
    Skill will be an integer in the range [0, 1000].
    There will be no invalid input lines.
    The program ends when you receive the command "Season end".
Output
    The output format for each player is:
        "{player}: {total_skills} skill"
        - {position1} <::> {skill}
        - {position2} <::> {skill}
        …
        - {positionN} <::> {skill}"
"""


players_dict = {}
possible_positions = ["Tank", "Mid", "Support", "Adc"]

players_input = input()

while not players_input == "Season end":
    # check the input
    # if `->` is present in the input string, the player should be added to the `players_dict`
    if "->" in players_input:
        player_name, positions, skill = players_input.split(" -> ")
        skill = int(skill)

        # adding new player to the dict + position and skill
        if player_name not in players_dict:
            players_dict[player_name] = {}
        # adding position if not present or updating position's skill if current skill is lower than the new one.
        if positions not in players_dict[player_name]:
            players_dict[player_name][positions] = skill
        elif skill > players_dict[player_name][positions]:
            players_dict[player_name][positions] = skill
    # Duel time.
    else:
        player_one, player_two = players_input.split(" vs ")

        # They can not duel if any of the players is not present in `players_dict`.
        if not player_one in players_dict or not player_two in players_dict:
            players_input = input()
            continue
        # Check for common positions and the skill.
        for position in possible_positions:
            if position in players_dict.get(player_one) and position in players_dict.get(player_two):
                player_one_skill_sum = sum(players_dict[player_one].values())
                player_two_skill_sum = sum(players_dict[player_two].values())
                if player_one_skill_sum > player_two_skill_sum:
                    players_dict.pop(player_two)
                    break
                elif player_one_skill_sum < player_two_skill_sum:
                    players_dict.pop(player_one)
                    break

    players_input = input()

# Ordered by total skill in descending order, then ordered by player name in ascending order.
sorted_player_dict_by_skill_and_name = dict(sorted(players_dict.items(), key=lambda playerr: (-(sum(playerr[1].values())), playerr[0])))

# ordered position descending by skill, then ordered by name in ascending order.
# Using dictionary comprehension will order stat: (position/skill) for each player
# sorted_psn_by_skill_per_player = {players: dict(sorted(stats.items(), key= lambda x: (-x[1], x[0]))) for players, stats in sorted_player_dict_by_skill_and_name.items()}
# for players, stats in sorted_psn_by_skill_per_player
for player, stats in sorted_player_dict_by_skill_and_name.items():
    print(f"{player}: {sum(stats.values())} skill")
    for psn, skill in sorted(stats.items(), key= lambda kvp: (-int(kvp[1]), kvp[0])):
        print(f"- {psn} <::> {skill}")
