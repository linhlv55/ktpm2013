import unittest
from math import sqrt
from triangle import checkTriangle
class MyTest(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(checkTriangle(-1,2,4),-1)
    def test_1_2(self):
        self.assertEqual(checkTriangle(1,-1,4),-1)
    def test_1_3(self):
        self.assertEqual(checkTriangle(1,1,-4),-1)
    def test_1_4(self):
        self.assertEqual(checkTriangle(-1,-2,-4),-1)
    def test_1_5(self):
        self.assertEqual(checkTriangle(2,2,10**39),-1)
    def test_1_6(self):
        self.assertEqual(checkTriangle(8* 10**39,100,410),-1)
    def test_1_7(self):
        self.assertEqual(checkTriangle(8* 10**39,10**40 ,410),-1)
    def test_1_8(self):
        self.assertEqual(checkTriangle(8* 10**39,8* 10**39,8* 10**39),-1)
    def test_2(self):    
        self.assertEqual(checkTriangle(4,1,2),0)
    def test_3(self): 
        self.assertEqual(checkTriangle(1,2,4),0)
	def test_4(self): 
        self.assertEqual(checkTriangle(1,1,1),0)
    def test_5(self): 
        self.assertEqual(checkTriangle(1,4,2),0)
    def test_6(self): 
        self.assertEqual(checkTriangle(2,2,2),1)
    def test_7(self): 
        self.assertEqual(checkTriangle(2,2,3),4)
    def test_8(self): 
        self.assertEqual(checkTriangle(3,4,5),3)
    def test_9(self): 
        self.assertEqual(checkTriangle(3,5,6),5)
    def main():
        unittest.main()
if __name__ == '__main__':
    unittest.main()     
