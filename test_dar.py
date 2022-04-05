import unittest
import random
from Dar import DynArray

class MyTests(unittest.TestCase):

    def test_insert(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        for j in range(10):
            da.insert(random.randint(0,4),random.randint(1,14))
        self.assertEqual(16,da.capacity)
        for j in range(20):
            da.insert(random.randint(0,15),random.randint(0,15))
        self.assertEqual(64,da.capacity)

    def test_delete(self):
        da = DynArray()
        for i in range(100):
            da.append(i)
        for j in range(random.randint(0,100)):
            #self.assertLess(j,i)
            #self.assertGreater(j,0)
            da.delete(j)

if __name__ == '__main__':
    unittest.main()