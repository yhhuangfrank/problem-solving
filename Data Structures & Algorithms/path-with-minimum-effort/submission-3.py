import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        # min_heap 儲存元素為: (目前累積的最大 Effort, x, y)
        min_heap = [(0, 0, 0)]
        
        # 紀錄到達每個格子的最小 Effort，初始化為無窮大 ♾️
        efforts = [[float('inf')] * COLS for _ in range(ROWS)]
        efforts[0][0] = 0
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            
            # 🎯 第一次 pop 出終點時，這個 effort 就一定是全圖的最佳解答！
            if x == ROWS - 1 and y == COLS - 1:
                return effort
            
            # 如果拿出來的 effort 比已經記錄過的還大，代表有更優的路徑走過這裡，直接跳過
            if effort > efforts[x][y]:
                continue
                
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS:
                    # 💡 計算經過這條邊後，新的瓶頸（Effort）是多少
                    next_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    
                    # 只有當找到更小的 Effort 時才更新並放入 Priority Queue
                    if next_effort < efforts[nx][ny]:
                        efforts[nx][ny] = next_effort
                        heapq.heappush(min_heap, (next_effort, nx, ny))