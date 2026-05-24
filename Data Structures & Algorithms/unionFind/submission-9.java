class UnionFind {
    private int n;
    private Map<Integer, Integer> nodes;
    private Map<Integer, Integer> rank;

    public UnionFind(int n) {
        this.n = n;
        this.nodes = new HashMap<>();
        this.rank = new HashMap<>();
        for (int i = 0; i < n; i++) {
            this.nodes.put(i, i);
            this.rank.put(i, 1);
        }
    }

    public int find(int x) {
        int parent = this.nodes.get(x);
        while (parent != this.nodes.get(parent)) {
            this.nodes.put(parent, this.nodes.get(this.nodes.get(parent)));
            parent = this.nodes.get(parent);
        }
        return parent;
    }

    public boolean isSameComponent(int x, int y) {
        return this.find(x) == this.find(y);
    }

    public boolean union(int x, int y) {
        int p1 = this.find(x), p2 = this.find(y);
        if (p1 == p2) {
            return false;
        }
        int r1 = this.rank.get(p1), r2 = this.rank.get(p2);
        if (r2 <= r1) {
            this.rank.put(p1, this.rank.get(p1) + 1);
            this.nodes.put(p2, p1);
        } else {
            this.rank.put(p2, this.rank.get(p2) + 1);
            this.nodes.put(p1, p2);
        }
        this.n -= 1;
        return true;
    }

    public int getNumComponents() {
        return this.n;
    }
}
