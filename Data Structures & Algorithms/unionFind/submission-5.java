class UnionFind {
    private Map<Integer, Integer> parent;
    private Map<Integer, Integer> rank;
    private int numOfComponents;

    public UnionFind(int n) {
        this.parent = new HashMap<>();
        this.rank = new HashMap<>();
        this.numOfComponents = n;

        for (int i = 0; i < n; i++) {
            this.parent.put(i, i);
            this.rank.put(i, 0);
        }
    }

    public int find(int x) {
        int p = this.parent.get(x);
        while (p != this.parent.get(p)) {
            // replaced by grand parent
            this.parent.put(p, this.parent.get(this.parent.get(p)));
            p = this.parent.get(p);
        }
        return p;
    }

    public boolean isSameComponent(int x, int y) {
        return this.find(x) == this.find(y);
    }

    public boolean union(int x, int y) {
        int p1 = this.find(x);
        int p2 = this.find(y);

        if (p1 == p2) return false;

        int r1 = this.rank.get(p1);
        int r2 = this.rank.get(p2);
        if (r1 > r2) {
            this.parent.put(p2, p1);
        } else if (r2 > r1) {
            this.parent.put(p1, p2);
        } else {
            this.parent.put(p2, p1);
            this.rank.put(p1, this.rank.get(p1) + 1);
        }
        this.numOfComponents--;
        return true;
    }

    public int getNumComponents() {
        return numOfComponents;
    }
}
