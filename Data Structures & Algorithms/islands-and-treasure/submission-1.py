class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
                    
        def bfs():
            dist = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    visited[r][c] = True
                    grid[r][c] = dist
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            min(nr, nc) < 0 or nr == ROWS or nc == COLS
                            or grid[nr][nc] == -1 or visited[nr][nc]
                        ):
                            continue
                        queue.append((nr, nc))
                        visited[nr][nc] = True
                dist += 1
        
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited[row][col] = True
        # 執行 bfs
        bfs()

        

