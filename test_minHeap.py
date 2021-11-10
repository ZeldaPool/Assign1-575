import unittest
from minHeap import Node, Heap


class TestMinHeap(unittest.TestCase):
    def test_minHeap(self):
        minHeap = Heap()

        # Checks if the root is the smallest element after every insert
        root = Node(50)
        result = minHeap.insert(root, 30)
        self.assertEqual(result.val, 30)
        result = minHeap.insert(root, 20)
        self.assertEqual(result.val, 20)
        result = minHeap.insert(root, 70)
        self.assertEqual(result.val, 20)
        minHeap.insert(root, 80)

        # Checks preorder
        odd_preorder_result = minHeap.odd_preorder(root, [])
        self.assertEqual(odd_preorder_result, [])

        # Checks postorder
        postorder_result = minHeap.postorder(root, [])
        self.assertEqual(postorder_result, [70, 50, 80, 30, 20])
