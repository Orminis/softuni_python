# """
# Kate is stuck in a maze. You should
# help her to find her way out.
# On the first line, you will be given how many rows there are in the maze.
# On the following n lines, you will be given the maze itself. Here is a legend for the maze:
#
#     "#" - means a wall; Kate cannot go through there
#     " " - means empty space; Kate can go through there
#     "k" - the initial position of Kate; start looking for a way out from there
#
# There are two options: Kate either gets out or not:
#     If Kate can get out, print the following:
#     "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
#     Otherwise, print: "Kate cannot get out".
#
# 4
# ######
# ##   k
# ## ###
# ## ###
#
# 5
# ######
# ##  k#
# ## ###
# ######
# ## ###
# """
#
# row_size = int(input())
# matrix = []
# starting_pos = []
#
# for row in range(row_size):
#     row_lst = [input()]
#     matrix.append(row_lst)
#     if not len(starting_pos) == 0:
#         continue
#     else:
#         for col, val in enumerate(row_lst[0]):
#             if val == 'k':
#                 starting_pos.append(row)
#                 starting_pos.append(col)
#                 starting_pos = tuple(starting_pos)
#
# # check is Kate on the edge
# # if starting_pos[0] == 0 or starting_pos[0] == row_size or starting_pos[1] == 0 or starting_pos[1] == len(matrix[0][0]) - 1:
# #     # then kate is on the edge:
# #     aaa = 0
# #     print(f"Kate got out in {aaa} move.")
#
# kates_movement = []
# # check squares around kate
# def kate_surroundings(kate_row, kate_col):
#     kate_possible_move = []
#     if matrix[kate_row-1][kate_col] == " ": #north
#         kate_possible_move.append([kate_row-1, kate_col])
#     if matrix[kate_row+1][kate_col] == " ": #south
#         kate_possible_move.append([kate_row+1, kate_col])
#     if matrix[kate_row][kate_col +1] == ' ': #east
#         kate_possible_move.append([kate_row, kate_col +1])
#     if matrix[kate_row][kate_col -1] == ' ': #west
#         kate_possible_move.append([kate_row, kate_col - 1])
#     return kate_possible_move
#
# while True:
#     kates_move = kate_surroundings(starting_pos[0], starting_pos[1])
#     print(kates_move)