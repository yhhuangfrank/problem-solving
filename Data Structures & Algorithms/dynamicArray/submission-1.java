class DynamicArray {

    int[] arr;
    int size;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
       this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.size == this.arr.length) {
            this.resize();
        }
        this.arr[this.size] = n;
        this.size++;
    }

    public int popback() {
        return this.arr[--this.size];
    }

    private void resize() {
        if(this.size == this.arr.length) {
            int newCapacity = this.size << 1;
            int[] newArr = new int[newCapacity];
            for (int i = 0; i < this.size; i++) {
                newArr[i] = this.arr[i];
            }
            this.arr = newArr;
        }
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.arr.length;
    }
}
