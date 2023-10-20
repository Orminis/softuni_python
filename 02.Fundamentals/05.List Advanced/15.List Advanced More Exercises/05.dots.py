"""
You will be given a number n representing the number of rows of a board of dots and dashes.
On the following n lines, you will receive each row of the board as a string with symbols
(dots and dashes only), separated by a single space.
Your task is to find and print the largest count of dots that could be connected at once.
You could only connect horizontally or vertically.
"""

#check is position inside the matrix:
def check_is_inside(row, col, matrikss):
    if row >= len(matrikss) or row < 0 or col >= len(matrikss[0]) or col < 0:
        return None
    return True

# Check what symbol is inside
def check_symbol(row, col, matriks):
    if not matriks[row][col] == '.':
        return None
    return True

# check nearby positions

def check_nearby_positions_for_dots(row, col, matriks):
    dots = []
    if check_is_inside(row-1, col, matriks): #North
        if check_symbol(row-1, col, matriks):
            dots.append([row-1, col])

    if check_is_inside(row+1, col, matriks): #South
        if check_symbol(row+1, col, matriks):
            dots.append([row+1, col])

    if check_is_inside(row, col-1, matriks): #west
        if check_symbol(row, col-1, matriks):
            dots.append([row, col-1])

    if check_is_inside(row, col+1, matriks): #east
        if check_symbol(row, col+1, matriks):
            dots.append([row, col+1])

    return dots

row_n = int(input())
matrix = []
dots_pools = [[[0, 0],[0, 1], [1,1]],[0,3],[0,5]]

for r in range(row_n):
    row = [x for x in input().split(' ')]
    matrix.append(row)


for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if check_symbol(r, c, matrix):

            nearby_dots = check_nearby_positions_for_dots(r, c, matrix)

            pool = {f'i[0]-i[1]' for i in x for x in nearby_dots}
            pool.add('r-c')