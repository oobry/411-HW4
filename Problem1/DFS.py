def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        """ Perform DFS to mark all connected land cells as visited """
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                island_count += 1
                dfs(r, c)

    return island_count

# Example usage:
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0]
]

print(num_islands(grid))  # Output: 2
