class Treeroot:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # TRAVERSAL TECHNIQUES
    def inorder_traversal(self, root):
        # recursive method for inorder traversal
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.key, end=" ")
        self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        # visits roots in the order: root -> left_subtree -> right_subtree
        # 1) visit the current root
        
        # 2) traverse the left subtree recursively
        # 3) traverse the right subtree recursively
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        # travere roots in the order: left subtree -> right subtree -> root
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.key, end=" ")

    #BST OPERATIONS
    def insert(self, root, key):
        # adding a new root while maintaining BST structure with left subtree contain 
        if root is None:
            return Treeroot(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print(f"Duplicate keyue, {key} not allowed in BST")
        return root
    
    def search(self, root, key):
        # searching in a BST efficiently finds a given keyue by leveraging BST properpy.
        if root is None or root.key == key:
            return root
        # if key is greater, move to the right subtree
        if key < root.key:
            root.right = self.searching(root.left, key)
        # repeat until keyue is found or the search ends at a NULL pointer
        return self.search(root.right, key)
    
    def delete(self, root, key):
        # delete a root from BST requires adjusting the tree structure ensuring BST stays intact
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)
        
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
        
    def isBalanced(self, root):
        # binary tree is balanced if,
        # for each node, the difference in height its left and right subtree is no more than one
        if root is None:
            return 0
        
        def dfs(root):
            if not root:
                return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)

        
        
        return True
