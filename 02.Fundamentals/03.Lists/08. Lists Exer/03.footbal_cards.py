######################################################################

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

game_was_terminated = False

sent_off_players = input().split(" ")
for player in sent_off_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")
#################################################################

#################################################################
# player_team_and_num = input().split(' ')
# team_a = 11
# team_b = 11
# players_sent_off = []
#
# for who in player_team_and_num:
#     if who not in players_sent_off:
#         if 'A' in who:
#             team_a -= 1
#             players_sent_off.append(who)
#         if 'B' in who:
#             team_b -= 1
#             players_sent_off.append(who)
#     if team_a < 7 or team_b < 7:
#         break
# print(f'Team A - {team_a}; Team B - {team_b}')
# if team_b < 7 or team_a < 7:
#     print(f'Game was terminated')
####################################################################

# team_a = []
# team_b = []
# for number in range(1, 12):
#     team_a.append(f'A-{number}')
#     team_b.append(f'B-{number}')
# print(team_a)
# print(team_b)
###################################################################
