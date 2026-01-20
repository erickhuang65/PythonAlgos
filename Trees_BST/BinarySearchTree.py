class Treeroot:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # TRAVERSAL TECHNIQUES
    def inorder_traversal(self, root):
        # recursive method for inorder traversal
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        # visits roots in the order: root -> left_subtree -> right_subtree
        # 1) visit the current root
        
        # 2) traverse the left subtree recursively
        # 3) traverse the right subtree recursively
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        # travere roots in the order: left subtree -> right subtree -> root
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.val, end=" ")

    #BST OPERATIONS
    def insert(self, root, val):
        # adding a new root while maintaining BST structure with left subtree contain 
        if root is None:
            return Treeroot(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            print(f"Duplicate value, {val} not allowed in BST")
        return root
    
    def search(self, root, val):
        # searching in a BST efficiently finds a given value by leveraging BST properpy.
        if root is None or root.val == val:
            return root
        # if val is greater, move to the right subtree
        if val < root.val:
            root.right = self.searching(root.left, val)
        # repeat until value is found or the search ends at a NULL pointer
        return self.search(root.right, val)
    
    def delete(self, root, val):
        # delete a root from BST requires adjusting the tree structure ensuring BST stays intact
        if not root:
            return root
        
        if val < root.val:
            root.left = self.delete(root.left, val)

        elif val > root.val:
            root.right = self.delete(root.right, val)
        
        else:
            # if left child is NULL
            if not root.left:
                return root.right
            # if right child is NULL
            elif root.right is None:
                return root.left
            
            # Case 3: root has two children
            # find the minimum in the right subtree
            cur = root
            while cur.left:
                cur.left
            root.val = cur.val
            root.right = self.delete(root.right, root.val)
        return root
    
    def maxDepth(self, root):
        # returns the depth (or height) of a binary tree
        # depth of.a BST refers to the number of nodes along the longest path from the root node
        # if tree is empty the depth is 0
        if root is None:
            return 0
        # create a var to store the recursive call of traversing to the left
        left_depth = self.maxDepth(root.left)
        # create a var to store the recursive call of traversing to the right
        right_depth = self.maxDepth(root.right)
        # compare left var to right var
        return max(left_depth, right_depth) + 1
        
    # helper function to calculate depth of a Tree
    def depth(self, node):
        if not node:
            return 0
        # create a variable to recursively traverse and grabs the height of left
        left_depth = self.depth(node.left)
        if left_depth == -1:
            return -1
        # create a variable to recursively traverse and grabs the height of right
        right_depth = self.depth(node.right)
        if right_depth == -1:
            return -1
        # if the absolute val of () >= 1
        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        # binary tree is balanced if, for each node, the difference in height its left and right subtree is no more than one
        return self.depth(root) != 1

    # find the smallest difference between the values of any two different nodes
    def minDiffInBST(self, root):
        min_diff = float('inf')
        pass

    def maxDepth(self, root):
        pass