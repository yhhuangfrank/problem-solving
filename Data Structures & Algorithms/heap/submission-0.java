class MinHeap {
    List<Integer> arr;

    public MinHeap() {
        this.arr = new ArrayList<>();
    }

    public void push(int val) {
        arr.add(val);
        int curr = this.arr.size() - 1;
        int parent = (curr - 1) / 2;
        while (parent >= 0 && this.arr.get(parent) > this.arr.get(curr)) {
            this.swap(parent, curr);
            curr = parent;
            parent = (curr - 1) / 2;
        }
    }

    public Integer pop() {
        int removed = this.top();
        if (removed == -1)
            return -1;
        swap(0, this.arr.size() - 1);
        this.arr.remove(this.arr.size() - 1);
        minHeapify(0);
        return removed;
    }

    public Integer top() {
        if (this.arr.isEmpty())
            return -1;
        return arr.get(0);
    }

    public void heapify(List<Integer> nums) {
        this.arr = nums;
        for (int i = this.arr.size() / 2; i >= 0; i--) {
            minHeapify(i);
        }
    }

    private void minHeapify(int index) {
        int len = this.arr.size();
        int l = 2 * index + 1;
        int r = l + 1;
        int minIndex = index;
        if (l < len && this.arr.get(l) < this.arr.get(minIndex)) {
            minIndex = l;
        }
        if (r < len && this.arr.get(r) < this.arr.get(minIndex)) {
            minIndex = r;
        }
        if (minIndex != index) {
            this.swap(minIndex,index);
            this.minHeapify(minIndex);
        }
    }

    private void swap(int x, int y) {
        int temp = this.arr.get(x);
        this.arr.set(x, this.arr.get(y));
        this.arr.set(y, temp);
    }
}
