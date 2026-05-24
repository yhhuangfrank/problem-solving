class Graph {
    private Map<Integer, Node> nodes;
    private Map<Integer, Boolean> visited;

    public Graph() {
        nodes = new HashMap<>();
        visited = new HashMap<>();
    }

    public void addEdge(int src, int dst) {
        Node srcNode = nodes.get(src) == null ? new Node(src) : nodes.get(src);
        Node dstNode = nodes.get(dst) == null ? new Node(dst) : nodes.get(dst);
        srcNode.neighbors.add(dstNode.val);

        nodes.put(src, srcNode);
        visited.put(src,false);
        if (nodes.get(dst) == null) {
            nodes.put(dst, dstNode);
            visited.put(dst,false);
        }
    }

    public boolean removeEdge(int src, int dst) {
        Node srcNode = nodes.get(src);
        Node dstNode = nodes.get(dst);
        if (srcNode == null || dstNode == null) return false;

        srcNode.neighbors.remove(dst);
        return true;
    }

    public boolean hasPath(int src, int dst) {
        Node srcNode = nodes.get(src);
        if (srcNode == null) return false;
        boolean isPathExist = dfs(srcNode, dst);
        clearVisited();
        return isPathExist;
    }

    public void clearVisited() {
        for (int k : visited.keySet()) {
            visited.put(k, false);
        }
    }

    private boolean dfs(Node node, int dst) {
        if (node.val == dst)
            return true;
        for (Integer i : node.neighbors) {
            Node n = nodes.get(i);
            if (!visited.get(n.val) && dfs(n, dst)) {
                return true;
            }
        }
        return false;
    }

    private class Node {
        int val;
        Set<Integer> neighbors;
        boolean isVisited;

        public Node(int val) {
            this.val = val;
            this.neighbors = new HashSet<>();
        }
    }
}
