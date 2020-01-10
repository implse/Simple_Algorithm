# Given a 2D screen, location of a pixel in the screen and a color,
# replace color of the given pixel and all adjacent same colored pixels with the
# given color.

matrix = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 2, 0],
[1, 0, 0, 1, 0, 2, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[2, 2, 1, 1, 1, 2, 2, 1],
]


ln_row = len(matrix)
ln_col = len(matrix[0])
visited = []

# Return all the neighbors (8) of a given cell.
def neighbours(row, col):
    return [[row+1, col], [row+1, col], [row-1, col], [row, col-1],
            [row+1, col+1], [row+1, col-1], [row-1, col-1], [row-1, col+1]]

# Recursive Flood Fill
def flood_fill(row, col, color, fill_color):
    # Flood fills the given segment starting from given index
    if row < 0 or row >= ln_row:
        return
    if col < 0 or col >= ln_col:
        return
    if matrix[row][col] != color:
        return

    matrix[row][col] = fill_color
    visited.append([row, col])
    moves = neighbours(row, col)

    # Recursive DFS
    for move in moves:
        if move not in visited:
            flood_fill(move[0], move[1], color, fill_color)


def flood_matrix():
    print("Matrix Input")
    for i in matrix:
        print(i)

    replace_point = (4, 4)
    flood_fill(*replace_point, color=2, fill_color=3)

    print("-" * 25)
    print("Matrix output : fill color = 3")
    for i in matrix:
        print(i)


flood_matrix()
