class SegmentTree {
    int total;
    int low;
    int high;
    SegmentTree left;
    SegmentTree right;

    public SegmentTree(int[] nums) {
        SegmentTree tree = this.build(nums, 0, nums.length - 1);
        this.total = tree.total;
        this.low = tree.low;
        this.high = tree.high;
        this.left = tree.left;
        this.right = tree.right;
    }

    public SegmentTree(int total, int low, int high) {
        this.total = total;
        this.low = low;
        this.high = high;
    }

    private SegmentTree build(int[] nums, int l, int r) {
        if (l == r) {
            return new SegmentTree(nums[l], l, r);
        }
        int m = l + (r - l) / 2;
        SegmentTree root = new SegmentTree(0, l, r);
        root.left = this.build(nums, l, m);
        root.right = this.build(nums, m + 1, r);
        root.total = root.left.total + root.right.total;
        return root;
    }

    public void update(int index, int val) {
        if (this.low == this.high) {
            this.total = val;
            return;
        }
        int m = this.low + (this.high - this.low) / 2;
        if (index > m) {
            this.right.update(index, val);
        } else {
            this.left.update(index, val);
        }
        this.total = this.left.total + this.right.total;
    }

    public int query(int L, int R) {
        if (this.low == L && this.high == R) {
            return this.total;
        }
        int m = this.low + (this.high - this.low) / 2;
        if (L > m) {
            return this.right.query(L, R);
        }
        if (R <= m) {
            return this.left.query(L, R);
        }
        return this.left.query(L, m) + this.right.query(m + 1, R);
    }
}
