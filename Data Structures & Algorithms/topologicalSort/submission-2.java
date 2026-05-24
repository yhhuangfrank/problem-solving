class Solution {
    private Map<Integer, List<Integer>> adj;
    private Set<Integer> visit;
    private Set<Integer> path;
    private List<Integer> res;

    public List<Integer> topologicalSort(int n, int[][] edges) {
        adj = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            int src = edge[0];
            int dst = edge[1];
            adj.get(src).add(dst);
        }

        visit = new HashSet<>();
        path = new HashSet<>();
        res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!dfs(i)) return new ArrayList<>();
        }
        Collections.reverse(res);
        return res;
    }

    private boolean dfs(int i) {
        if (path.contains(i)) return false;
        if (visit.contains(i)) return true;

        visit.add(i);
        path.add(i);
        for (Integer neigh : adj.get(i)) {
            if (!dfs(neigh)) return false;
        }
        path.remove(i);
        res.add(i);
        return true;
    }
}
