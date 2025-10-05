class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited, prev_height):
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or heights[r][c] < prev_height:
                return

            visited[r][c] = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])  # left col
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # right
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])  # top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # bottom row

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result