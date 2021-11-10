'''CECS 575 - Assignment 1
Min Heap

Harsh Manoj Jain  -   027950193
Smit Rana         -   027980613
'''


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Heap(Node):

    def heap_create(self):
        
        root = Node(50)
        self.heap_insert(root, 37)
        self.heap_insert(root, 24)
        self.heap_insert(root, 43)
        self.heap_insert(root, 70)
        self.heap_insert(root, 61)

        print("Odds in Preorder:", end=" ")
        self.minHeap.print_odd_preorder(root)
        print("\nPostorder:", end=" ")
        self.minHeap.print_postorder(root)

    def min_depth(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.min_depth(root.right) + 1

        if root.right is None:
            return self.min_depth(root.left) + 1

        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

    # Returns a list of odd values in the tree in preorder
    def odd_preorder(self, root, result):
        if root:
            if (root.val % 2) != 0:
                result.append(root.val)
            self.odd_preorder(root.left, result)
            self.odd_preorder(root.right, result)
        return result

    def print_odd_preorder(self, root):
        odd_preorder_result = self.odd_preorder(root, [])
        for i in odd_preorder_result:
            print(i, end=" ")

    # Returns a list of values in postorder
    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.val)

        return result

    def print_postorder(self, root):
        postorder_result = self.postorder(root, [])
        for i in postorder_result:
            print(i, end=" ")

class HeapOperations(Heap) :
        
    minHeap = Heap()
        
    # Inserts value into the min heap and creates node when necessary
    def heap_insert(self, root, val):
        if root is None:
            return Node(val)

        left_height = self.minHeap.min_depth(root.left)
        right_height = self.minHeap.min_depth(root.right)

        if val < root.val:
            temporary_node = root.val
            root.val = val

            if left_height <= right_height:
                root.left = self.heap_insert(root.left, temporary_node)
            else:
                root.right = self.heap_insert(root.right, temporary_node)

        else:
            if left_height <= right_height:
                root.left = self.heap_insert(root.left, val)
            else:
                root.right = self.heap_insert(root.right, val)

        return root


if __name__ == "__main__":

    heapOperations = Heap()
    heapOperations.heap_create()


