class Node:
    def __init__(self, total, s, e):
        self.total = total
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)
        node = Node(0, l, r)
        m = (l + r) // 2
        node.left = self.build(nums, l, m)
        node.right = self.build(nums, m + 1, r)
        node.total = node.left.total + node.right.total
        return node
    
    def update(self, index: int, val: int) -> None:
        if index < self.root.s or index > self.root.e:
            return
        
        def updateHelper(root, idx, v):
            if root.s == root.e and root.s == idx:
                root.total = v
                return
            m = (root.s + root.e) // 2
            if index > m:
                updateHelper(root.right, idx, v)
            else:
                updateHelper(root.left, idx, v)
            root.total = root.left.total + root.right.total
        
        updateHelper(self.root, index, val)
    
    def query(self, L: int, R: int) -> int:
        if R < self.root.s or L > self.root.e:
            return 0
        
        def queryHelper(root, l, r):
            if root.s == l and root.e == r:
                return root.total
            m = (root.s + root.e) // 2
            if l > m:
                return queryHelper(root.right, l, r)
            elif r <= m:
                return queryHelper(root.left, l, r)
            else:
                return queryHelper(root.left, l, m) + queryHelper(root.right, m + 1, r)

        return queryHelper(self.root, L, R)

