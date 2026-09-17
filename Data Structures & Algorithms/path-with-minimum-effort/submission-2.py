class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # range of diff: 0 <= diff < 1000000
        # choose a diff represented for max diff of a route
        # check if it works (can traverse from top-left to bottom-right)
        # if works, try to find the next smaller max diff
        # if dont work, try to find the next larger one
        # use binary search approach

        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def valid_route(max_diff: int) -> bool:
            visited = [[False] * COLS for _ in range(ROWS)]
            q = deque()
            q.append((0, 0))

            while q:
                x, y = q.popleft()

                if x == ROWS - 1 and y == COLS - 1:
                    return True
                visited[x][y] = True

                for (dx, dy) in dirs:
                    nx = x + dx
                    ny = y + dy
                    if (
                        min(nx, ny) < 0 or nx == ROWS or ny == COLS or visited[nx][ny] 
                        or abs(heights[nx][ny] - heights[x][y]) > max_diff
                    ):
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny))
            return False

        l = -1 # false
        r = 1000000 # true

        while l + 1 < r:
            mid = l + (r - l) // 2
            if valid_route(mid):
                r = mid
            else:
                l = mid
            # print(f'l, r: {(l, r)}')
        return r
