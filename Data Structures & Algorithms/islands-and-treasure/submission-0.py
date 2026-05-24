class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            visited = set()
            queue = deque()
            queue.append((i, j))
            dist = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return dist
                    visited.add((r,c))
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            min(nr, nc) < 0 or nr == ROWS or nc == COLS
                            or grid[nr][nc] == -1 or (nr, nc) in visited
                        ):
                            continue
                        queue.append((nr, nc))
                        visited.add((nr,nc))
                dist += 1
            return dist

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == INF:
                    distance = bfs(row, col)
                    grid[row][col] = INF if distance == 0 else distance

