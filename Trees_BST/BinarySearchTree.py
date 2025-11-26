class TreeNode:
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
        # visits nodes in the order: root -> left_subtree -> right_subtree
        # 1) visit the current node
        
        # 2) traverse the left subtree recursively
        # 3) traverse the right subtree recursively
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        # travere nodes in the order: left subtree -> right subtree -> root
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.val, end=" ")

    #BST OPERATIONS
    def insertion(self, node, val):
        # adding a new node while maintaining BST structure with left subtree contain 
        if node is None:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self.insert(node.left, val)
        elif val > node.val:
            node.right = self.insert(node.right, val)
        else:
            print(f"Duplicate value, {val} not allowed in BST")
        return node

    def searching(self, node, val):
        # searching in a BST efficiently finds a given value by leveraging BST properpy.
        if node is None:
            return "Not Found"
        