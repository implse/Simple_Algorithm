# Sierpinski Triangle
n = 8
grid = [["." for _ in range(n)] for i in range(n)]

# Iterative Method
def sierpinski_triangle_iterative(grid, n):
    row = 0
    col = 0
    cote = 1
    grid[0][0] = "#"
    while cote < n:
        for row in range(cote):
            for col in range(cote):
                grid[row][col + cote] = grid[row][col]
                grid[row + cote][col] = grid[row][col]
        cote *= 2

# Recursive Method
def sierpinski_triangle_recursive(grid, n, x, y):
    if n == 1:
        grid[x][y] = "#"
        return
    n //= 2
    sierpinski_triangle_recursive(grid, n, x, y)
    sierpinski_triangle_recursive(grid, n, x + n, y)
    sierpinski_triangle_recursive(grid, n, x, y + n)


def print_grid(grid):
    for r in range(n):
        print(" ".join(grid[r]))

sierpinski_triangle_recursive(grid, n, 0, 0)
print_grid(grid)
