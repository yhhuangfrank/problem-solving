class Graph {
    private Map<Integer, Node> nodes;
    private Set<Integer> visited;

    public Graph() {
        this.nodes = new HashMap<>();
        this.visited = new HashSet<>();
    }

    public void addEdge(int src, int dst) {
        this.nodes.putIfAbsent(src, new Node(src));
        this.nodes.putIfAbsent(dst, new Node(dst));
        Node srcNode = this.nodes.get(src);
        Node dstNode = this.nodes.get(dst);
        srcNode.neighbors.add(dstNode.val);
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
        visited.clear();
        return isPathExist;
    }

    private boolean dfs(Node node, int dst) {
        if (node.val == dst)
            return true;
        visited.add(node.val);
        for (Integer i : node.neighbors) {
            Node n = nodes.get(i);
            if (!visited.contains(n.val) && dfs(n, dst)) {
                return true;
            }
        }
        return false;
    }

    private class Node {
        int val;
        Set<Integer> neighbors;

        public Node(int val) {
            this.val = val;
            this.neighbors = new HashSet<>();
        }
    }
}
