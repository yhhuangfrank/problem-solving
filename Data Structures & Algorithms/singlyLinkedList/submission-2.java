class LinkedList {
    
    private ListNode head;
    private int size = 0;

    public LinkedList() {

    }

    public int get(int index) {
        int i = 0;
        ListNode temp = this.head;
        if (temp == null) return -1;
        while(temp != null && i != index) {
            temp = temp.next;
            i++;
        }
        return temp == null ? -1 : temp.val;
    }

    public void insertHead(int val) {
        this.head = new ListNode(val, this.head);
        this.size++;
    }

    public void insertTail(int val) {
        ListNode node = new ListNode(val, null);
        ListNode temp = this.head;
        if (temp == null) {
            this.head = node;
            this.size++;
            return;
        }
        while (temp.next != null) {
            temp = temp.next;
        }

        temp.next = node;
        this.size++;
    }

    public boolean remove(int index) {
        if (this.head == null) return false;
        if (index == 0) {
            this.head = this.head.next;
            return true;
        }
        int i = 0;
        ListNode temp = this.head;
        while (temp != null && i + 1 != index) {
            temp = temp.next;
            i++;
        }
        if (i + 1 == this.size) return false;
        if (i + 1 == index && temp != null) {
            temp.next = temp.next.next;
            this.size--;
            return true;
        }
        return false;
    }

    public List<Integer> getValues() {
        List<Integer> res = new ArrayList<>();
        ListNode temp = this.head;
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
    }
}
