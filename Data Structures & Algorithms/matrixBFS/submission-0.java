class Solution {
    public int shortestPath(int[][] grid) {
        if (grid.length == 0) return -1;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        return bfs(grid, visited);
    }

    public int bfs(int[][] grid, boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;
        int length = 0;
        Deque<Integer[]> queue = new ArrayDeque<>();
        queue.add(new Integer[] {0, 0});
        visited[0][0] = true;
        int[][] moves = new int[][] {
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
        };

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {   
                Integer[] arr = queue.removeFirst();
                int r = arr[0];
                int c = arr[1];
                if (r == rows - 1 && c == cols - 1) {
                    return length;
                }
                for (int[] m : moves) {
                    int nr = r + m[0];
                    int nc = c + m[1];
                    if (Math.min(nr, nc) < 0 || nr == rows 
                    || nc == cols || grid[nr][nc] == 1 
                    || visited[nr][nc]) {
                        continue;
                    }
                    visited[nr][nc] = true;
                    queue.add(new Integer[] {nr, nc});
                }
            }
            length += 1;
        }
        return -1;
    }
}
