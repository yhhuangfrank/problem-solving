class LinkedList {
    
    private ListNode head;
    private ListNode tail;

    public LinkedList() {
        this.head = new ListNode(-1);
        this.tail = head;
    }

    public int get(int index) {
        int i = 0;
        ListNode temp = this.head.next;

        while(temp != null) {
            if (i == index) {
                return temp.val;
            }
            temp = temp.next;
            i++;
        }
        return -1;
    }

    public void insertHead(int val) {
        ListNode node = new ListNode(val, this.head.next);
        this.head.next = node;
        if (node.next == null) { //  只有一個 node
            this.tail = node;
        }
    }

    public void insertTail(int val) {
        ListNode node = new ListNode(val, null);
        this.tail.next = node;
        this.tail = node;
    }

    public boolean remove(int index) {
        int i = 0;
        ListNode temp = this.head.next;
        ListNode prev = this.head;

        while(temp != null) {
            if (index == i) {
                prev.next = temp.next;
                if (prev.next == null) {
                    this.tail = prev;
                }
                return true;
            }
            prev = temp;
            temp = temp.next;
            i++;
        }
        return false;
    }

    public List<Integer> getValues() {
        List<Integer> res = new ArrayList<>();
        ListNode temp = this.head.next;
        while (temp != null) {
            res.add(temp.val);
            temp = temp.next;
        }
        return res;
    }

    private class ListNode {
        int val;
        ListNode next;

        public ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
        public ListNode(int val) {
            this.val = val;
        }
    }
}
