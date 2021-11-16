import unittest
from minHeap import MinHeap, MaxHeap, Node, Heap, OddFilter, OddHeapDecorator


class TestHeap(unittest.TestCase):  
    def test_MinHeap(self):
        minHeap = Heap(heapType=MinHeap())

        # Checks if the root is the smallest element after every insert
        root = Node(50)
        result = minHeap.addElement(root, 37)
        self.assertEqual(result.val, 37)
        result = minHeap.addElement(root, 24)
        self.assertEqual(result.val, 24)
        result = minHeap.addElement(root, 43)
        self.assertEqual(result.val, 24)
        minHeap.addElement(root, 70)
        minHeap.addElement(root, 61)

        # Checks preorder
        self.assertEqual(minHeap.preorder(root, []), [24, 43, 50, 61, 37, 70], "Pre-Order does not match")

        # Checks postorder
        postorder_result = minHeap.postorder(root, [])
        self.assertEqual(postorder_result, [50, 61, 43, 70, 37, 24], "Post-Order does not match")

        # Checks inorder
        inorder_result = minHeap.inorder(root, [])
        self.assertEqual(inorder_result, [50, 43, 61, 24, 70, 37], "In-Order does not match")

        # Checks toArray
        toarray_result = minHeap.__repr__(root)
        self.assertEqual(toarray_result, [24, 43, 37, 50, 61, 70])

        # Checks toString
        tostring_result = minHeap.__str__(root)
        self.assertEqual(tostring_result, '24, 43, 37, 50, 61, 70', "Strings do not match")

        # Checks OddFilter
        oddFilter = OddFilter(minHeap.preorder(root, []))
        oddFilter_result = oddFilter.filter()
        self.assertEqual(oddFilter_result, [43, 61, 37])

        # Checks OddHeapDecorator
        oddHeapDecorator_result = OddHeapDecorator(minHeap.preorder(root, []), root)
        self.assertEqual(oddHeapDecorator_result.__repr__(), [43, 61, 37])


    def test_MaxHeap(self):
        minHeap = Heap(heapType=MaxHeap())

        root = Node(50)
        result = minHeap.addElement(root, 37)
        self.assertEqual(result.val, 50)
        minHeap.addElement(root, -24)
        minHeap.addElement(root, 43)
        minHeap.addElement(root, -70)
        minHeap.addElement(root, 61)

        # Checks postorder
        postorder_result = minHeap.postorder(root, [])
        self.assertEqual(postorder_result, [37, 43, 50, -70, -24, 61])

        # Checks preorder
        self.assertEqual(minHeap.preorder(root, []), [61, 50, 37, 43, -24, -70], "Pre-Order does not match")
    
if __name__ == "__main__":
    unittest.main()
    