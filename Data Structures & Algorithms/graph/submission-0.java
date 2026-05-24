class Graph {
    private Map<Integer, Node> nodes;

    public Graph() {
        nodes = new HashMap<>();
    }

    public void addEdge(int src, int dst) {
        Node srcNode = nodes.get(src) == null ? new Node(src) : nodes.get(src);
        Node dstNode = nodes.get(dst) == null ? new Node(dst) : nodes.get(dst);
        srcNode.neighbors.add(dstNode.val);

        nodes.put(src, srcNode);
        if (nodes.get(dst) == null) {
            nodes.put(dst, dstNode);
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
        return dfs(srcNode, dst);
    }

    private boolean dfs(Node node, int dst) {
        if (node.val == dst)
            return true;
        for (Integer i : node.neighbors) {
            Node n = nodes.get(i);
            if (!n.isVisited && dfs(n, dst)) {
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
