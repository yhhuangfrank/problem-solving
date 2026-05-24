class TreeMap {

    TreeNode root;

    public TreeMap() {
        
    }

    public void insert(int key, int val) {
        TreeNode node = insert(this.root, key, val);
        this.root = node;
    }

    public TreeNode insert(TreeNode root, int key, int val) {
        if (root == null) {
            return new TreeNode(key, val);
        }
        if (key > root.key) {
            root.right = insert(root.right, key, val);
        } else if (key < root.key) {
            root.left = insert(root.left, key, val);
        } else {
            root.val = val;
        }
        return root;
    }

    public int get(int key) {
        return get(this.root, key);
    }

    public int get(TreeNode root, int key) {
        if (root == null) return -1;
        if (root.key == key) return root.val;
        if (root.key > key) {
            return get(root.left, key);
        } else {
            return get(root.right, key);
        }
    }

    public int getMin() {
        TreeNode minNode = getMin(this.root);
        return minNode != null ? minNode.val : -1;
    }

    public TreeNode getMin(TreeNode root) {
        TreeNode temp = root;
        while (temp != null && temp.left != null) {
            temp = temp.left;
        }
        return temp;
    }

    public int getMax() {
        TreeNode maxNode = getMax(this.root);
        return maxNode != null ? maxNode.val : -1;
    }

    public TreeNode getMax(TreeNode root) {
        TreeNode temp = root;
        while (temp != null && temp.right != null) {
            temp = temp.right;
        }
        return temp;
    }

    public void remove(int key) {
       this.root = remove(this.root, key);
    }

    public TreeNode remove(TreeNode root, int key) {
        if (root == null) return null;
        if (key > root.key) {
            root.right = remove(root.right, key);
        } else if (key < root.key) {
            root.left = remove(root.left, key);
        } else {
            // case 1: 0 or 1 child
            if (root.right == null) return root.left;
            if (root.left == null) return root.right;
            // case 2: 2 children
            TreeNode minNode = getMin(root.right);
            root.key = minNode.key;
            root.val = minNode.val;
            root.right = remove(root.right, minNode.key);
        }
        return root;
    }

    public List<Integer> getInorderKeys() {
        List<Integer> result = new ArrayList<>();
        if (this.root == null) return result;
        getInorderKeys(this.root, result);
        return result;
    }

    public void getInorderKeys(TreeNode root, List<Integer> result) {
        if (root.left != null) {
            getInorderKeys(root.left, result);
        }
        result.add(root.key);
        if (root.right != null) {
            getInorderKeys(root.right, result);
        }
    }

    private class TreeNode {
        int key;
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
}
