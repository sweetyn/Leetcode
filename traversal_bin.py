"""graph traversal, binary search tree, OOP

   1
 2   3
4 5
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1"""


class Node(object):

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):

    if root:
        print("left")
        inorder(root.left)
        print("root")
        print(root.val)

        inorder(root.right)
        print("right")


def preorder(root):

    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)




# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print (inorder(root))
# print ("Preorder : " + preorder(root))
# print ("Ineorder : " + inorder(root))
# print ("Preorder : " + preorder(root))
