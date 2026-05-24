class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.buildHelper(nums, 0, len(nums) - 1)
    
    def buildHelper(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)
        m = l + (r - l) // 2
        root = Node(0, l, r)
        root.left = self.buildHelper(nums, l , m)
        root.right = self.buildHelper(nums, m + 1, r)
        root.total = root.left.total + root.right.total
        return root
    
    def update(self, index: int, val: int) -> None:

        def updateHelper(node, index, val):
            if node.L == node.R:
                node.total = val
                return
            m = node.L + (node.R - node.L) // 2
            if index > m:
                updateHelper(node.right, index, val)
            else:
                updateHelper(node.left, index, val)
            node.total = node.left.total + node.right.total
        
        updateHelper(self.root, index, val)
    
    def query(self, L: int, R: int) -> int:

        def queryHelper(node, L, R):
            if L == node.L and R == node.R:
                return node.total
            m = node.L + (node.R - node.L) // 2
            if L > m:
                return queryHelper(node.right, L, R)
            elif R <= m:
                return queryHelper(node.left, L, R)
            else:
                return (
                    queryHelper(node.left, L, m) +
                    queryHelper(node.right, m + 1, R)
                )
            
        return queryHelper(self.root, L, R)

