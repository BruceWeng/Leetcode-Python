"""
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water. Grid cells are connected horizontally/vertically
(not diagonally). The grid is completely surrounded by water, and there is exactly
one island (i.e., one or more connected land cells). The island doesn't have
"lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

T: O(MN), S: O(1)

* There is also a solution using DFS and visited hash table, but not necessary.
"""
"""
@params {int[][]} grid: element either 0 or 1
@return {int}
"""
def islandPerimeter(grid):
    """
    1. Loop over grid and count numbers of island
    2. find right neighbors and down neighbors
    3. return islands * 4 and neighbors * 2
    """
    if grid == None or len(grid) == 0:
        return 0
    islands = 0
    neighbors = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 1:
                islands += 1
                # Count right neighbors
                if j < len(row) - 1 and grid[i][j + 1] == 1:
                    neighbors += 1
                # Count down neighbors
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    neighbors += 1
    return islands * 4 - neighbors * 2
