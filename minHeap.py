'''CECS 575 - Assignment 1
Min Heap

Harsh Manoj Jain  -   027950193
Smit Rana         -   027980613
'''

from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Heap:
    def __init__(self, heapType):
        self.heapType = heapType

<<<<<<< Updated upstream
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
=======
    def __repr__(self, root):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        heap_array = []

        while queue:

            curr = queue.popleft()
>>>>>>> Stashed changes

            heap_array.append(curr.val)

<<<<<<< Updated upstream
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
=======
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return heap_array

    def __str__(self, root):
        heap_iterator = iter(self.__repr__(root))
        heap_string = ""

        while True:
            try:
                heap_string += str(next(heap_iterator))
            except StopIteration:
                break

            heap_string += ", "
        return heap_string[:len(heap_string)-2]

    def addElement(self, root, val):
        return self.heapType.append(root, val)
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
    def print_postorder(self, root):
        postorder_result = self.postorder(root, [])
        for i in postorder_result:
            print(i, end=" ")
    
=======
>>>>>>> Stashed changes
    # Returns a list of values in inorder
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)

        return result


<<<<<<< Updated upstream
class HeapOperations(Heap) :
        
    minHeap = Heap()
        
=======
class HeapOperations:
    def min_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.min_depth(root.left), self.min_depth(root.right))

>>>>>>> Stashed changes
    # Inserts value into the min heap and creates node when necessary
    def heap_insert(self, root, val):
        if root is None:
            return Node(val)

<<<<<<< Updated upstream
        left_height = self.minHeap.min_depth(root.left)
        right_height = self.minHeap.min_depth(root.right)
=======
        left_height = self.min_depth(root.left)
        right_height = self.min_depth(root.right)

        temporary_node = val
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======

class MinHeap(HeapOperations):
    def isMinOrMaxHeap(self, root, val):
        return val <= root.val


class MaxHeap(HeapOperations):
    def isMinOrMaxHeap(self, root, val):
        return val >= root.val


class OddFilter:
    filtered_result = None

    def __init__(self, unfiltered_result):
        self.unfiltered_result = unfiltered_result
        self.filter()

    def filter(self):
        self.filtered_result = list(filter(lambda x: x % 2 == 1, self.unfiltered_result))
        return self.filtered_result


class OddHeapDecorator:
    filtered_result = None
    def __init__(self, unfiltered_result, root):
        self.filtered_result = list(filter(lambda x: x % 2 == 1, unfiltered_result))
    
    def __str__(self):
        result = ""

        for i in self.filtered_result:
            result += str(i) + ", "
        
        return result[:len(result)-2]

    def __repr__(self):
        return list(self.filtered_result)
    

def heap_create():
    heap_object = Heap(heapType=MinHeap())
>>>>>>> Stashed changes

    heapC = HeapOperations()
    heapC2 = Heap()    
       
    root = Node(50)
<<<<<<< Updated upstream
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
=======
    heap_object.addElement(root, 37)
    heap_object.addElement(root, 24)
    heap_object.addElement(root, 43)
    heap_object.addElement(root, 70)
    heap_object.addElement(root, 61)

    print("Preorder:", end=" ")
    print(heap_object.preorder(root, []))
    print("Postorder:", end=" ")
    print(heap_object.postorder(root, []))
    print("ToArray:", end=" ")
    print(heap_object.__repr__(root))
    print("ToString:", end=" ")
    print(heap_object.__str__(root))
    print("Inorder:", end=" ")
    print(heap_object.inorder(root, []))
    unfiltered_arr = heap_object.preorder(root, [])
    decoTest = OddHeapDecorator(unfiltered_arr, root)
    print("ToArray OddDecorator:", end=" ")
    print(decoTest.__repr__())
    print("ToString OddDecorator:", end=" ")
    print(decoTest.__str__())
>>>>>>> Stashed changes


if __name__ == "__main__":
    heap_create()


