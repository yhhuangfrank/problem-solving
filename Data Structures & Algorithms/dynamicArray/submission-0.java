class DynamicArray {

    int[] arr;
    int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == arr.length) {
            this.resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        return arr[--size];
    }

    private void resize() {
        if(size == arr.length) {
            int newCapacity = size << 1;
            int[] newArr = new int[newCapacity];
            for (int i = 0; i < size; i++) {
                newArr[i] = arr[i];
            }
            arr = newArr;
        }
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.arr.length;
    }
}
