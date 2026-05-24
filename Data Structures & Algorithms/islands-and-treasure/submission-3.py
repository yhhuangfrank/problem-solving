class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs():
            dist = 0
            while q:
                size = len(q)
                for _ in range(size):
                    r, c = q.popleft()
                    grid[r][c] = dist
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if (
                            min(nr, nc) < 0 or nr == ROWS or nc == COLS
                            or visit[nr][nc] or grid[nr][nc] == -1
                        ):
                            continue
                        q.append((nr, nc))
                        visit[nr][nc] = True
                dist += 1
            return dist
        
        # O(mn) time complexity, space complexity
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = [[False] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit[r][c] = True
        bfs()
        