class Deque {
    ListNode head;
    ListNode tail;

    public Deque() {
        head = new ListNode(-1);
        tail = new ListNode(-1);
        head.next = tail;
        tail.prev = head;
    }

    public boolean isEmpty() {
        return this.head.next == this.tail;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        ListNode lastNode = this.tail.prev;

        newNode.prev = lastNode;
        lastNode.next = newNode;
        newNode.next = this.tail;
        this.tail.prev = newNode;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
        ListNode firstNode = this.head.next;

        firstNode.prev = newNode;
        newNode.next = firstNode;
        newNode.prev = this.head;
        this.head.next = newNode;
    }

    public int pop() {
        if (isEmpty()) return -1;
    
        ListNode removed = this.tail.prev;
        removed.prev.next = this.tail;
        this.tail.prev = removed.prev;
        return removed.val;
    }

    public int popleft() {
        if (isEmpty()) return -1;
    
        ListNode removed = this.head.next;
        this.head.next = removed.next;
        removed.next.prev = this.head;
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
