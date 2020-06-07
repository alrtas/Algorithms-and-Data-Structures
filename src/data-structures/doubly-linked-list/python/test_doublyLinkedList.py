import unittest
import doublyLinkedList as d


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.my_list = d.DoublyLinkedList();
        self.my_list.append(1)
        self.my_list.append(2)
        self.my_list.append(3)
        self.my_list.append(4)
        self.my_list.append(5)

    def tearDown(self):
        del self.my_list

    def test_length(self):
        self.assertEqual(self.my_list.length(), 5)

    def test_append(self):
        self.my_list.append(6)
        self.my_list.append(7)
        self.assertEqual(self.my_list.length(), 7)


if __name__ == '__main__':
    unittest.main()
