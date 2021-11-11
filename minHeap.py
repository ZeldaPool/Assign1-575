'''CECS 575 - Assignment 1
Min Heap

Harsh Manoj Jain  -   027950193
Smit Rana         -   027980613
'''

from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NullNode(object):
    def __init__(self):
        self.val = -1
        self.left = None
        self.right = None

class OddFilter:
    filtered_arr = []
    
    #self.filtered_arr.append(self.input_object[i])
    
    def __init__(self, input_object):
        self.len_input_object = len(input_object)
        self.i = 0
    
        while True:
            try:
                if self.has_next:
                    self.next(self.i)
            except StopIteration:
                break

    def has_next(self):
        return True if self.i < self.len_input_object else False

    def next(self):
        if self.has_next(self.i):
            if (self.input_object[i] % 2) != 0:
                self.i += 1
                return self.input_object[self.i-1]
        return 


class Heap(Node):

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
    
    # Returns a list of values in inorder
    def inorder(self, root, result):
        if root:
            result.append(root.val)
            self.inorder(root.left, result)
            self.inorder(root.right, result)

        return result

    def print_inorder(self, root):
        inorder_result = self.inorder(root, [])
        for i in inorder_result:
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

    def heap_toArray(self, root):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        heap_array = []

        while queue:

            curr = queue.popleft()

            heap_array.append(curr.val)
            # print(curr.val, end=' ')

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return heap_array

    def heap_toString(self, root):
        heap_iter = iter(self.heap_toArray(root))
        heap_string = "["

        while True:
            try:
                heap_string += str(next(heap_iter))
            except StopIteration:
                break
            
            heap_string += ", "
        return heap_string + "]"


def heap_create():

    heapC = HeapOperations()
    heapC2 = Heap()    
       
    root = Node(50)
    heapC.heap_insert(root, 37)
    heapC.heap_insert(root, 24)
    heapC.heap_insert(root, 43)
    heapC.heap_insert(root, 70)
    heapC.heap_insert(root, 61)

    print("Odds in Preorder:", end=" ")
    heapC2.print_odd_preorder(root)
    print("\nPostorder:", end=" ")
    heapC2.print_postorder(root)
    print("\nToArray:", end=" ")
    print(heapC.heap_toArray(root))
    print("ToString:", end=" ")
    print(heapC.heap_toString(root))
    print("Inorder:", end=" ")
    heapC2.print_inorder(root)


if __name__ == "__main__":

    heap_create()


