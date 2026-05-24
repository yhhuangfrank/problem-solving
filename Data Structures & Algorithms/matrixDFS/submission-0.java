class Solution {
    public int countPaths(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        return dfs(grid, visited, 0, 0);
    }

    private int dfs(int[][] grid, boolean[][] visited, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;
        if (Math.min(i, j) < 0 || i == rows || j == cols || grid[i][j] == 1 || visited[i][j]) {
            return 0;
        }
        if (i == rows - 1 && j == cols - 1) {
            return 1;
        }
        int count = 0;
        visited[i][j] = true;
        int[][] moves = new int[][] {
            {1, 0}, {0,1}, {-1,0}, {0, -1}
        };
        for (int[] move : moves) {
            int di = move[0];
            int dj = move[1];
            int r = i + di;
            int c = j + dj;
            count += dfs(grid, visited, r, c);
        }
        visited[i][j] = false;
        return count;
    }
}
