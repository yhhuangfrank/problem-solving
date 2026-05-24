class Solution {
    public int minimumSpanningTree(List<List<Integer>> edges, int n) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (List<Integer> edge : edges) {
            int src = edge.get(0);
            int dst = edge.get(1);
            int w = edge.get(2);
            adj.putIfAbsent(src, new ArrayList<>());
            adj.putIfAbsent(dst, new ArrayList<>());
            adj.get(src).add(new int[] {w, dst});
            adj.get(dst).add(new int[] {w, src});
        }

        List<int[]> mst = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int[] neighbor : adj.getOrDefault(0, new ArrayList<>())) {
            int w = neighbor[0];
            int node = neighbor[1];
            minHeap.add(new int[] {w, 0, node}); // {weight, src, dst}
        }
        visited.add(0);

        while (!minHeap.isEmpty()) {
            int[] cur = minHeap.poll();
            int w = cur[0];
            int src = cur[1];
            int dst = cur[2];
            if (visited.contains(dst)) continue;
            mst.add(cur);
            visited.add(dst);
            if (visited.size() == n) {
                break;
            }
            for (int[] neighbor : adj.getOrDefault(dst, new ArrayList<>())) {
                int w2 = neighbor[0];
                int dst2 = neighbor[1];
                if (visited.contains(dst2)) continue;
                minHeap.add(new int[] {w2, dst, dst2});
            }
        }

        if (visited.size() != n) {
            return -1;
        }
        int totalCost = 0;
        for (int[] pair : mst) {
            totalCost += pair[0];
        }
        return totalCost;
    }
}    
