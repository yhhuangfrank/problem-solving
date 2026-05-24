class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visit = set()
            q.append((r, c))
            visit.add((r, c))
            dist = 0

            while q:
                size = len(q)
                for _ in range(size):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return dist
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = row + dr, col + dc
                        if (
                            min(nr, nc) < 0 or nr == ROWS or nc == COLS
                            or (nr, nc) in visit or grid[nr][nc] == -1
                        ):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                dist += 1
            return dist
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        