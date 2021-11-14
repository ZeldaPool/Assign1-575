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
    filtered_result = []

    def __init__(self, unfiltered_result):
        self.unfiltered_result = unfiltered_result
        self.filter()

    def filter(self):
        self.filtered_result = list(filter(lambda x: x % 2 == 1, self.unfiltered_result))
        for i in self.filtered_result:
            print(i, end=" ")
        return self.filtered_result


class Heap:
    def __init__(self, heapType):
        self.heapType = heapType

    def min_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.min_depth(root.left), self.min_depth(root.right))

    # Returns a list of odd values in the tree in preorder
    def preorder(self, root, result):
        if root:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)
        return result

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


class HeapOperations(Heap):

    # heap_object = Heap()

    # Inserts value into the min heap and creates node when necessary
    def append(self, root, val):
        if root is None:
            return Node(val)

        left_height = self.Heap.min_depth(root.left)
        right_height = self.Heap.min_depth(root.right)

        temporary_node = val

        if self.isMinOrMaxHeap(root, val):
            temporary_node = root.val
            root.val = val

        if left_height <= right_height:
            root.left = self.append(root.left, temporary_node)
        else:
            root.right = self.append(root.right, temporary_node)
        return root

    def isMinOrMaxHeap(self, root, val):
        pass

    def toarray(self, root):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        heap_array = []

        while queue:

            curr = queue.popleft()

            heap_array.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return heap_array

    def tostring(self, root):
        heap_iterator = iter(self.toarray(root))
        heap_string = "["

        while True:
            try:
                heap_string += str(next(heap_iterator))
            except StopIteration:
                break

            heap_string += ", "
        return heap_string + "]"


class MinHeap(HeapOperations):
    def isMinOrMaxHeap(self, root, val):
        return val <= root.val


class MaxHeap(HeapOperations):
    def isMinOrMaxHeap(self, root, val):
        return val >= root.val


def heap_create():

    heap_object = Heap(MinHeap)
    # heapType = MinHeap()

    root = Node(50)
    heap_object.heapType.append(root, 37)
    # heapType.append(root, 24)
    # heapType.append(root, 43)
    # heapType.append(root, 70)
    # heapType.append(root, 61)

    print("Odds in Preorder:", end=" ")
    OddFilter(heap_object.preorder(root, []))
    print("\nPostorder:", end=" ")
    heap_object.print_postorder(root)
    print("\nToArray:", end=" ")
    print(heap_object.toarray(root))
    print("ToString:", end=" ")
    print(heap_object.tostring(root))
    print("Inorder:", end=" ")
    heap_object.print_inorder(root)


if __name__ == "__main__":

    heap_create()
