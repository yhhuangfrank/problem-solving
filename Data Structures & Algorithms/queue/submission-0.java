class Deque {
    ListNode head;
    ListNode tail;
    int size = 0;

    public Deque() {
        
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        if (this.tail == null) {
            this.tail = newNode;
            this.head = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        size++;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
       if (head == null) {
            this.head = newNode;
            this.tail = this.head;
       } else {
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
       }
       size++;
    }

    public int pop() {
        if (isEmpty()) return -1;
        ListNode removed = this.tail;
        if (size == 1) {
            this.head = null;
            this.tail = null;
        } else {
            ListNode newTail = this.tail.prev;
            newTail.next = null;
            this.tail = newTail;
        }
        size--;
        return removed.val;
    }

    public int popleft() {
        if (isEmpty()) return -1;
        ListNode removed = this.head;
        if (size == 1) {
            this.head = null;
            this.tail = null;
        } else {
            ListNode newHead = this.head.next;
            newHead.prev = null;
            this.head = newHead;
        }
        size--;
        return removed.val;
    }

    private class ListNode {
        int val;
        ListNode prev;
        ListNode next;
        
        public ListNode(int val) {
            this.val = val;
        }
    }
}
