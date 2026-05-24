class SegmentTree {
    private int sum;
    private int L;
    private int R;
    private SegmentTree left;
    private SegmentTree right;

    public SegmentTree(int[] nums) {
        SegmentTree tree = build(nums, 0, nums.length - 1);
        this.sum = tree.sum;
        this.L = tree.L;
        this.R = tree.R;
        this.left = tree.left;
        this.right = tree.right;
    }

    public SegmentTree(int sum, int l, int r) {
        this.sum = sum;
        this.L = l;
        this.R = r;
    }

    private SegmentTree build(int[] nums, int l, int r) {
        if (l == r) {
            return new SegmentTree(nums[l], l, r);
        }
        int m = l + (r - l) / 2;
        SegmentTree root = new SegmentTree(0, l, r);
        root.left = build(nums, l, m);
        root.right = build(nums, m + 1 , r);
        root.sum = root.left.sum + root.right.sum;
        return root;
    }

    public void update(int index, int val) {
        if (this.L == this.R && this.L == index) {
            this.sum = val;
            return;
        }
        int m = (this.L + this.R) / 2;
        if (index > m) {
            this.right.update(index, val);
        } else {
            this.left.update(index, val);
        }
        this.sum = this.left.sum + this.right.sum;
    }

    public int query(int L, int R) {
        if (this.L == L && this.R == R) {
            return this.sum;
        }
        int m = (this.L + this.R) / 2;
        if (L > m) {
            return this.right.query(L, R);
        } else if (R <= m) {
            return this.left.query(L, R);
        } else {
            // two ways
            return this.left.query(L, m) + this.right.query(m + 1, R);
        }
    }
}
