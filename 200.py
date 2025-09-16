import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    self.bfs(grid, r, c)

        return island_count

    def bfs(self, grid: list[list[str]], r: int, c: int):
        q = collections.deque()

        q.append((r, c))
        grid[r][c] = '0'
        rows, cols = len(grid), len(grid[0])

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == '1'):
                    q.append((nr, nc))
                    grid[nr][nc] = '0'